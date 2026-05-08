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


## Troubleshooting

- If MySQL authentication uses `caching_sha2_password`/`sha256_password`, ensure dependencies are installed from `requirements.txt` (includes `cryptography`).
- For local `.env`, you can set `DATABASE_URL` directly (for example: `mysql+pymysql://root:password@localhost:3306/stock_tracker`).
