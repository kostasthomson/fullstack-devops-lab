# fullstack-devops-lab

A guided learning repository for building a production-style full-stack application with modern DevOps practices.

## Goals

- Build a simple application and evolve it step by step.
- Learn backend, frontend, database, containers, CI/CD, cloud, and Kubernetes.
- Keep the repository clean, documented, and production-minded.

## Planned stack

- Frontend: React
- Backend: FastAPI
- Database: PostgreSQL
- Local development: Docker Compose
- CI: GitHub Actions
- Infrastructure as Code: Terraform
- Orchestration: Kubernetes

## Repository structure

- `apps/web` — frontend application
- `apps/api` — backend API
- `infra/docker` — container-related assets
- `infra/terraform` — cloud infrastructure
- `infra/k8s` — Kubernetes manifests or Helm material
- `.github/workflows` — CI/CD pipelines
- `docs` — architecture notes and learning docs
- `scripts` — helper scripts
- `tests` — cross-service or integration tests

## Working rules

- Small commits.
- Clear branch names.
- Prefer documentation with every meaningful change.
- Keep local setup reproducible.