import logging

from fastapi import FastAPI

from app.db import init_db
from app.routers import auth, budgets, ping

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(budgets.router, prefix="/budgets", tags=["budgets"])
    application.include_router(auth.router, prefix="/auth", tags=["auth"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
