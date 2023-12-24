from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.config import Settings
from api.database import create_db_and_tables
from api.public import api as public_api
from api.utils.mock_data_generator import create_heroes_and_teams


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    create_heroes_and_teams()

    yield


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
        lifespan=lifespan,
    )

    app.include_router(public_api)

    return app
