# HrSystem

This repository contains a full-stack Human Resource Management System (HRMS) with a Django REST API backend and a Vue 3 + Vite frontend.

## Testing

This section describes how to run backend and frontend tests locally and inside Docker. It also covers common test tooling recommendations.

### Backend (Django / DRF)

Prerequisites: virtualenv or Docker running Postgres/Redis.

Run tests locally (virtualenv):

```bash
cd backend
python -m venv .venv
. .venv/bin/activate        # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py test
```

Run tests inside the running docker-compose stack:

```bash
# start services (db, redis, django)
docker-compose up -d db redis
# run Django tests inside the django service
docker-compose exec django python manage.py test
```

Run a single app or test module:

```bash
docker-compose exec django python manage.py test apps.employees.tests
```

Use pytest (recommended for richer assertions):

```bash
pip install pytest pytest-django
pytest -q
```

### Frontend (Vue + Vite)

This scaffold does not include a test runner by default. We recommend using Vitest + @testing-library/vue or Jest.

Install test tooling example (Vitest):

```bash
cd frontend
npm install -D vitest @testing-library/vue @testing-library/jest-dom
# Add a test script to package.json: "test": "vitest"
npm run test
```

If you prefer Jest, install and configure `vue-jest` and run `npm run test` after adding a test script.

Run frontend tests inside Docker (if image includes test deps):

```bash
docker-compose run --rm vue npm run test
```

### Run all tests (quick guide)

From project root you can run backend tests then frontend tests sequentially (example):

```bash
# Backend
docker-compose exec django python manage.py test

# Frontend (locally)
cd frontend && npm run test
```

Automate this in CI (GitHub Actions / GitLab CI) by adding steps to:
- spin up services (Postgres, Redis) via service containers
- run `python manage.py migrate` and `python manage.py test`
- run `npm ci` and the frontend test script

### Code style, type checks and linters

Recommended dev tools:
- flake8 / black / isort for Python
- mypy for static typing
- eslint + Prettier for JS/TS

Run linters locally or in CI before tests.

### Notes
- Make sure the test database settings are configured (Django creates a separate test database by default).
- When running tests in Docker, ensure the `django` container can connect to `db` and `redis` services.
- Add health endpoints (e.g. `/api/health/`) used by deployment health checks and CI readiness probes.
