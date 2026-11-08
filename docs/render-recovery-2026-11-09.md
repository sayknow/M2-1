# 무료 운영 서버 복구 — 2026-11-09

[문서 전체 목차](final/README.md) · [현재 보안·운영](final/security-and-operations.md) · [기술 검증 요약](final/evidence/render-recovery-2026-11-09.json)

2026-11-08~09 KST에 동일 소스 `4492a7147e55008567f18cd625e8b9f408bb70f5`의 배포 환경을 변경하고 운영 사이트에서 검증했다. 앱 코드·추천 정책·제품 DB는 수정하지 않았다. 이 기록의 문서 커밋과 이미 적용한 Render 설정 변경은 별개다.

## 장애와 원인 범위

기존 Singapore/Docker 백엔드는 배포 직후 정상 작동했지만 15분 유휴 종료 뒤 다음 접속에 응답하지 않았다. 같은 코드의 새 Singapore/Docker 서버에서도 재현됐다. AI·FastAPI·DB를 제외한 최소 Python HTTP 서버를 대조 시험한 결과도 17분 유휴 후 첫 요청이 약120초 동안 응답하지 않았다.

동일 코드를 Oregon/Python 환경으로 이전한 뒤 유휴 후 자동 기동과 실제 기능이 정상 작동했다. 지역과 실행 환경을 함께 변경했으므로 Singapore 또는 Docker 하나만을 단독 원인으로 단정하지 않는다. Render 내부의 정확한 기동 실패 원인은 확인하지 못했다.

## 현재 운영 설정

| 항목 | 값 |
|---|---|
| 홈페이지 | https://vitastep-guide.onrender.com/ — 주소 유지 |
| 프런트 서비스 | `vitastep-guide` / `srv-dbcsntavcj2c73fofdpg` |
| 공개 API 주소 | https://vitastep-api-recovery.onrender.com |
| 백엔드 서비스 | `vitastep-api-recovery` / `srv-dbo8alm7bikc7387o7m0` |
| 지역·실행 환경·요금제 | Oregon · Python 3 · Free |
| 배포 브랜치·자동 배포 | `production` · `After CI Checks Pass` |
| Python | `PYTHON_VERSION=3.13.15` |
| 빌드 | `pip install --no-cache-dir -r backend/requirements.lock` |
| 시작 | `uvicorn backend.main:app --host 0.0.0.0 --port $PORT --no-access-log` |
| 상태 검사 | `/api/health` |
| 프런트 공개 환경변수 | `VITE_API_BASE_URL=https://vitastep-api-recovery.onrender.com` |
| 허용 출처 | `https://vitastep-guide.onrender.com,http://127.0.0.1:5173,http://localhost:5173` |
| AI | COPA `gpt-5.4` — 기존 제공자·모델 유지 |

`COPA_API_KEY`는 사용자 승인 후 새 백엔드의 비밀 환경변수에만 등록했다. 실제 값은 문서·Git·화면·검사 보고서에 넣지 않는다. 프런트 환경변수를 바꾸면 정적 자산을 다시 빌드해야 한다. 실제 공개 번들 `/assets/index-BZw8EaCE.js`의 새 API 주소 반영을 확인했다.

이전 `m2-1-api`(`srv-dbc2hefavr4c73ekh06g`)는 삭제하지 않고 자동 배포를 Off로 바꾸어 보존했다. 현재 대표 홈페이지는 이 서버에 연결하지 않는다. 대조 시험용 `vitastep-api-test`(`srv-dbo1s4gu01pc73e21pjg`)는 임시 실행 명령과 상태 검사 경로를 원복한 뒤 Suspend했다. 원래 Dockerfile은 저장소에 남아 있으며 새 운영 서버의 실행 방식은 아니다.

## 성공 기준과 실측 결과

성공 기준은 **기능 정상 동작과 15분 이상 유휴 후 최초 접속에서 60초 이내 복귀**였다. 서버를 계속 깨워 두는 주기적 요청을 추가하지 않고 실제 유휴 종료를 허용해 측정했다.

| 검사 | 결과 |
|---|---|
| 새 백엔드 17분 유휴 후 첫 요청 | 31.512초에 ready·AI 설정 확인 |
| 실제 운영 홈페이지 17분 유휴 후 첫 접속 | 40.905초 시점에 정상 홈·87개 제품 링크 표시 확인 |
| 필수 기능 M01·M02·M03·M04·M05·M06·M07·M09 | 각각3회 중3회 성공 |
| S01 AI 비교 해설 | 3회 중3회 성공 |
| 운영 브라우저 | 설문 추천·추천 설명·비교표·AI 비교 해설·제품 맥락 AI 대화·함량 카드·제품 상세·카탈로그·동의 철회 확인 |
| 최종 재기동 직후 | 제품 목록87개·상세·비교·CORS·실제 AI 답변 정상 |
| 최종 AI 첫 질문 | “함량과 기준량의 차이가 궁금해요.” — 실제 AI 응답, 검색 도구 성공, 출처2개 확인 |

운영 홈페이지가 서버 준비 안내에서 자동으로 정상 화면으로 전환되는 것을 확인했다. 40.905초는 정상 화면을 관측한 시점의 경과 시간이다. 이후 API 점검에서도 실제 AI 답변이 약14.8초에 생성됐다. AI 답변 생성 시간은 서버 재기동 시간과 별개다.

위 결과는 가상 성인 선택값을 사용한 개발자 QA이며 독립적인 실사용자 피드백이 아니다. 임시 세션과 브라우저 입력은 정리했다. 2026-10월의 기존 API 증빙은 당시 결과대로 보존하며 이 검사로 덮어쓰지 않는다.

## 비용·한계·후속 점검

유료 전환은 하지 않았다. 복구 중 확인한 Billing 기준 월 누적·예상 요금은 모두 $0.00이었다. 무료 실행3.28/750시간·빌드5/500분·전송3MB/5GB는 해당 시점 계정 전체 스냅샷이며 앞으로의 잔여량 보장이 아니다. Render 사용량과 COPA 사용량은 별개다.

이번 유휴 재기동은 두 번 모두 기준을 통과했지만 무료 서버의 모든 향후 기동 시간을 보장하지는 않는다. 재발 시 Render 배포·로그·상태, `/api/health`와 실제 제품 조회를 구분해 확인한다. 실제 AI 성공 여부는 별도 질문으로 확인한다. 기존 서버로 되돌릴 경우 먼저 유휴 재기동까지 확인한 뒤 프런트 API 주소를 변경하고 재배포한다.

재현 가능한 현재 설정은 이 문서에서 관리한다. 실행 소스·검수 DB·분류 자료를 변경하면 기존 `canary → dev → production` 및 CI 절차를 따른다. 사용자 컴퓨터의 상시 실행에 의존하지 않는다.
