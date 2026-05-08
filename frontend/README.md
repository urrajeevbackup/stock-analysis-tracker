# Stock Analysis Tracker Frontend

## Setup
- `cd frontend`
- `npm install`
- Copy `.env.example` to `.env`

## Env
- `VITE_API_BASE_URL=http://127.0.0.1:8000/api/v1`

## Run
- `npm run dev`

## Pages
- Dashboard
- Analysis
- Log Trade
- Trade Detail (`/trades/:id`)
- Live Monitor
- Alert Centre
- Reports

## API Base URL
Configured in `src/services/api.ts` via `VITE_API_BASE_URL`, defaults to `http://127.0.0.1:8000/api/v1`.
