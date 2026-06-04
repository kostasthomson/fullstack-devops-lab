from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version="0.1.0")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "API is running", "environment": settings.app_env}


app.include_router(health_router)