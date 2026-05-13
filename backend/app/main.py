from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import chat, files, tasks, skills, tools, results

app = FastAPI(title="Multi-Agent Analytics Backend", version="0.2.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(files.router)
app.include_router(tasks.router)
app.include_router(skills.router)
app.include_router(tools.router)
app.include_router(results.router)


@app.get('/health')
def health() -> dict:
    return {"status": "ok"}
