from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.db.database import check_database_connection

router = APIRouter()


@router.get("/health")
def health() -> JSONResponse:
    db_ok = check_database_connection()
    payload = {
        "status": "ok" if db_ok else "degraded",
        "environment": settings.app_env,
        "database_connected": db_ok,
    }

    status_code = status.HTTP_200_OK if db_ok else status.HTTP_503_SERVICE_UNAVAILABLE
    return JSONResponse(content=payload, status_code=status_code)