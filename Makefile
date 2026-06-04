api-lint:
	cd apps/api && uv run ruff check .

api-test:
	cd apps/api && uv run pytest -q

api-build:
	cd apps/api && docker build -t fullstack-devops-lab-api .