from fastapi import FastAPI
from app.api import chat, files, tasks, skills, tools, results

app = FastAPI(title="Multi-Agent Analytics Backend", version="0.2.0")
app.include_router(chat.router)
app.include_router(files.router)
app.include_router(tasks.router)
app.include_router(skills.router)
app.include_router(tools.router)
app.include_router(results.router)


@app.get('/health')
def health() -> dict:
    return {"status": "ok"}
