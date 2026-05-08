# Backend (FastAPI)

## Run locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

## Swagger and OpenAPI

Once the app is running, open:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

## Seed / Initial sample data

The initial sample records are inserted by the Alembic migration during:

```bash
alembic upgrade head
```

This creates and seeds sample users, analyses, trades, and trade trail records.

## Validate backend APIs quickly

Run this script while the backend is running:

```bash
./scripts/validate_api.sh
```

It validates:
- Swagger and OpenAPI availability
- Health check endpoint
- Seeded list endpoints (`analysis`, `trades`, `trade-trails`)
- Create + fetch flow for a sample trade

## Troubleshooting: `GET /api/v1/analysis/` returns 500

If you see an error like:

- `RuntimeError: 'cryptography' package is required for sha256_password or caching_sha2_password auth methods`

your MySQL user is using an auth plugin that requires `cryptography` in the Python environment.

Fix:

```bash
pip install cryptography
```

Then restart the FastAPI server.


## Troubleshooting: `Database connection failed: OperationalError`

This means FastAPI could not connect to the configured database server.

1. Confirm your database URL/environment:

```bash
cd backend
python - <<'PY'
from app.core.config import settings
print(settings.resolved_database_url)
PY
```

2. If you do not have MySQL running locally, start MySQL or use SQLite for local development:

```bash
export DATABASE_URL="sqlite:///./stock_tracker.db"
alembic upgrade head
uvicorn app.main:app --reload
```

3. If using MySQL, verify DB/user exists and credentials match `DB_*` vars (or `DATABASE_URL`).
