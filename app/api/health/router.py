from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.core.database import check_database_connection

router = APIRouter()


@router.get("/health")
async def health_check():
    return { "status": "ok" }

@router.get("/ready")
async def readiness_check():
    database_connected = await check_database_connection()

    if not database_connected:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": 'not ready',
                "database": "disconnected"
            }
        )
        
    return {
        "status": "ready",
        "database": "connected"
    }