# Cloud Study

퍼블릭 클라우드(AWS 중심)를 공부하고, 최종적으로 본인 연구/프로젝트 인프라(예: PDF-Ontology-RAG, Qwen 평가, 주식 대시보드)를 클라우드 위에 직접 구축·운영해보는 것을 목표로 하는 저장소입니다.

- 학습·구축·운영 전체 로드맵: [`docs/roadmap.md`](docs/roadmap.md)
- **8주 실행 계획(이론→실습→구축→운영)**: [`docs/8week-plan.md`](docs/8week-plan.md)
- 주차별 참고 자료(링크 모음): [`docs/weekly-references.md`](docs/weekly-references.md)
- 주차별 진행 기록: [`docs/study-log.md`](docs/study-log.md)

## 폴더 구조

```
Cloud_Study/
  docs/            # 로드맵, 진행 기록, 아키텍처 문서
  infra/           # Terraform 등 인프라 코드 (실습을 진행하며 채워나갈 폴더)
  apps/            # 클라우드에 올릴 애플리케이션 코드
  scripts/         # 비용 감시/자동 종료 등 운영 스크립트
```

`infra/`, `apps/`, `scripts/`는 실습이 진행되며 내용이 생기는 대로 채워나가면 됩니다.

## 원칙

- 자격증명(access key, `.pem`, `.env` 등)은 절대 커밋하지 않습니다 — `.gitignore` 참고.
- 콘솔에서 수동으로 만든 리소스는 익숙해지는 대로 Terraform 코드로 옮겨 `infra/`에 커밋합니다.
- 실습 단계가 끝날 때마다 `docs/study-log.md`에 기록을 남깁니다.
