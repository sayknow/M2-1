# 팀원 역할과 실제 기여 증빙

[문서 전체 목차](README.md) · [서비스 소개·실행](../../README.md)

2026-10-24 · [제출 목차](README.md)

팀원은 **이승현·조준수·김재욱·배창민·윤준서**다. 팀 협의에 따라 이승현은 주 개발, 조준수는 부 개발(UX 개선 및 최종 사용성 및 디버그), 김재욱은 문서작성(기획서(역할분담), 기능요구서, README), 배창민은 문서작성(피드백 자료 수집 및 작성), 윤준서는 문서작성(발표 자료(pdf))으로 역할을 배정했다. `sayknow`는 이승현의 GitHub 계정임을 확인했다.

## 역할 배정

| 팀원 | 배정 역할 | 상세 책임·협업 | 담당 산출물 위치 |
|---|---|---|---|
| 이승현 | 주 개발 | 프런트·백엔드·AI 추천 개발 총괄, 화면/API/DB 연결, 추천/Agent 핵심 구현, 통합 설계, CI·production 승격·배포 관리 | [화면](../../frontend/src/App.tsx) · [서버](../../backend/main.py) · [AI](../../backend/agent.py) |
| 조준수 | 부 개발 | UX 개선 및 최종 사용성 및 디버그, 사용자 경험 개선, 화면 사용성 보완, 디버깅 및 버그 수정 | [화면](../../frontend/src/App.tsx) · [스타일](../../frontend/src/styles.css) |
| 김재욱 | 문서작성 | 기획서(역할분담) 작성, 기능요구서 작성 및 관리, 저장소 README 작성 및 프로젝트 가이드 정리 | [기획서](../project-plan.md) · [명세서](../functional-requirements.md) · [README](../../README.md) |
| 배창민 | 문서작성 | 피드백 자료 수집 및 작성, 실사용자 테스트 시나리오/질문지 운영, 사용자 응답 취합 및 피드백 개선 기록 정리 | [피드백](user-feedback.md) |
| 윤준서 | 문서작성 | 발표 자료(pdf) 기획 및 슬라이드 작성, 프로젝트 발표 내용 정리 및 최종 결과물 발표 자료 제작 | [발표 내용](../presentation.md) · [PDF](../presentation.pdf) |

위 산출물은 **담당 범위에 배정한 위치**다. 파일 링크만으로 해당 개인이 실제 작성했다는 증거로 사용하지 않는다. 개발 두 명의 참여는 팀이 확인했지만 세부 작업량·개인별 작성 이력은 별도 확인 대상이다. 나머지 세 명의 세부 역할은 이번 문서 정리 과정의 배정이다.

## 확인된 저장소 이력

확인된 연결은 `sayknow=이승현`, `jojunsu98=조준수`다. 아래는 실제 저장소 링크이며 변경 작성자와 PR 병합자를 구분한다. 계정 이력만으로 공동 작업의 모든 구현을 한 사람이 작성했다고 단정하지 않는다. 전체 변경과 포크 제안 계정은 [커밋·PR 이력](../commit-history.md)에서 관리한다.

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

포크 문서 PR #12~#14의 제안·커밋 계정은 이력 문서에 보존했다. 나머지 세 팀원의 실명에 임의로 연결하지 않는다. 각자 본인이 작성한 기여 요약과 대표 링크는 추가 확인 대상이다. 위 역할 표의 담당 산출물 링크만으로 실제 작성 증빙을 대신하지 않는다.

