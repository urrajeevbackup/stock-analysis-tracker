#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${1:-http://127.0.0.1:8000}"
API_PREFIX="/api/v1"

echo "[1/5] Checking Swagger UI..."
curl -fsS "${BASE_URL}/docs" >/dev/null

echo "[2/5] Checking OpenAPI schema..."
curl -fsS "${BASE_URL}/openapi.json" >/dev/null

echo "[3/5] Checking health endpoint..."
curl -fsS "${BASE_URL}${API_PREFIX}/health" | python -m json.tool

echo "[4/5] Listing seeded resources..."
curl -fsS "${BASE_URL}${API_PREFIX}/analysis/" | python -m json.tool
curl -fsS "${BASE_URL}${API_PREFIX}/trades/" | python -m json.tool
curl -fsS "${BASE_URL}${API_PREFIX}/trade-trails/" | python -m json.tool

echo "[5/5] Creating and fetching a sample trade..."
CREATE_RESPONSE=$(curl -fsS -X POST "${BASE_URL}${API_PREFIX}/trades/" \
  -H 'Content-Type: application/json' \
  -d '{
    "user_id": 1,
    "stock_symbol": "AAPL",
    "trade_type": "Swing",
    "entry_price": 191.2,
    "entry_date": "2026-05-08",
    "stop_loss": 184.0,
    "target_price": 205.0,
    "status": "OPEN",
    "notes": "API smoke test sample"
  }')

echo "$CREATE_RESPONSE" | python -m json.tool
TRADE_ID=$(echo "$CREATE_RESPONSE" | python -c 'import json,sys; print(json.load(sys.stdin)["id"])')
curl -fsS "${BASE_URL}${API_PREFIX}/trades/${TRADE_ID}" | python -m json.tool

echo "API validation completed successfully."
