from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="AI SaaS Platform",
    description="Local LLM powered AI SaaS using Ollama",
    version="1.0.0"
)

app.include_router(router)
