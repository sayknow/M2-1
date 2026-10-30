# 문서 안내와 최종 제출 목차

**문서 정리일: 2026-10-29 (KST)** · [서비스](https://vitastep-guide.onrender.com/) · [저장소](https://github.com/sayknow/M2-1) · [서비스 소개·실행 방법](../../README.md)

**영상 먼저 보기:** [시연 영상 v1 · 2분 52초](../../README.md#시연-영상) · 2026-10-30 첨부. 원본 MP4를 GitHub 첨부로 업로드했으며 README 상단에서 재생할 수 있다. 영상은 서면 문서와 날짜별 기능 검사에 보조 자료로 연결한다.

이 페이지가 저장소 문서의 공통 입구다. **처음에는 아래 기준 문서만 읽고, 추가 확인이 필요할 때 상세 자료와 날짜가 고정된 기록을 펼친다.** 기존 파일 경로는 유지하고 같은 주제의 기준 문서를 하나로 정했다.

문서 정리일, 코드 커밋일, 상품 관찰일, 검사 실행일은 서로 다르다. API 반복 검사는 `0bc17dc` 기준의 2026-10-24 자료이며, 후속 화면 검사와 다크 모드는 별도 기록이다. 현재 정리 대상은 canary `ab3e8bf` 이후의 로컬 문서 변경이다. 브랜치별 반영 상태는 [커밋·PR 이력](../commit-history.md), 실행 코드 해시는 [기준 정보](manifest.json)를 확인한다. 이번 문서 정리가 새 운영 배포나 실사용자 재시험을 의미하지 않는다.

## 1. 처음 읽는 순서와 주제별 기준 문서

| 순서 | 알고 싶은 내용 | 기준 문서 | 여기서 관리하는 내용 |
|---|---|---|---|
| 1 | 서비스가 무엇이고 어떻게 실행하나 | [루트 README](../../README.md) | 개요·역할 요약·기술 스택·실행 방법·결과 요약 |
| 2 | 어떤 문제를 왜 해결하나 | [기획서](../project-plan.md) | 문제·타깃·범위·선정 이유·일정 |
| 3 | 무슨 기능을 확인해야 하나 | [기능 요구 명세서](../functional-requirements.md) | Must 8개·Should S01·비기능 요구·API 계약·재현 방법 |
| 4 | 화면·서버·DB·AI가 어떻게 연결되나 | [시스템 아키텍처](architecture.md) | 요청/응답·구성 요소·데이터/배포 경계 |
| 5 | Agent와 RAG가 어떻게 동작하나 | [AI 설계](ai-design.md) | 도구·루프·검색·출처 검증·개인정보 경계·한계 |
| 6 | 어떤 규칙으로 추천하나 | [추천 정책](../recommendation-policy-v2.md) | 후보 제외·목적 연결·순위·포장 변형·단위 처리 |
| 7 | 데이터와 함량 비율의 근거는 무엇인가 | [상품 DB](../product-database.md) · [성인 섭취기준](../adult-intake-reference.md) | 검수 뷰·원본 추적 / 공식 RNI·AI와 계산 규칙 |
| 8 | 무엇을 시험했고 어디까지 확인했나 | [검증 결과](test-results.md) | 날짜·코드·검사 범위별 결과와 실행 원본 |
| 9 | 어떤 불편을 어떻게 개선했나 | [사용자 피드백](user-feedback.md) | F01~F05·팀 제공 날짜·변경 근거·증빙 한계 |
| 10 | 누가 맡고 실제로 무엇을 기여했나 | [팀원 역할·기여](team-contributions.md) | 역할 배정과 확인한 개인 기여 링크 |
| 11 | 어떤 결정을 거쳐 바뀌었나 | [진행 기록](progress.md) · [커밋·PR 이력](../commit-history.md) | 의사결정 / 커밋·PR·작성자·병합자·반영 브랜치 |
| 12 | 어떻게 참여·운영·복구하나 | [참여 방법](../../CONTRIBUTING.md) · [보안·운영](security-and-operations.md) | 브랜치·검사·병합 / 동의·키·보존·장애·복구 |
| 13 | 발표용 요약을 읽고 싶다 | [발표 PDF](../presentation.pdf) · [내용 원본](../presentation.md) | 문제 → 해결 → AI 기술과 근거 → 구현 → 피드백·개선 |

동일한 주제가 여러 문서에 나오면 위 표의 기준 문서가 상세 설명을 관리한다. 나머지는 필요한 요약과 링크를 둔다. 검사 기록은 그 검사 당시 사실이므로 새 기능 설명으로 덮어쓰지 않는다. 자료가 충돌하면 코드·원본·실행 기록을 대조하고 미확인 내용을 임의로 확정하지 않는다.

## 2. 접속과 검토 범위

평가용 계정은 필요 없다. 제품 찾기·상세·표시 비교는 바로 이용하고 추천·대화·AI 비교 해설은 성인 이용·정보 처리·외부 AI 전송 안내에 동의한 뒤 이용한다. 서버가 대기 중이면 화면의 준비 안내를 기다린다. 팀은 결과 안내를 받을 때까지 서비스를 유지한다.

수집 88개·공개 87개·보류 1개, 공식 썸네일 88개 중 공개 제품 87개에 연결되어 있다. 상품 주 관찰일은 10/19, 전수 검수는 10/19~20, 사진 확인은 10/21이다. AI는 COPA `gpt-5.4`, 필수 기술은 **AI Agent + RAG**다. 문서 정리일을 상품 최신 확인일로 바꾸지 않는다.

| 평가 요건 | 연결할 근거 | 준비 상태와 한계 |
|---|---|---|
| G1 문서 | 위 기준 문서·[발표 PDF](../presentation.pdf) | Markdown·HTML·12쪽 PDF를 연결함. PDF에는 미확인 증빙 상태도 표시 |
| G2 외부 접속 | [운영 URL](https://vitastep-guide.onrender.com/)·[배포 기록](evidence/production-release-2026-10-23.json) | 보존된 배포 검사이며 이번 정리에서 새 운영 검사를 수행하지 않음 |
| G3 AI 기술 2개 | [AI 설계](ai-design.md)·M03/M04 실행 기록 | Agent + 질의별 RAG. 임베딩·멀티모달·장기 메모리는 사용하지 않음 |
| G4 Must | [검증 결과](test-results.md)·[API 원본](evidence/acceptance-api.json) | 8개 기능의 대표 API 사례 3회 중 2회 이상. M04 2/3, 나머지 3/3. 화면 반복은 M01·M02 범위 |
| G5 실사용자 5명 | [피드백](user-feedback.md) | 5개 개선 항목은 정리됨. 실제 5명 참여·익명화 원본은 보완 필요 |
| G6 전원 기여 | [기여 문서](team-contributions.md)·[커밋 이력](../commit-history.md) | 확인된 계정·실제 링크를 기록. 전원 본인 작성 요약·개별 수행 증빙은 보완 필요 |
| G7 AI 윤리·개인정보 | [보안·운영](security-and-operations.md) | AI 표시·동의·입력 최소화·철회 구현. 피드백 원본은 개인정보 제거 후 연결 |

이는 팀의 준비 점검이며 최종 평가 판정이 아니다. **5개 개선 항목을 5명 참여 증거로 대신하지 않는다.** 개발자 QA·실제 사용자 의견·배정 역할·실제 기여를 구분한다.

## 3. 더 확인할 때: 상세 자료와 증빙

<details>
<summary>데이터·화면·발표 상세 자료</summary>

| 자료 | 확인하는 내용 |
|---|---|
| [전수 표시 검수 보고](../product-label-review.md) | 자체 검수 기준·보류 이유·원문 대조 범위 |
| [제품별 검수 결과](../product-collection-report.md) | 88개 품번별 완료/보류 상태 |
| [썸네일 수집·연결](../product-thumbnails.md) | 공식 사진·출처·확인일·파일 검증 |
| [AI 비교 해설 상세](../comparison-explanation.md) | 표시표와 AI 해설 구분·사실 ID 검증·캐시 |
| [발표 관리 안내](presentation-outline.md) | PDF·내용 원본·HTML의 역할과 동기화 방법 |
| [발표 HTML](../presentation.html) | PDF를 출력하는 편집 원본 |
| [실행 코드·자료 기준](manifest.json) | 정책/분류 버전·파일 해시·미완료 증빙 |

</details>

<details>
<summary>날짜가 고정된 검사 원본·화면·설정</summary>

검사 결과는 [검증 결과](test-results.md)의 설명과 함께 읽는다. 아래 폴더의 파일은 작성 당시 증빙이며 현재 운영 상태나 새 AI 호출 성공을 보장하지 않는다.

- [최종 API·브라우저·성분 기준 검사 원본](evidence/)
- [화면 캡처](../screenshots/)
- [상품 원본·DB·라벨 검수 원장](../../data/products/)
- [GitHub 브랜치 규칙 원본](../branch-rules/)

### 개발 단계별 실행 결과 JSON

- [backend-live-check.json](../backend-live-check.json)
- [chat-label-reading-api-check.json](../chat-label-reading-api-check.json)
- [comparison-live-check.json](../comparison-live-check.json)
- [copa-compatibility-check.json](../copa-compatibility-check.json)
- [copa-local-integration-check.json](../copa-local-integration-check.json)
- [counselor-backend-check.json](../counselor-backend-check.json)
- [counselor-deployment-check.json](../counselor-deployment-check.json)
- [counselor-local-check.json](../counselor-local-check.json)
- [deployment-api-check.json](../deployment-api-check.json)
- [gemini-live-check.json](../gemini-live-check.json)
- [recommendation-v2-live-check.json](../recommendation-v2-live-check.json)
- [vitastep-migration-check.json](../vitastep-migration-check.json)

</details>

## 4. 과거 설계·검사 기록

<details>
<summary>과거 기록 목록 열기: 초기 기획·Gemini·전환·검사</summary>

당시의 날짜·정책·시험 결과를 보존한다. **현재 사용법과 기능 계약은 1절 기준 문서를 먼저 읽는다.** 외부에서 이미 연결한 파일 경로는 유지하고 각 문서 상단에 과거 기록임을 표시했다.

| 기록 | 대상 시점 | 읽는 목적 |
|---|---|---|
| [ai-counselor.md](../ai-counselor.md) | 2026-10-21 | 일반 영양 상담 확장 당시 설계·검사 |
| [backend-api.md](../backend-api.md) | 2026-10-21~23 | Gemini 초기 연결과 COPA 전환 중 API 설명 |
| [backend-test-results.md](../backend-test-results.md) | 2026-10-21 | 초기 Gemini 백엔드 검사 |
| [catalog-research.md](../catalog-research.md) | 2026-10-19 | 상품 목록 탐색 표본 |
| [chat-label-reading-fix.md](../chat-label-reading-fix.md) | 2026-10-21 | 첫 질문 오류 수정·당시 Gemini 재검증 |
| [codyssey-gpt.md](../codyssey-gpt.md) | 2026-10-23 | COPA 전환 당시 설정·호환성 검사 |
| [copa-local-integration.md](../copa-local-integration.md) | 2026-10-23 | dev 병합 전 COPA 로컬 통합 검사 |
| [data-sources.md](../data-sources.md) | 2026-10-19~20 | 초기 파일럿 출처와 전수 검수 전환 |
| [data-validation.md](../data-validation.md) | 2026-10-19~20 | 파일럿 데이터 검사와 전수 검수 전환 |
| [deployment.md](../deployment.md) | 2026-10-21~23 | 최초 배포·주소·브랜치 전환 |
| [frontend-test-results.md](../frontend-test-results.md) | 2026-10-20~21 | 초기 프런트·서버 연결 검사 |
| [recommendation-classification-v2.md](../recommendation-classification-v2.md) | 2026-10-23 | 구현 전 분류표·예상 사례 |
| [recommendation-policy.md](../recommendation-policy.md) | 2026-10-21 | 교체된 초기 추천 정책 |
| [recommendation-v2-test-results.md](../recommendation-v2-test-results.md) | 2026-10-23 | 분야 축소 전후 로컬 검사 |
| [ui-design.md](../ui-design.md) | 2026-10-21 | 초기 화면·연결 설계 |
| [version-control.md](../version-control.md) | 2026-10-20 | main 단일 브랜치 시절 기록 |
| [project-plan-initial.md](../archive/project-plan-initial.md) | 초기 기획 | 초기 아이디어·범위 |
| [user-feedback-2026-10-24.md](../archive/user-feedback-2026-10-24.md) | 2026-10-24 | 이전 피드백 작성본·미확인 응답 주장 |

</details>

이전 [피드백 경로](../user-feedback.md)는 현재 기준 문서로 안내한다. 과거 피드백 원문은 목록의 보존본에서 확인할 수 있다. README 전체를 버전별 복제하지 않으며 과거 README는 Git 이력으로 확인한다.

## 5. 문서를 바꿀 때

1. 주제별 기준 문서를 먼저 고치고 다른 문서의 요약·링크에 영향이 있는지 확인한다.
2. 작성/정리일과 코드 기준·관찰일·실행일을 따로 적는다. 로컬 확인과 운영 확인을 구분한다.
3. 피드백은 실제 응답과 팀의 요약/제안을, 기여는 역할 배정과 실제 작성 링크를 구분한다.
4. 발표 내용을 고치면 Markdown → HTML → PDF 순서로 반영하고 화면 잘림·페이지 수·연결을 확인한다. 발표 요약이 상세 문서의 기준을 덮어쓰지 않는다.
5. 새 문서를 만들면 이 목차와 [문서 목록](manifest.json)에 등록하고 아래 검사를 실행한다. 파일 이동 시 기존 링크를 안내 문서로 유지한다.

```sh
python3 scripts/validate_final_docs.py
git diff --check
```

문서 검사는 목록 누락·상대 링크·문서 내부 연결·HTML 자산·실행 코드 해시를 확인한다. 이 검사는 실제 사용자 참여나 모든 자연어 서술의 진실성을 판정하지 않는다.

## 6. 제출 전 남은 확인

실제 타깃 최소 5명의 참여·날짜·질문·응답과 각 팀원의 본인 작성 기여 요약·대표 링크를 확인해야 한다. 현재 상태는 [manifest](manifest.json)의 `submissionReady: false`에 반영한다. 익명화한 증빙을 연결한 뒤 canary → dev → production 절차로 반영하고 플랫폼에 저장소를 연결한다. 선택 제출물인 시연 영상은 2026-10-30에 README 상단으로 연결했다.
