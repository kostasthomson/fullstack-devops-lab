from fastapi import FastAPI

from app.api.routes.health import router as health_router

app = FastAPI(title="fullstack-devops-lab api", version="0.1.0")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "API is running"}


app.include_router(health_router)