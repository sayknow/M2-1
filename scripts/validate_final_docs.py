"""Offline final-document links, source baseline and evidence consistency checks.

This validates technical records, not user participation or individual authorship.
It does not load .env, contact providers or spend AI quota.
"""
import ast
import hashlib
import json
import re
import sqlite3
import unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FINAL = ROOT / 'docs/final'


def read_json(path):
    return json.loads(path.read_text())


def literal_assignment(path, name):
    tree = ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise AssertionError(f'Missing literal {name}: {path}')


def markdown_anchors(content):
    """GitHub-style heading anchors, including repeated heading suffixes."""
    anchors = set()
    counts = {}
    for line in content.splitlines():
        match = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        heading = re.sub(r'<[^>]+>', '', match.group(1)).lower().replace('`', '')
        slug = ''.join(c for c in heading if c in '-_' or c.isspace()
                       or unicodedata.category(c)[0] not in 'PS')
        slug = re.sub(r'\s', '-', slug.strip())
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        anchors.add(slug + (f'-{count}' if count else ''))
    return anchors


class HtmlReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = set()
        self.slide_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.references.extend(attrs[key] for key in ('href', 'src') if attrs.get(key))
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'section' and 'slide' in attrs.get('class', '').split():
            self.slide_count += 1


def document_references(path):
    content = path.read_text()
    if path.suffix == '.html':
        parser = HtmlReferences()
        parser.feed(content)
        return parser.references
    return [m.group(1).strip().strip('<>')
            for m in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', content)]


def local_reference(path, target):
    target = target.strip().strip('<>')
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
    assert resolved.is_relative_to(ROOT), f'Outside project: {path.relative_to(ROOT)}: {target}'
    assert resolved.exists(), f'Broken link: {path.relative_to(ROOT)}: {target}'
    if parsed.fragment and resolved.suffix in {'.md', '.html'}:
        if resolved.suffix == '.md':
            anchors = markdown_anchors(resolved.read_text())
        else:
            parser = HtmlReferences()
            parser.feed(resolved.read_text())
            anchors = parser.ids
        assert unquote(parsed.fragment) in anchors, f'Broken anchor: {path.relative_to(ROOT)}: {target}'
    return resolved


def main():
    manifest = read_json(FINAL / 'manifest.json')
    guide = manifest['documentationGuide']
    inventory = {'README.md', 'CONTRIBUTING.md', 'docs/presentation.html'} | {
        str(p.relative_to(ROOT)) for p in (ROOT / 'docs').rglob('*.md')}
    assert len(manifest['documents']) == len(set(manifest['documents'])), 'Duplicate document registration'
    assert set(manifest['documents']) == inventory, 'Document inventory changed; register it in the guide and manifest'
    index = ROOT / guide['index']
    indexed = {p for target in document_references(index)
               if (p := local_reference(index, target)) is not None}
    for relative in inventory - {guide['index']}:
        assert ROOT / relative in indexed, f'Document missing from common index: {relative}'
    classified = (set(guide['canonicalByTopic'].values()) | set(guide['supportingDocuments'])
                  | set(guide['historicalDocuments']) | set(guide['compatibilityDocuments'])
                  | {guide['index'], manifest['presentation']['html']})
    assert classified == inventory, 'Classify each document as current, supporting, historical or compatibility'
    assert not set(guide['canonicalByTopic'].values()) & set(guide['historicalDocuments'])
    assert guide['canonicalByTopic']['userFeedback'] == 'docs/final/user-feedback.md'
    for relative in guide['historicalDocuments']:
        assert (ROOT / relative).read_text().startswith('> **과거'), f'Missing historical notice: {relative}'
    for old, current in guide['compatibilityDocuments'].items():
        links = {p for target in document_references(ROOT / old)
                 if (p := local_reference(ROOT / old, target)) is not None}
        assert ROOT / current in links, f'Compatibility path must link to current document: {old}'
    archived_feedback = ROOT / 'docs/archive/user-feedback-2026-10-24.md'
    assert hashlib.sha256(archived_feedback.read_bytes()).hexdigest() == guide['archivedFeedbackSha256']
    presentation = manifest['presentation']
    for key in ('markdown', 'html', 'pdf'):
        assert (ROOT / presentation[key]).is_file(), f'Missing presentation {key}'
        expected = presentation['sha256'][key]
        assert hashlib.sha256((ROOT / presentation[key]).read_bytes()).hexdigest() == expected, (
            f'Presentation {key} changed; synchronize sources/PDF and record checked hashes')
    assert (ROOT / presentation['pdf']).read_bytes().startswith(b'%PDF-')
    slides = HtmlReferences()
    slides.feed((ROOT / presentation['html']).read_text())
    assert slides.slide_count == presentation['pages']
    assert len(re.findall(r'^## \d+\.', (ROOT / presentation['markdown']).read_text(), re.M)) == presentation['pages']
    checked = 0
    for relative in manifest['documents']:
        path = ROOT / relative
        assert path.is_file(), f'Missing document: {relative}'
        content = path.read_text()
        for target in document_references(path):
            if local_reference(path, target) is not None:
                checked += 1
        # Catch private values, not references to environment variable names.
        assert not re.search(r'(?i)(?:sk-[A-Za-z0-9_-]{20,}|AIza[A-Za-z0-9_-]{25,}|gh[pousr]_[A-Za-z0-9]{20,})', content), f'Possible secret: {relative}'

    for relative, expected in manifest['sourceSha256'].items():
        actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
        assert actual == expected, f'Runtime source changed; update document baseline: {relative}'

    assert list(literal_assignment(ROOT / 'backend/models.py', 'INTERESTS')) == manifest['interests']
    assert literal_assignment(ROOT / 'backend/config.py', 'POLICY_VERSION') == manifest['policyVersion']
    assert literal_assignment(ROOT / 'backend/config.py', 'CONSENT_VERSION') == manifest['consentVersion']
    assert literal_assignment(ROOT / 'backend/comparison.py', 'VERSION') == manifest['comparisonVersion']
    classification = read_json(ROOT / 'data/recommendation/classification-v2.json')
    assert classification['version'] == manifest['classificationVersion']
    assert len(classification['entries']) == manifest['products']['classifiedProducts']
    assert sum(len(e['matches']) for e in classification['entries'].values()) == manifest['products']['claimLinks']
    knowledge = read_json(ROOT / 'backend/nutrition-knowledge.json')
    assert knowledge['version'] == manifest['knowledgeVersion']
    assert len(knowledge['cards']) == manifest['products']['knowledgeCards']
    assert len(knowledge['sources']) == manifest['products']['knowledgeSources']

    adult = read_json(ROOT / 'frontend/src/data/adult-intake-references.json')
    groups = {group['id'] for group in adult['groups']}
    assert len(groups) == len(adult['groups'])
    values = sum(len(item['values']) for item in adult['nutrients'].values())
    assert manifest['adultIntakeReferences'] == {
        'version': adult['version'], 'nutrients': len(adult['nutrients']),
        'groups': len(groups), 'values': values, 'sourceSha256': adult['source']['sha256'],
    }
    source = (ROOT / adult['source']['localPath']).resolve()
    assert source.is_relative_to(ROOT) and source.is_file()
    assert hashlib.sha256(source.read_bytes()).hexdigest() == adult['source']['sha256']
    for item in adult['nutrients'].values():
        assert item['kind'] in {'RNI', 'AI'} and set(item['values']) == groups
        assert all(float(value) > 0 for value in item['values'].values())

    with sqlite3.connect(f'file:{ROOT / "data/products/products.sqlite3"}?mode=ro', uri=True) as db:
        assert db.execute('SELECT count(*) FROM products').fetchone()[0] == manifest['products']['collected']
        public = db.execute("SELECT count(*) FROM label_reviews WHERE data_review_status='verified'").fetchone()[0]
        assert public == manifest['products']['public']
        held = [r[0] for r in db.execute("SELECT product_id FROM label_reviews WHERE data_review_status!='verified' ORDER BY product_id")]
        assert held == manifest['products']['heldIds']
        available = db.execute("SELECT count(*) FROM product_thumbnails WHERE status='available'").fetchone()[0]
        assert available == manifest['products']['thumbnails']
        public_images = db.execute("SELECT count(*) FROM product_thumbnails t JOIN label_reviews r ON r.product_id=t.product_id WHERE t.status='available' AND r.data_review_status='verified'").fetchone()[0]
        assert public_images == manifest['products']['publicThumbnails']

    api = read_json(FINAL / 'evidence/acceptance-api.json')
    assert api['passed'] and len(api['trials']) == 3
    for name in manifest['mustIds'] + ['S01']:
        checks = [c for t in api['trials'] for c in t['checks'] if c['id'] == name]
        count = sum(c['passed'] for c in checks)
        assert len(checks) == 3 and count >= 2, name
        assert api['summary'][name] == {'attempts': 3, 'successes': count}, name
    assert api['summary']['M04']['successes'] == 2, 'Update written failure/success report if evidence changes'
    for key in ('policyVersion', 'consentVersion'):
        assert api['health'][key] == manifest[key]
    assert api['health']['aiProvider'] == manifest['provider']
    assert api['health']['aiModel'] == manifest['model']
    browser = read_json(FINAL / 'evidence/acceptance-browser.json')
    assert browser['passed'] and len(browser['trials']) == 3
    assert all(t['M01'] and t['M02'] for t in browser['trials'])
    release = read_json(FINAL / 'evidence/production-release-2026-10-23.json')
    local = read_json(FINAL / 'evidence/local-checks.json')
    assert release['commit'] == local['baselineCommit'] == manifest['baselineCommit']
    assert release['passed'] and all(c['passed'] for c in local['checks'])
    assert len(manifest['team']) == 5 and len(set(manifest['team'])) == 5
    accounts = manifest['confirmedAccount']
    assert accounts['sayknow'] == '이승현'
    assert accounts['jojunsu98'] == '조준수'
    assert set(accounts.values()) == set(manifest['team'])
    unidentified = manifest.get('unidentifiedAccounts', {})
    assert not (set(accounts) & set(unidentified)), 'Unconfirmed accounts must not be assigned to team members'
    for identity in unidentified.values():
        assert identity['identityStatus'] == 'unconfirmed'
        assert identity['teamMembership'] == 'unconfirmed'
        assert identity['countedAsConfirmedTeamAccount'] is False
    contributions = manifest['forkContributions']
    assert len(contributions) == 3
    assert {record['pullRequest'] for record in contributions} == {12, 13, 14}
    contribution_doc = (FINAL / 'team-contributions.md').read_text()
    for record in contributions:
        assert accounts[record['proposerAccount']] == record['person']
        assert record['parentRepository'] == 'sayknow/M2-1'
        assert record['targetBranch'] == 'canary'
        assert record['forkUrl'] == 'https://github.com/' + record['repository']
        assert record['pullRequestUrl'] == f"https://github.com/sayknow/M2-1/pull/{record['pullRequest']}"
        assert record['forkUrl'] in contribution_doc
        assert record['pullRequestUrl'] in contribution_doc
        for commit in record['commits']:
            author = commit['authorAccount']
            assert author in accounts or author in unidentified
            if author in unidentified:
                assert commit['authorIdentityStatus'] == 'unconfirmed'
            assert len(commit['sha']) == 40 and all(c in '0123456789abcdef' for c in commit['sha'])
            assert commit['url'] == 'https://github.com/sayknow/M2-1/commit/' + commit['sha']
            assert commit['url'] in contribution_doc
    assert isinstance(manifest['submissionReady'], bool)
    assert isinstance(manifest['pendingEvidence'], list)
    if manifest['submissionReady']:
        assert not manifest['pendingEvidence'], 'Evidence still pending'
    else:
        assert manifest['pendingEvidence'] or manifest.get('submissionReview', {}).get('remainingActions'), (
            'Document the remaining final review or submission actions')
    confirmation = manifest['teamContributionConfirmation']
    assert set(confirmation['documentContributors']) == {'김재욱', '배창민', '윤준서'}
    assert confirmation['demoVideoCreator'] == manifest['demoVideo']['creator'] == '윤준서'
    reporting = manifest['feedbackReporting']
    assert reporting['individualResponseAttachmentsRequiredByProject'] is False
    assert reporting['minimumActualTargetUsersRequired'] >= 5
    assert reporting['developerQACountedAsActualUsers'] is False

    # Evidence may contain public field names; raw session credentials must not be saved.
    def inspect(value):
        if isinstance(value, dict):
            for key, child in value.items():
                assert key.lower() not in {'token', 'api_key', 'apikey', 'authorization', 'x-session-token'}, 'Credential field in evidence'
                inspect(child)
        elif isinstance(value, list):
            for child in value:
                inspect(child)

    for path in (FINAL / 'evidence').glob('*.json'):
        inspect(read_json(path))
    print(json.dumps({'technicalDocumentationChecksPassed': True,
                      'documents': len(manifest['documents']), 'localLinks': checked,
                      'commonIndexCoversAllDocuments': True,
                      'historicalDocuments': len(guide['historicalDocuments']),
                      'presentationSourcePages': slides.slide_count,
                      'runtimeSourceHashes': len(manifest['sourceSha256']),
                      'submissionReady': manifest['submissionReady'],
                      'pendingEvidence': manifest['pendingEvidence']}, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
