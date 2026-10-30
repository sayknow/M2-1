# 프로젝트 진행 기록

[문서 전체 목차](README.md) · [서비스 소개·실행](../../README.md)

2026-10-24 · [제출 목차](README.md)

> 2026-10-29 추가: 전체 커밋과 PR의 최신 정리본은 [커밋·PR 변경 이력](../commit-history.md)에서 관리한다. 아래 표는 10/24에 정리한 진행·의사결정 기록으로 보존하며 전체 이력 표를 중복 작성하지 않는다.

2026-10-29 도식 정리: [시스템 아키텍처](architecture.md), README·기획서·기능 명세서·발표 자료의 통신/함수 호출을 요청과 결과 반환으로 표시했다. 외부 HTTPS와 서버 내부 읽기 전용 조회, Agent의 도구 실행을 구분하고 수집·검수·구축의 작업 순서는 단방향으로 유지했다. 서비스 코드·배포 설정은 변경하지 않았다.

2026-10-29 문서 연결 정리: 이 [문서 목차](README.md)를 공통 입구로 삼아 기준 문서·상세 자료·과거 기록을 구분했다. 중복 피드백은 안내 경로와 과거 보존본으로 정리하고 날짜·계정·발표 제작 상태의 차이를 대조했다. 발표 내용·HTML·PDF를 함께 맞추고 문서 목록·링크·내부 연결·출력 파일 검사를 확장했다. 이번 로컬 문서 변경은 아직 커밋 이력에 포함하지 않으며 사용자 증빙의 확인 상태를 임의로 완료 처리하지 않는다.

확인 가능한 자료 날짜와 Git 이력으로 정리했다. 계정 `sayknow`는 이승현이다. 아래 변경은 저장소 이력이며 다른 팀원의 개인 기여는 [별도 증빙 표](team-contributions.md)로 확인한다.

## 실제 진행과 근거

| 날짜(KST) | 작업/결정 | 결과·이력 |
|---|---|---|
| 10-19~20 | 다이소 공식 상품·라벨 수집과 원문 대조 | 88개 수집·87개 공개, [DB 기록](../product-database.md)·[검수](../product-label-review.md) |
| 10-20 | 검수 데이터·모바일 화면 프로토타입 저장 | [de683ca](https://github.com/sayknow/M2-1/commit/de683ca) |
| 10-21 | 공식 사진·서버·초기 Gemini 추천/대화 연결 | [fb2cce0](https://github.com/sayknow/M2-1/commit/fb2cce0) |
| 10-21 | 외부 배포 구성과 접속 확인 | [0496668](https://github.com/sayknow/M2-1/commit/0496668) |
| 10-21 | 표시 읽기 첫 질문 검색 오류 개선 | [c8fa914](https://github.com/sayknow/M2-1/commit/c8fa914)·[686d8a2](https://github.com/sayknow/M2-1/commit/686d8a2) |
| 10-21 | 일반 영양 질문·공식 지식 검색 확장 | [b1185bf](https://github.com/sayknow/M2-1/commit/b1185bf) |
| 10-21 | 초보자에게 어색한 제목 문구 개선 | [795a23c](https://github.com/sayknow/M2-1/commit/795a23c) |
| 10-22 | 서비스 주소 vitastep-guide 적용 | [1e44b76](https://github.com/sayknow/M2-1/commit/1e44b76) |
| 10-23 | canary/dev/production 관리·CI 도입 | [0eb636a](https://github.com/sayknow/M2-1/commit/0eb636a), [PR #1](https://github.com/sayknow/M2-1/pull/1)·[PR #2](https://github.com/sayknow/M2-1/pull/2) |
| 10-23 | 코디세이 GPT 연결·옵션 호환성·로컬 검사 | [c450731](https://github.com/sayknow/M2-1/commit/c450731)·[6f59312](https://github.com/sayknow/M2-1/commit/6f59312)·[8b77b2d](https://github.com/sayknow/M2-1/commit/8b77b2d), [PR #3](https://github.com/sayknow/M2-1/pull/3) |
| 10-23 | 목적 분류·대표 포장 후보·활력 추천 개선 | [b75f847](https://github.com/sayknow/M2-1/commit/b75f847), [PR #4](https://github.com/sayknow/M2-1/pull/4) |
| 10-23 | 다섯 관심 분야와 AI 비교 해설 | [7f392c2](https://github.com/sayknow/M2-1/commit/7f392c2), [PR #5](https://github.com/sayknow/M2-1/pull/5) |
| 10-23 17:44 | dev → production 병합 | [PR #6](https://github.com/sayknow/M2-1/pull/6)·[0bc17dc](https://github.com/sayknow/M2-1/commit/0bc17dc) |
| 10-23 | 운영 COPA 환경변수 적용·실제 호출 확인 | [릴리스 증빙](evidence/production-release-2026-10-23.json) |
| 10-24 | 최종 코드/문서 대조·3회 반복 QA·문서 작성 | [검증](test-results.md)·[증빙](evidence/acceptance-api.json) |

전체 프로젝트 시작일·모든 회의 날짜를 복원한 표는 아니다. 자료 관찰일은 Git 커밋일과 구분한다. 최종 문서 변경은 [canary 커밋 기록](https://github.com/sayknow/M2-1/commits/canary/)에서 확인한다. 운영 기능 코드의 기준 커밋과 문서 정리 커밋은 구분한다.

## 주요 의사결정

| 주제 | 선택과 이유 | 현재 한계 |
|---|---|---|
| 화면 후 정책 확정 | 실제 설문 입력·목적에 맞춰 정책을 연결 | 모든 일반 건강 관심을 지원하지 않음 |
| DB | 작은 검수 DB를 읽기 전용 SQLite로 배포 | 온라인 편집/사용자 기록 저장 기능 없음 |
| 추천 | LLM 임의 선택 대신 표시 기반 규칙 | 분류된 후보 범위가 작고 원문 갱신 시 재검토 필요 |
| AI | 제품 질문과 일반 영양 질문을 구분한 Agent+RAG | 검색·자연어 검증의 의미적 한계 |
| COPA | 제공된 코디세이 키·실제 GPT 도구 호환성 검증 | 일부 형식 강제 옵션 미지원, 서버 검증 필요 |
| 브랜치 | main 보존, canary → dev → production | 별도 시험 서버 없이 로컬 검증에 의존 |
| 비교 | 전체 표시 앞에 AI 차이 해설 | AI 오류 시 표만 이용, 캐시 결과와 새 생성 구분 |
| 범위 | 핵심 Must8개 유지, 외부 대안·장기 메모리 제외 | 초기 구상 일부 미구현을 최종 명세에 명시 |

## 제출 준비 상태

운영 기능·기술 검사 기록과 Markdown 문서를 정리했다. [발표 PDF](../presentation.pdf)는 12쪽으로 존재하며 문서 기준과 맞춰 관리한다. 실제 사용자 5명 원본과 전원 개인 기여 확인은 남아 있다. 현재 상태와 읽는 순서는 [문서 전체 목차](README.md)를 따른다. 변경을 운영 브랜치에 반영할 때 기존 CI와 승인 흐름을 따른다.

2026-10-30 시연 영상 추가: 사용자가 제공한 v1 MP4(약 2분 52초·8.55MB)를 GitHub 영상 첨부로 업로드하고 [README 상단](../../README.md#시연-영상)에 재생 주소를 연결했다. 영상 원본을 Git 이력에 중복 저장하지 않는다. 파일의 시연 내용은 기존 날짜별 기술 검증이나 실제 사용자 원본을 대신하지 않는다.
