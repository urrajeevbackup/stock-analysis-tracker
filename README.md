# Stock Analysis Tracker

Monorepo skeleton for web, mobile, and backend services.

## Structure
- `backend/` FastAPI + SQLAlchemy + Alembic + MySQL
- `frontend/` React + Vite + TypeScript + Tailwind CSS
- `mobile/` React Native + Expo + TypeScript
- `docs/` API and architecture documentation

## Quick Start

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Mobile
```bash
cd mobile
npm install
npx expo start
```

## Notes
- Authentication logic is not implemented yet.
- NSE live integration is not implemented yet.
- PDF/CSV export is not implemented yet.
