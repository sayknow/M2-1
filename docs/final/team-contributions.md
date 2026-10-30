# 팀원 역할과 기여 기록

[문서 전체 목차](README.md) · [서비스 소개·실행](../../README.md)

**팀 기여 확인: 2026-10-30 · 확인 근거: 프로젝트 담당 사용자의 설명**

팀원은 이승현·조준수·김재욱·배창민·윤준서다. 사용자가 김재욱·배창민·윤준서의 문서 기여와 **윤준서의 시연 영상 제작**을 확인해 주었다. 아래 표는 팀이 확인한 기여 내용이며, GitHub에서 직접 확인한 작성 계정·커밋은 다음 절에서 별도로 연결한다.

## 팀이 확인한 기여

| 팀원 | 기여 분야 | 기여 요약 | 산출물·연결 근거 |
|---|---|---|---|
| 이승현 | 주 개발·통합·운영 | 프런트엔드·백엔드·AI 추천 개발 총괄, 화면/API/DB 연결, CI·통합·배포 관리 | [화면](../../frontend/src/App.tsx) · [서버](../../backend/main.py) · [AI](../../backend/agent.py) · 아래 `sayknow` 이력 |
| 조준수 | 부 개발·사용성 개선 | UX 개선·디버깅, 다크 모드와 제품 카드 검수 배지 제거 | [화면](../../frontend/src/App.tsx) · [스타일](../../frontend/src/styles.css) · [PR #15](https://github.com/sayknow/M2-1/pull/15) · [작성 커밋 d94c09b](https://github.com/sayknow/M2-1/commit/d94c09b0d894dfe11923bf013b868806b998df0f) |
| 김재욱 | 기획·요구사항 문서·포크 제안 | 기획서의 역할 분담 정리, 기능 요구 명세서와 README 작성·정리, 역할 분담 문서 PR 제안 | [기획서](../project-plan.md) · [명세서](../functional-requirements.md) · [README](../../README.md) · [PR #14 제안·canary 병합](https://github.com/sayknow/M2-1/pull/14) |
| 배창민 | 피드백 문서 | 피드백 자료 수집·작성, 질문과 개선 내용 정리 | [사용자 피드백](user-feedback.md) · [PR #13](https://github.com/sayknow/M2-1/pull/13) |
| 윤준서 | 제출·발표 문서·시연 영상 | 제출 문서·발표 자료 작성 및 정리, 시연 영상 v1 제작 | [발표 내용](../presentation.md) · [PDF](../presentation.pdf) · [시연 영상](../../README.md#시연-영상) · [PR #12](https://github.com/sayknow/M2-1/pull/12) |

김재욱·배창민·윤준서의 문서/영상 기여와 아래 계정 연결은 2026-10-30 사용자 확인을 반영했다. 파일 링크는 산출물 위치를, 커밋·포크·PR 링크는 저장소에 남은 작성·제안 이력을 보여 준다. 이승현의 업로드·병합 기록만으로 문서나 영상 제작자까지 동일 인물이라고 판단하지 않는다.

## 세 팀원의 포크·커밋·PR

2026-10-30 GitHub 조회로 포크의 원본이 `sayknow/M2-1`인지, PR의 제출·커밋 작성 계정과 병합 대상을 확인했다. 실명 연결은 같은 날 사용자가 확인했다. 세 PR 모두 `sayknow`가 **canary**에 병합한 기록이며, 아래 이력 자체가 dev·production 반영을 뜻하지는 않는다.

| 팀원·제안 계정 | 실제 포크 저장소 | 대표 변경 커밋·작성자 | PR·반영 내용 | canary 병합일(KST) |
|---|---|---|---|---|
| 윤준서 · `etu9317cw` | [etu9317cw/M2-1](https://github.com/etu9317cw/M2-1) | [c8b9462](https://github.com/sayknow/M2-1/commit/c8b94625d787c7221fcbff4d6d8241497572e530) · [628b141](https://github.com/sayknow/M2-1/commit/628b141263b8042a41c2ceccc3669383d8e66e89), 모두 `etu9317cw` 작성 | [PR #12](https://github.com/sayknow/M2-1/pull/12): README·기획서·명세서 등 제출 문서 재작성, 발표 자료 추가 | 2026-10-28 |
| 배창민 · `daguri2963` | [daguri2963/M2-1](https://github.com/daguri2963/M2-1) | [21865ef](https://github.com/sayknow/M2-1/commit/21865efb6d2af037fdf39eaf59d4bd0c20bbf709), `daguri2963` 작성 | [PR #13](https://github.com/sayknow/M2-1/pull/13): 사용자 피드백 문구·표 구조 수정 | 2026-10-29 |
| 김재욱 · `woogie0403` | [woogie0403/M2-1-final](https://github.com/woogie0403/M2-1-final) | [ff2d348](https://github.com/sayknow/M2-1/commit/ff2d34822bbb2261668d56b9375e028eff7d27fb), **`love4xox` 작성(실명·팀 소속 미확인)** | [PR #14](https://github.com/sayknow/M2-1/pull/14): 김재욱의 포크에서 역할 분담·관련 문서 변경 제안 | 2026-10-29 |

PR #12의 제출 문서·발표 자료 커밋은 윤준서(`etu9317cw`)의 작성 기록이다. 윤준서의 시연 영상 제작도 팀 확인 내용으로 함께 기록한다. 김재욱의 저장소 기여 근거는 **우리 저장소의 포크 `woogie0403/M2-1-final`에서 제출한 PR #14가 2026-10-29 canary에 병합된 기록**이다. PR #14는 **제안자 김재욱 / 커밋 작성 계정 love4xox(실명·팀 소속 미확인) / 병합자 이승현**으로 구분하며, 이 커밋을 김재욱 또는 조준수 명의의 작성 커밋으로 적지 않는다. `love4xox`는 확인된 팀원 계정 목록과 개인별 작성 커밋 집계에서 제외한다.

## 확인된 저장소 이력

확인된 연결은 `sayknow=이승현`, `jojunsu98=조준수`, `etu9317cw=윤준서`, `daguri2963=배창민`, `woogie0403=김재욱`이다. 아래는 실제 저장소 링크이며 변경 작성자와 PR 병합자를 구분한다. 계정 이력만으로 공동 작업의 모든 구현을 한 사람이 작성했다고 단정하지 않는다. 전체 변경과 포크 제안 계정은 [커밋·PR 이력](../commit-history.md)에서 관리한다.

| 이력 | 실제 링크 | 확인 내용 |
|---|---|---|
| 데이터·화면 프로토타입 | [de683ca](https://github.com/sayknow/M2-1/commit/de683ca) | 초기 검수 데이터·프런트 코드 저장 |
| 사진·백엔드 연결 | [fb2cce0](https://github.com/sayknow/M2-1/commit/fb2cce0) | 상품 사진·Gemini 초기 백엔드 |
| 상담 범위 개선 | [b1185bf](https://github.com/sayknow/M2-1/commit/b1185bf) | 일반 영양 설명과 공식 지식 검색 |
| COPA 전환 | [PR #3](https://github.com/sayknow/M2-1/pull/3) | GPT 연결·호환성 검증 통합 |
| 추천 분류 | [PR #4](https://github.com/sayknow/M2-1/pull/4) | 목적 중심 후보 정책 통합 |
| 5분야·AI 비교 | [PR #5](https://github.com/sayknow/M2-1/pull/5) | 관심 분야 정리·비교 해설 |
| 운영 릴리스 | [PR #6](https://github.com/sayknow/M2-1/pull/6) | dev → production 반영 |
| 조준수의 화면 개선 | [d94c09b](https://github.com/sayknow/M2-1/commit/d94c09b0d894dfe11923bf013b868806b998df0f) · [PR #15](https://github.com/sayknow/M2-1/pull/15) | `jojunsu98`가 다크 모드·카드 배지 정리를 작성, `sayknow`가 canary에 병합 |

포크 문서 PR #12~#14의 원래 계정·작성 시각·병합 기록은 [이력 문서](../commit-history.md)에 보존한다. 이번 정리는 기여 링크와 실명 연결을 추가한 것으로 Git의 원래 작성자나 커밋 해시를 변경하지 않는다. 제출 전에는 각 팀원이 위 기여 요약과 대표 산출물 링크를 검토한다.
