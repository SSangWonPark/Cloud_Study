# 주차별 참고 자료 (링크 모음)

`docs/8week-plan.md`의 주차 구성에 맞춰, 주차마다 가장 핵심적인 자료 1~2개만 골랐습니다. 그 주의 여러 하위 주제를 다 커버하는 자료 대신, 공식 문서와 그 주의 실습에 가장 직접적으로 필요한 글 하나를 우선했습니다. 더 깊게 파고 싶을 때는 `docs/roadmap.md`의 "단계별 추천 학습 자료" 섹션을 참고하세요.

## 1주차 — 클라우드 개념 + 리눅스/네트워킹 기초
- [개발자를 위한 네트워크 기초 완전 정복: TCP/IP, HTTP, DNS, TLS부터 gRPC, WebSocket까지](https://www.youngju.dev/blog/culture/2026-03-23-networking-fundamentals-developer-guide) — 이번 주 네트워킹 파트를 이 글 하나로 다 훑을 수 있음
- [AWS 공식: Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) — 클라우드 개념 중 가장 먼저 이해해야 하는 것

## 2주차 — AWS 코어 서비스 이론 + 계정 안전장치 셋업
- [AWS 공식: Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) — 계정 셋업 전에 꼭 읽을 것
- [AWS Billing and Cost Management Cheat Sheet (Tutorials Dojo)](https://tutorialsdojo.com/aws-billing-and-cost-management/) — Budget Alert 설정 포함, 소액 예산 관리에 바로 씀
- [AWS 공식 Hands-On: Control Your AWS Costs](https://aws.amazon.com/getting-started/hands-on/control-your-costs-free-tier-budgets/) — 프리티어 한도·Budget 설정을 직접 콘솔에서 따라 해보는 공식 실습

## 3주차 — 입문 실습: 정적 사이트 + 첫 EC2
- [AWS 공식: Getting Started with Amazon EC2](https://aws.amazon.com/ec2/getting-started/) — 첫 EC2 인스턴스는 이 공식 가이드로
- [freeCodeCamp: How to Host a Static Website on AWS S3 and CloudFront](https://www.freecodecamp.org/news/host-a-static-website-on-aws-s3-and-cloudfront/) — S3+CloudFront 실습

## 4주차 — 중급 실습: 주식 대시보드를 EC2 + Nginx로 배포·운영 *(재수정: 목표가 서버 직접 운영 경험이므로 EC2로 확정, 서버리스 옵션은 제외)*

난이도순으로 4단계: 기초(인스턴스+SSH) → 핵심(정적 사이트 배포) → 심화(동적 Flask 앱 배포) → 마무리(HTTPS).

1. (기초) [AWS 공식: Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) — 인스턴스 생성 + SSH 접속까지 (웹서버 설치는 안 다룸)
2. (핵심) [Build and Deploy Your First Website on AWS EC2: A Step-by-Step Guide (AWS Builder Center)](https://builder.aws.com/content/3KeFaA8Vbp6oCH8rZnXqS5oPI9Z/build-and-deploy-your-first-website-on-aws-ec2-a-step-by-step-guide) — 보안그룹 HTTP(80) 오픈 → SSH → Nginx 설치 → 정적 사이트 배포까지 짧고 명확하게 완주 (AWS 운영, 공식 문서는 아님)
3. (심화) [영상: How to deploy flask app on AWS EC2 instance using NGINX server (YouTube)](https://www.youtube.com/watch?v=AFpYh8d9yW8) / [Deploying Flask to AWS: Amazon Linux 2, Nginx (The Coding Interface)](https://thecodinginterface.com/blog/flask-aws-ec2-deployment/) — 정적 사이트에서 실제 Flask 앱(동적) 배포로 넘어가는 단계
4. (마무리) [AWS re:Post 공식: Use Certbot to enable HTTPS on Amazon Linux 2023 EC2 instances](https://repost.aws/articles/AR_doGU0cxQymwf5A1Gl97yA/use-certbot-to-enable-https-with-apache-or-nginx-on-ec2-instances-running-amazon-linux-2023-al2023) — HTTPS 적용

## 5주차 — 심화 실습: Terraform으로 코드화 + CI/CD
- [HashiCorp 공식: Terraform — AWS Get Started](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) — Terraform은 이 튜토리얼 하나로 충분
- [AWS DevOps Blog 공식: GitHub Actions CI/CD로 EC2에 배포하기](https://aws.amazon.com/blogs/devops/integrating-with-github-actions-ci-cd-pipeline-to-deploy-a-web-app-to-amazon-ec2/)

## 6주차 — PDF-Ontology-RAG 클라우드 아키텍처 구축 착수
- [Neo4j 공식: Neo4j on AWS — Operations Manual](https://neo4j.com/docs/operations-manual/current/cloud-deployments/neo4j-aws/) — 공식 배포 가이드
- [How to host Neo4j on EC2 using Docker (DEV Community)](https://dev.to/foundanand/how-to-host-neo4j-on-ec2-using-docker-2dem) — 기존에 Docker로 Neo4j를 다뤄본 경험과 바로 이어지는 실습형 글
- (선택, RAG API를 컨테이너로 확장할 경우) [AWS 공식 Hands-On: Deploy Docker Containers on Amazon ECS](https://docs.aws.amazon.com/hands-on/latest/deploy-docker-containers/deploy-docker-containers.html)

## 7주차 — 구축 마무리·통합·문서화
- 새 자료 없이 **5주차의 Terraform 자료를 그대로 재사용**하는 주간입니다 — 6주차에 콘솔로 만든 걸 코드로 옮기는 작업 위주라 새 링크보다 반복 적용이 중요합니다.

## 8주차 — 운영: 모니터링·비용·백업·장애대응
- [AWS 공식: AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) — 모니터링/백업/비용/장애대응을 관통하는 운영 체크리스트, 이번 주 전체를 이 프레임워크로 점검
- [AWS 공식: Create a CloudWatch alarm for an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-createalarm.html) — 이번 주 실제로 손으로 할 작업

---

## 보충: 글보다 영상이 편할 때

주차별 필수 자료는 위 글/공식 문서로 충분하지만, 개념을 영상으로 한 번 더 훑고 싶을 때 쓸 수 있는 것들만 큰 주제별로 하나씩 추렸습니다 (매주 넣지 않고, 필요한 사람만 골라보도록 최소한으로).

- **AWS 전반 개론 (1~2주차)**: [AWS Certified Cloud Practitioner Training — Full Course (freeCodeCamp)](https://www.youtube.com/watch?v=3hLmDS179YE) — 4시간, 클라우드 개념부터 서비스 개관까지
- **네트워킹 + VPC (1, 3주차)**: [AWS Networking Explained for Beginners – VPCs, Subnets, CloudFront, Direct Connect & VPN](https://www.youtube.com/watch?v=n0ODDF69gWM)
- **Docker (4, 6주차)**: [Docker Tutorial for Beginners \[FULL COURSE in 3 Hours\] (TechWorld with Nana)](https://www.youtube.com/watch?v=3c-iBn73dDE) — 애니메이션 설명 + 실습이 같이 있어 이해가 빠름
- **Terraform (5, 7주차)**: [Complete Terraform Course - From BEGINNER to PRO! (TechWorld with Nana)](https://www.youtube.com/watch?v=7xngnjfIlK4)
- **Neo4j (6주차)**: [Neo4j (Graph Database) Crash Course](https://www.youtube.com/watch?v=8jNPelugC2s)
- **CloudWatch (8주차)**: [AWS CloudWatch Tutorial for Beginners | Metrics, Alarms, Dashboards & Logs Explained](https://www.youtube.com/watch?v=dQPXBohP0hw)
