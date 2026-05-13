# Backend (FastAPI + Skill/Tool Registry)

## Run

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints
- `GET /health`
- `GET /api/tools`
- `GET /api/skills`
- `POST /api/tasks`
