from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.api.health.router import router as health_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Application startup")

    yield

    print("🛑 Application shutdown")

def create_app() -> FastAPI:

    app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
  )

    app.include_router(health_router)  

    return app 

app = create_app()

