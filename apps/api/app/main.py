from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.tasks import router as tasks_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    yield


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "API is running", "environment": settings.app_env}


app.include_router(health_router)
app.include_router(tasks_router)