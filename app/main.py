from fastapi import FastAPI
from app.core.config import settings



def create_app() -> FastAPI:
    app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
  )

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}

    return app 

app = create_app()
