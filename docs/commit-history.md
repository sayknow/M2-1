# 커밋·PR 변경 이력

[문서 전체 목차](final/README.md) · [서비스 소개·실행](../README.md)

**기록 기준일: 2026-10-29 · 시간대: 한국 시간(KST, UTC+09:00)**

이 문서는 실제 Git 커밋과 GitHub PR을 연결해 개발 흐름을 한곳에서 읽도록 정리한 이력 대장이다. 작업의 시작일·회의일·상품 관찰일을 커밋 날짜로 대신하지 않는다.

## 1. 기록 범위와 현재 브랜치

- 카나리 기준 커밋: [`ab3e8bf`](https://github.com/sayknow/M2-1/commit/ab3e8bfd175ebe0e3c2669d8cd65755164157d5a). 이 커밋까지 네 브랜치에서 확인한 **전체 커밋 43개 = 변경 커밋 26개 + 병합 커밋 17개**, 병합된 PR 15개를 정리했다.
- PR 병합 15개와 데브 이력을 카나리에 반영한 동기화 병합 2개를 구분한다. 병합 커밋을 별도의 기능 개발 1건으로 중복 계산하지 않는다.
- 아래 SHA는 GitHub에서 확인한 원격 브랜치의 기준값이다. 이 문서 작성 자체와 이후 커밋은 아직 집계하지 않은 고정 시점 기록이다.

| 브랜치 | 기준 커밋 | 기록 시점의 역할·반영 상태 |
|---|---|---|
| `main` | [`1e44b76`](https://github.com/sayknow/M2-1/commit/1e44b762b6b71e8ba0b53fbd18698c3efe20cf68) | 10/22 주소 변경까지의 초기 프로토타입 보존 |
| `production` | [`b9ba2d3`](https://github.com/sayknow/M2-1/commit/b9ba2d3434d51e505bf13c6f1de2fa2e9d213f7d) | PR #11까지 반영한 운영 배포 기준 브랜치 |
| `dev` | [`3d8d359`](https://github.com/sayknow/M2-1/commit/3d8d359b7d8a302076036d074b903683a608b037) | PR #10까지 통합한 상태 |
| `canary` | [`ab3e8bf`](https://github.com/sayknow/M2-1/commit/ab3e8bfd175ebe0e3c2669d8cd65755164157d5a) | PR #12~#15와 PR #15 이후 문서 해시 갱신까지 반영 |

**카나리에만 추가된 주요 내용:** 제출 문서·발표 자료, 피드백·역할 분담 문서 수정, 다크 모드·카드 배지 제거, 문서 해시 갱신. 데브·프로덕션으로의 추가 승격은 이 기록 시점에 수행되지 않았다.
브랜치의 커밋과 실제 Render 실행 버전은 별도로 확인한다. 이 문서는 브랜치 이력이며 현재 운영 서버의 실시간 배포 상태를 보증하는 기록이 아니다.

## 2. 단계별 주요 변경

| 단계 | 시기(KST) | 변경 내용과 목적 | 대표 커밋·PR |
|---|---|---|
| 초기 자료·화면 | 10/20 | 상품 표시·성분 자료를 검수 데이터로 저장하고 모바일 프로토타입 구성 | [`de683ca`](https://github.com/sayknow/M2-1/commit/de683ca718519e8b486cfc4e5528d35ad8ce8d96) |
| 서버·외부 배포 | 10/21 | 사진·상품 조회·초기 Gemini 연결 후 외부 접근 검증 | [`fb2cce0`](https://github.com/sayknow/M2-1/commit/fb2cce091f495581ffdb60b7c43117f7a9168f35) · [`0496668`](https://github.com/sayknow/M2-1/commit/0496668c78b701e09e672f86d6eb41ee299ab68c) |
| 상담 편의 개선 | 10/21 | 시작 질문의 근거 없음 오류 수정, 일반 영양 질문 확대, 제목 개선 | [`c8fa914`](https://github.com/sayknow/M2-1/commit/c8fa914815cf883d47d22619c5b691a55c7bd0d5) · [`b1185bf`](https://github.com/sayknow/M2-1/commit/b1185bf8274f855f9616aee930d6c59b3f2f60a6) · [`795a23c`](https://github.com/sayknow/M2-1/commit/795a23c94bdb69a2321154dcc5a6501a6d533b2c) |
| 주소 정리 | 10/22 | 서비스 주소를 vitastep-guide로 변경하고 연결 확인 | [`1e44b76`](https://github.com/sayknow/M2-1/commit/1e44b762b6b71e8ba0b53fbd18698c3efe20cf68) |
| 브랜치·검사 도입 | 10/23 | canary → dev → production 승격, 소유자 관리·CI 체계 구성 | [`0eb636a`](https://github.com/sayknow/M2-1/commit/0eb636a898f31c831cbd966f7c1229a3751325db) · [PR #1](https://github.com/sayknow/M2-1/pull/1) · [PR #2](https://github.com/sayknow/M2-1/pull/2) |
| GPT 전환 | 10/23 | COPA GPT 연결, 도구 호출·미지원 옵션 검증 후 데브 통합 | [`c450731`](https://github.com/sayknow/M2-1/commit/c450731ce7a31be267c2347b7cad0b3800e0d5c0) · [`6f59312`](https://github.com/sayknow/M2-1/commit/6f593123c912c5a60c381b1ee7021d32112b1766) · [`8b77b2d`](https://github.com/sayknow/M2-1/commit/8b77b2d1dd3ec193293e3f3007360846288b8a04) · [PR #3](https://github.com/sayknow/M2-1/pull/3) |
| 추천·비교 개선 | 10/23 | 목적 기반 후보, 포장 변형 묶기, 다섯 관심 분야, AI 비교 해설을 운영 브랜치에 반영 | [`b75f847`](https://github.com/sayknow/M2-1/commit/b75f84792507f32401898b2f47ac189aeb71a69a) · [`7f392c2`](https://github.com/sayknow/M2-1/commit/7f392c25eeff9c4d3a4b2b65d3b8464a4a271fef) · [PR #4](https://github.com/sayknow/M2-1/pull/4) · [PR #5](https://github.com/sayknow/M2-1/pull/5) · [PR #6](https://github.com/sayknow/M2-1/pull/6) |
| 제출 문서 정리 | 10/24 | 명세·설계·검증·기여·피드백 문서를 정리해 운영 브랜치에 반영 | [`e40d644`](https://github.com/sayknow/M2-1/commit/e40d6441e650d8c37e8acb3dbe56845029f5b9c8) · [PR #7](https://github.com/sayknow/M2-1/pull/7) · [PR #8](https://github.com/sayknow/M2-1/pull/8) |
| 설명·설문 개선 | 10/24 | 제품별 시작 질문, 성분 함량·성인 기준 대비 비율, 쉬운 설명과 접힌 근거, 설문 선택지 정리 | [`b6ba219`](https://github.com/sayknow/M2-1/commit/b6ba219a4c1ff33a75a34103e6f4a3b713a5aad0) · [`6ae740b`](https://github.com/sayknow/M2-1/commit/6ae740b047bb7ffa54f70fdbb7062e9a24f43333) · [PR #9](https://github.com/sayknow/M2-1/pull/9) · [PR #10](https://github.com/sayknow/M2-1/pull/10) · [PR #11](https://github.com/sayknow/M2-1/pull/11) |
| 포크 문서 기여 | 작성 10/24~28 · 병합 10/28~29 | 제출 문서·발표 자료 추가, 피드백·역할 문서 조정. 카나리에만 반영 | [PR #12](https://github.com/sayknow/M2-1/pull/12) · [PR #13](https://github.com/sayknow/M2-1/pull/13) · [PR #14](https://github.com/sayknow/M2-1/pull/14) |
| 다크 모드 | 10/29 | 다크 모드·테마 유지·제품 카드 배지 정리 후 문서 해시 갱신. 카나리에만 반영 | [`d94c09b`](https://github.com/sayknow/M2-1/commit/d94c09b0d894dfe11923bf013b868806b998df0f) · [PR #15](https://github.com/sayknow/M2-1/pull/15) · [`ab3e8bf`](https://github.com/sayknow/M2-1/commit/ab3e8bfd175ebe0e3c2669d8cd65755164157d5a) |

초기 자료의 상세 수집·검수 과정은 [상품 DB 기록](product-database.md)과 [표시 검수 기록](product-label-review.md), 기술 검증은 [검증 결과](final/test-results.md)를 참조한다.

## 3. 전체 PR 병합 대장

날짜는 **GitHub의 실제 병합 시각**이다. PR 작성자는 제안 계정이며 모든 변경 파일의 단독 작성자를 뜻하지 않는다.

| PR | 제안 계정 | 병합 시각(KST) | 대상 | 변경 내용 | 병합 커밋 |
|---|---|---|---|---|
| [PR #1](https://github.com/sayknow/M2-1/pull/1) | `sayknow` | 10/23 09:39:53 | `dev` | 브랜치 관리·CI 도입 | [`aa78a5a`](https://github.com/sayknow/M2-1/commit/aa78a5ad56c3e9f10373f9437c21b5663b896c79) |
| [PR #2](https://github.com/sayknow/M2-1/pull/2) | `sayknow` | 10/23 09:41:27 | `production` | 브랜치 관리 체계를 프로덕션에 반영 | [`e885bf6`](https://github.com/sayknow/M2-1/commit/e885bf6940093f3ab4b5bef047fe7445cb563059) |
| [PR #3](https://github.com/sayknow/M2-1/pull/3) | `sayknow` | 10/23 12:58:26 | `dev` | COPA GPT 연결·호환성 검증 | [`d458643`](https://github.com/sayknow/M2-1/commit/d4586434f9eeb3b9254a628e54cfa5ff6aac0c53) |
| [PR #4](https://github.com/sayknow/M2-1/pull/4) | `sayknow` | 10/23 15:31:40 | `dev` | 목적 중심 추천 정책 개선 | [`9cb0060`](https://github.com/sayknow/M2-1/commit/9cb00601bef8f95b792bc22551bec9471ea76026) |
| [PR #5](https://github.com/sayknow/M2-1/pull/5) | `sayknow` | 10/23 17:33:37 | `dev` | 다섯 관심 분야·AI 비교 해설 | [`11ce98e`](https://github.com/sayknow/M2-1/commit/11ce98e40a7edd2ed085921eb9db7db72f09a912) |
| [PR #6](https://github.com/sayknow/M2-1/pull/6) | `sayknow` | 10/23 17:44:21 | `production` | GPT 추천·비교를 프로덕션에 반영 | [`0bc17dc`](https://github.com/sayknow/M2-1/commit/0bc17dca34f3ec6479549248798e76bfcb962064) |
| [PR #7](https://github.com/sayknow/M2-1/pull/7) | `sayknow` | 10/24 13:41:00 | `dev` | 최종 제출 문서·피드백 기록 정리 | [`e3fcab0`](https://github.com/sayknow/M2-1/commit/e3fcab0e3db5ae36c5ee8c796650a78da81d4971) |
| [PR #8](https://github.com/sayknow/M2-1/pull/8) | `sayknow` | 10/24 13:42:01 | `production` | 제출 문서를 프로덕션에 반영 | [`4eedc4e`](https://github.com/sayknow/M2-1/commit/4eedc4e329028f560857b241d5290d1fdd07e88b) |
| [PR #9](https://github.com/sayknow/M2-1/pull/9) | `sayknow` | 10/24 15:41:04 | `dev` | 제품 AI 질문·성분 요약·성인 기준 비율 | [`01ca19d`](https://github.com/sayknow/M2-1/commit/01ca19d19b3f06d8c3e3b8bf5ab58738382d2847) |
| [PR #10](https://github.com/sayknow/M2-1/pull/10) | `sayknow` | 10/24 15:57:20 | `dev` | 설문 3·4번 선택지·안내 정리 | [`3d8d359`](https://github.com/sayknow/M2-1/commit/3d8d359b7d8a302076036d074b903683a608b037) |
| [PR #11](https://github.com/sayknow/M2-1/pull/11) | `sayknow` | 10/24 16:12:43 | `production` | 성분 설명·설문 개선을 프로덕션에 반영 | [`b9ba2d3`](https://github.com/sayknow/M2-1/commit/b9ba2d3434d51e505bf13c6f1de2fa2e9d213f7d) |
| [PR #12](https://github.com/sayknow/M2-1/pull/12) | `etu9317cw` | 10/28 19:07:27 | `canary` | 제출 문서 재작성·발표 자료 추가 | [`bb921e6`](https://github.com/sayknow/M2-1/commit/bb921e6d451aa6ddc70e1cb92cec724ac8482186) |
| [PR #13](https://github.com/sayknow/M2-1/pull/13) | `daguri2963` | 10/29 11:33:59 | `canary` | 피드백 문구·참여자 표 정리 | [`dff7564`](https://github.com/sayknow/M2-1/commit/dff7564002a5cbab9c16763c4ebbe0798e04d5cc) |
| [PR #14](https://github.com/sayknow/M2-1/pull/14) | `woogie0403` | 10/29 11:34:22 | `canary` | 역할 분담·관련 문서 동기화 | [`757bdbb`](https://github.com/sayknow/M2-1/commit/757bdbba394e2cdf59dca1a09d5aef4240fcbfde) |
| [PR #15](https://github.com/sayknow/M2-1/pull/15) | `jojunsu98` | 10/29 21:57:31 | `canary` | 다크 모드·제품 카드 배지 정리 | [`16d1288`](https://github.com/sayknow/M2-1/commit/16d12887f7b8254a3c98a3a9366540340bd130d6) |

## 4. 전체 커밋 목록

다음 표는 **Git 커미터 시각**을 KST로 바꿔 시간순으로 정리했다. 작성자 열은 Git의 `author` 값이다. 원래 커밋의 작성 시각·병합 시각·로컬 테스트 시각은 서로 다를 수 있다. 원문 커밋 메시지와 상세 변경은 각 커밋 링크에서 확인한다.

포함 브랜치는 `M=main`, `C=canary`, `D=dev`, `P=production`이다. 해당 커밋이 그 브랜치 이력에 포함되는지를 확인한 값이며, 서로 다른 커밋 ID라도 파일 내용은 같을 수 있다. 문자가 없으면 해당 커밋이 그 브랜치 이력에 없다는 뜻이다. 기능의 반영 여부는 병합 커밋 ID만이 아니라 실제 변경 커밋을 함께 확인한다.


### 2026-10-20

| 시각 | 커밋 | 구분 | 작성자 | 변경 요약 | 포함 브랜치 |
|---|---|---|---|---|---|
| 22:34:17 | [`de683ca`](https://github.com/sayknow/M2-1/commit/de683ca718519e8b486cfc4e5528d35ad8ce8d96) | 변경 | [sayknow](https://github.com/sayknow) | 검수 상품 데이터·수집/대조 자료와 모바일 화면 프로토타입을 최초 저장 | M · C · D · P |
| 22:35:12 | [`badf876`](https://github.com/sayknow/M2-1/commit/badf876deca519abd16867d175501dc564ee48df) | 변경 | [sayknow](https://github.com/sayknow) | 저장소 백업 범위와 상태 설명 정리 | M · C · D · P |

### 2026-10-21

| 시각 | 커밋 | 구분 | 작성자 | 변경 요약 | 포함 브랜치 |
|---|---|---|---|---|---|
| 11:39:24 | [`fb2cce0`](https://github.com/sayknow/M2-1/commit/fb2cce091f495581ffdb60b7c43117f7a9168f35) | 변경 | [sayknow](https://github.com/sayknow) | 공식 상품 사진·DB 조회·FastAPI·초기 Gemini 추천/대화 연결 | M · C · D · P |
| 11:59:16 | [`0496668`](https://github.com/sayknow/M2-1/commit/0496668c78b701e09e672f86d6eb41ee299ab68c) | 변경 | [sayknow](https://github.com/sayknow) | Render 외부 배포와 접속 검사 기록 추가 | M · C · D · P |
| 20:21:24 | [`c8fa914`](https://github.com/sayknow/M2-1/commit/c8fa914815cf883d47d22619c5b691a55c7bd0d5) | 변경 | [sayknow](https://github.com/sayknow) | 함량·기준량 시작 질문에 공식 표시 읽기 근거 검색 연결 | M · C · D · P |
| 20:26:07 | [`686d8a2`](https://github.com/sayknow/M2-1/commit/686d8a217f1cab59fd7200d95d3269eb7ec2b898) | 변경 | [sayknow](https://github.com/sayknow) | 운영 시작 질문 회귀 검사 결과 기록 | M · C · D · P |
| 21:06:44 | [`b1185bf`](https://github.com/sayknow/M2-1/commit/b1185bf8274f855f9616aee930d6c59b3f2f60a6) | 변경 | [sayknow](https://github.com/sayknow) | 일반 영양 지식 검색과 상담형 AI 대화로 질문 범위 확대 | M · C · D · P |
| 21:14:06 | [`10656a7`](https://github.com/sayknow/M2-1/commit/10656a73e344cf08d9aa1084fd24de1a35973c15) | 변경 | [sayknow](https://github.com/sayknow) | 상담 기능 배포 검증과 입력 안내 정리 | M · C · D · P |
| 21:15:43 | [`3a9d67e`](https://github.com/sayknow/M2-1/commit/3a9d67ebca74f48d2062f752bff4b33b66c4a5f9) | 변경 | [sayknow](https://github.com/sayknow) | 상담 프런트엔드 배포 확인 기록 | M · C · D · P |
| 21:35:36 | [`795a23c`](https://github.com/sayknow/M2-1/commit/795a23c94bdb69a2321154dcc5a6501a6d533b2c) | 변경 | [sayknow](https://github.com/sayknow) | 홈·제품 찾기의 첫 방문자용 제목 문구 개선 | M · C · D · P |

### 2026-10-22

| 시각 | 커밋 | 구분 | 작성자 | 변경 요약 | 포함 브랜치 |
|---|---|---|---|---|---|
| 17:45:00 | [`1e44b76`](https://github.com/sayknow/M2-1/commit/1e44b762b6b71e8ba0b53fbd18698c3efe20cf68) | 변경 | [sayknow](https://github.com/sayknow) | vitastep-guide 주소 적용과 주소 전환 검사 기록 | M · C · D · P |

### 2026-10-23

| 시각 | 커밋 | 구분 | 작성자 | 변경 요약 | 포함 브랜치 |
|---|---|---|---|---|---|
| 09:35:55 | [`0eb636a`](https://github.com/sayknow/M2-1/commit/0eb636a898f31c831cbd966f7c1229a3751325db) | 변경 | [sayknow](https://github.com/sayknow) | 소유자 관리 브랜치 절차·PR 템플릿·오프라인 CI 도입 | C · D · P |
| 09:39:52 | [`aa78a5a`](https://github.com/sayknow/M2-1/commit/aa78a5ad56c3e9f10373f9437c21b5663b896c79) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #1](https://github.com/sayknow/M2-1/pull/1) · 브랜치 관리·CI 도입 | C · D · P |
| 09:41:26 | [`e885bf6`](https://github.com/sayknow/M2-1/commit/e885bf6940093f3ab4b5bef047fe7445cb563059) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #2](https://github.com/sayknow/M2-1/pull/2) · 브랜치 관리 체계를 프로덕션에 반영 | C · D · P |
| 11:42:32 | [`c450731`](https://github.com/sayknow/M2-1/commit/c450731ce7a31be267c2347b7cad0b3800e0d5c0) | 변경 | [sayknow](https://github.com/sayknow) | Gemini에서 COPA GPT로 전환하기 위한 연결 구현 | C · D · P |
| 12:47:12 | [`6f59312`](https://github.com/sayknow/M2-1/commit/6f593123c912c5a60c381b1ee7021d32112b1766) | 변경 | [sayknow](https://github.com/sayknow) | 실제 GPT 도구 호출 검증 및 COPA 미지원 옵션 처리 | C · D · P |
| 12:56:51 | [`8b77b2d`](https://github.com/sayknow/M2-1/commit/8b77b2d1dd3ec193293e3f3007360846288b8a04) | 변경 | [sayknow](https://github.com/sayknow) | 데브 승격 전 카나리 로컬 GPT 통합 검사 기록 | C · D · P |
| 12:58:25 | [`d458643`](https://github.com/sayknow/M2-1/commit/d4586434f9eeb3b9254a628e54cfa5ff6aac0c53) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #3](https://github.com/sayknow/M2-1/pull/3) · COPA GPT 연결·호환성 검증 | C · D · P |
| 15:21:38 | [`b75f847`](https://github.com/sayknow/M2-1/commit/b75f84792507f32401898b2f47ac189aeb71a69a) | 변경 | [sayknow](https://github.com/sayknow) | 표시 목적 기반 추천 순위·관련 성분 구분·포장 변형 묶기 개선 | C · D · P |
| 15:22:41 | [`8869bab`](https://github.com/sayknow/M2-1/commit/8869bab9db8b625799bfa81a3789cd11c1a3b01e) | 이력 동기화 | [sayknow](https://github.com/sayknow) | 데브 이력을 카나리에 정상 병합하여 공통 이력 반영 | C · D · P |
| 15:31:39 | [`9cb0060`](https://github.com/sayknow/M2-1/commit/9cb00601bef8f95b792bc22551bec9471ea76026) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #4](https://github.com/sayknow/M2-1/pull/4) · 목적 중심 추천 정책 개선 | C · D · P |
| 17:31:03 | [`7f392c2`](https://github.com/sayknow/M2-1/commit/7f392c25eeff9c4d3a4b2b65d3b8464a4a271fef) | 변경 | [sayknow](https://github.com/sayknow) | AI 제품 비교 해설 추가 및 추천 관심 분야를 5개로 정리 | C · D · P |
| 17:33:37 | [`11ce98e`](https://github.com/sayknow/M2-1/commit/11ce98e40a7edd2ed085921eb9db7db72f09a912) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #5](https://github.com/sayknow/M2-1/pull/5) · 다섯 관심 분야·AI 비교 해설 | C · D · P |
| 17:44:21 | [`0bc17dc`](https://github.com/sayknow/M2-1/commit/0bc17dca34f3ec6479549248798e76bfcb962064) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #6](https://github.com/sayknow/M2-1/pull/6) · GPT 추천·비교를 프로덕션에 반영 | C · D · P |

### 2026-10-24

| 시각 | 커밋 | 구분 | 작성자 | 변경 요약 | 포함 브랜치 |
|---|---|---|---|---|---|
| 13:35:48 | [`e40d644`](https://github.com/sayknow/M2-1/commit/e40d6441e650d8c37e8acb3dbe56845029f5b9c8) | 변경 | [sayknow](https://github.com/sayknow) | 최종 제출 문서·팀 역할·피드백 기록 정리 | C · D · P |
| 13:40:59 | [`e3fcab0`](https://github.com/sayknow/M2-1/commit/e3fcab0e3db5ae36c5ee8c796650a78da81d4971) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #7](https://github.com/sayknow/M2-1/pull/7) · 최종 제출 문서·피드백 기록 정리 | C · D · P |
| 13:42:00 | [`4eedc4e`](https://github.com/sayknow/M2-1/commit/4eedc4e329028f560857b241d5290d1fdd07e88b) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #8](https://github.com/sayknow/M2-1/pull/8) · 제출 문서를 프로덕션에 반영 | C · D · P |
| 15:38:59 | [`b6ba219`](https://github.com/sayknow/M2-1/commit/b6ba219a4c1ff33a75a34103e6f4a3b713a5aad0) | 변경 | [sayknow](https://github.com/sayknow) | 제품별 AI 시작 질문·간단한 성분 설명·공식 성인 섭취기준 비교 추가 | C · D · P |
| 15:41:03 | [`01ca19d`](https://github.com/sayknow/M2-1/commit/01ca19d19b3f06d8c3e3b8bf5ab58738382d2847) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #9](https://github.com/sayknow/M2-1/pull/9) · 제품 AI 질문·성분 요약·성인 기준 비율 | C · D · P |
| 15:54:44 | [`6ae740b`](https://github.com/sayknow/M2-1/commit/6ae740b047bb7ffa54f70fdbb7062e9a24f43333) | 변경 | [sayknow](https://github.com/sayknow) | 설문 3·4번 선택지 축소 및 비교 범위·상담 필요 안내 추가 | C · D · P |
| 15:56:06 | [`f6a9a6b`](https://github.com/sayknow/M2-1/commit/f6a9a6b7ea357a7e7aa5e26e23efbc481505b608) | 이력 동기화 | [sayknow](https://github.com/sayknow) | 데브 이력을 카나리에 정상 병합하여 공통 이력 반영 | C · D · P |
| 15:57:18 | [`3d8d359`](https://github.com/sayknow/M2-1/commit/3d8d359b7d8a302076036d074b903683a608b037) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #10](https://github.com/sayknow/M2-1/pull/10) · 설문 3·4번 선택지·안내 정리 | D · P |
| 16:12:43 | [`b9ba2d3`](https://github.com/sayknow/M2-1/commit/b9ba2d3434d51e505bf13c6f1de2fa2e9d213f7d) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #11](https://github.com/sayknow/M2-1/pull/11) · 성분 설명·설문 개선을 프로덕션에 반영 | P |
| 19:05:41 | [`c8b9462`](https://github.com/sayknow/M2-1/commit/c8b94625d787c7221fcbff4d6d8241497572e530) | 변경 | [etu9317cw](https://github.com/etu9317cw) | README·LICENSE·기획서·명세서·피드백 문서 재작성 | C |
| 19:05:41 | [`628b141`](https://github.com/sayknow/M2-1/commit/628b141263b8042a41c2ceccc3669383d8e66e89) | 변경 | [etu9317cw](https://github.com/etu9317cw) | 발표 PDF와 Markdown·HTML 원본 추가 | C |

### 2026-10-28

| 시각 | 커밋 | 구분 | 작성자 | 변경 요약 | 포함 브랜치 |
|---|---|---|---|---|---|
| 19:07:27 | [`bb921e6`](https://github.com/sayknow/M2-1/commit/bb921e6d451aa6ddc70e1cb92cec724ac8482186) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #12](https://github.com/sayknow/M2-1/pull/12) · 제출 문서 재작성·발표 자료 추가 | C |
| 19:55:33 | [`21865ef`](https://github.com/sayknow/M2-1/commit/21865efb6d2af037fdf39eaf59d4bd0c20bbf709) | 변경 | [daguri2963](https://github.com/daguri2963) | 최종 피드백 문구를 개선 요구사항으로 바꾸고 참여자 표 등 삭제 | C |
| 21:43:51 | [`ff2d348`](https://github.com/sayknow/M2-1/commit/ff2d34822bbb2261668d56b9375e028eff7d27fb) | 변경 | [love4xox](https://github.com/love4xox) | 팀 역할을 재배정하고 README·기획서·발표 원본 등 문서 동기화 | C |

### 2026-10-29

| 시각 | 커밋 | 구분 | 작성자 | 변경 요약 | 포함 브랜치 |
|---|---|---|---|---|---|
| 11:33:59 | [`dff7564`](https://github.com/sayknow/M2-1/commit/dff7564002a5cbab9c16763c4ebbe0798e04d5cc) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #13](https://github.com/sayknow/M2-1/pull/13) · 피드백 문구·참여자 표 정리 | C |
| 11:34:22 | [`757bdbb`](https://github.com/sayknow/M2-1/commit/757bdbba394e2cdf59dca1a09d5aef4240fcbfde) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #14](https://github.com/sayknow/M2-1/pull/14) · 역할 분담·관련 문서 동기화 | C |
| 21:09:59 | [`d94c09b`](https://github.com/sayknow/M2-1/commit/d94c09b0d894dfe11923bf013b868806b998df0f) | 변경 | [조준수](https://github.com/jojunsu98) | 다크 모드·브라우저 테마 저장 추가 및 제품 카드 표시 검수 배지 제거 | C |
| 21:57:30 | [`16d1288`](https://github.com/sayknow/M2-1/commit/16d12887f7b8254a3c98a3a9366540340bd130d6) | PR 병합 | [sayknow](https://github.com/sayknow) | [PR #15](https://github.com/sayknow/M2-1/pull/15) · 다크 모드·제품 카드 배지 정리 | C |
| 21:58:00 | [`ab3e8bf`](https://github.com/sayknow/M2-1/commit/ab3e8bfd175ebe0e3c2669d8cd65755164157d5a) | 변경 | [sayknow](https://github.com/sayknow) | PR #15 반영 후 App.tsx·styles.css의 문서 기준 해시 갱신 | C |

## 5. 기능 작성과 병합·정리 기여의 구분

기능을 만든 커밋의 작성자와 PR을 병합한 사람은 별도로 기록한다. 커밋 수로 기여율이나 작업 시간을 추정하지 않는다. 같은 계정으로 저장한 공동 작업은 이 이력만으로 개인별 작업을 나눌 수 없다.

| 사례 | 변경 작성 | 통합·후속 정리 |
|---|---|---|
| 다크 모드·배지 정리 | 조준수(`jojunsu98`), [`d94c09b`](https://github.com/sayknow/M2-1/commit/d94c09b0d894dfe11923bf013b868806b998df0f) | `sayknow`가 [PR #15](https://github.com/sayknow/M2-1/pull/15) 병합, 이후 [`ab3e8bf`](https://github.com/sayknow/M2-1/commit/ab3e8bfd175ebe0e3c2669d8cd65755164157d5a)에서 문서 해시 갱신 |
| 제출 문서·발표 자료 | Git 작성자 `etu9317cw`, [`c8b9462`](https://github.com/sayknow/M2-1/commit/c8b94625d787c7221fcbff4d6d8241497572e530) · [`628b141`](https://github.com/sayknow/M2-1/commit/628b141263b8042a41c2ceccc3669383d8e66e89) | `sayknow`가 [PR #12](https://github.com/sayknow/M2-1/pull/12) 병합 |
| 피드백 문서 수정 | Git 작성자 `daguri2963`, [`21865ef`](https://github.com/sayknow/M2-1/commit/21865efb6d2af037fdf39eaf59d4bd0c20bbf709) | `sayknow`가 [PR #13](https://github.com/sayknow/M2-1/pull/13) 병합 |
| 역할 분담 문서 수정 | Git 작성자 `love4xox`, [`ff2d348`](https://github.com/sayknow/M2-1/commit/ff2d34822bbb2261668d56b9375e028eff7d27fb) | PR 제안 계정은 `woogie0403`, `sayknow`가 [PR #14](https://github.com/sayknow/M2-1/pull/14) 병합 |

**2026-10-30 계정 연결 보완:** 사용자가 `sayknow=이승현`, `jojunsu98=조준수`, `etu9317cw=윤준서`, `daguri2963=배창민`, `woogie0403=김재욱`을 확인했다. PR #12는 윤준서, PR #13은 배창민, PR #14는 김재욱이 우리 저장소의 포크 `woogie0403/M2-1-final`에서 제출해 canary에 병합된 기여 기록이다. PR #14의 커밋 작성 계정은 `love4xox`(실명·팀 소속 미확인)이며 제안자·작성자·병합자를 구분한다. 이 계정 연결 보완은 위 고정 커밋 스냅샷의 개수·작성자·시각을 변경하지 않는다. 개인별 포크·커밋·PR 링크는 [팀원 역할·기여 문서](final/team-contributions.md)에서 확인한다.

## 6. 이 문서 관리 방법

1. 새 변경이 들어오면 실제 변경 커밋·PR 번호·작성 계정·병합 대상·병합 시각을 확인한다.
2. 2절에는 사용자가 이해할 수 있는 변경 목적을, 3절에는 PR 병합 결과를, 4절에는 빠진 커밋 없이 이력을 추가한다. 상세 작업 설명은 커밋/기능 문서에 링크한다.
3. 기준 커밋과 원격 브랜치 SHA를 갱신한 뒤 전체 개수와 포함 브랜치를 다시 계산한다. 과거 행의 날짜·작성자를 새 날짜나 병합자로 덮어쓰지 않는다.
4. 진행 기록은 의사결정 중심, 이 문서는 커밋·PR 추적 중심으로 관리한다. 동일한 전체 커밋 표를 다른 문서에 복제하지 않는다.
5. 이 커밋 표는 `ab3e8bf`까지의 고정 스냅샷이다. 이후 로컬 문서 정리는 커밋·PR이 생성된 뒤 이력에 추가한다. README 복제본의 버전별 보관은 도입하지 않기로 했고, 아키텍처 통신의 요청·응답 표시는 별도 문서 수정으로 진행한다. 문서 전체 재편은 후속 작업이다.

조회에 사용한 기본 명령은 다음과 같다. 시간은 기록 시 KST로 변환한다.

```sh
git log --all --format="%H %cI %an %s"
git merge-base --is-ancestor <commit> <branch>
gh pr list --state all --limit 100 --json number,author,baseRefName,mergedAt,mergeCommit,url
```

[루트 README](../README.md) · [최종 제출 목차](final/README.md) · [프로젝트 진행 기록](final/progress.md) · [브랜치 운영 절차](../CONTRIBUTING.md)
