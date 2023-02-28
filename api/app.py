from fastapi import FastAPI

from pydantic import BaseSettings
from api.database import create_db_and_tables
from api.public import api as public_api
from api.utils.mock_data_generator import create_heroes_and_teams


def create_app(settings: BaseSettings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        description=settings.DESCRIPTION,
    )

    @app.on_event("startup")
    def on_starup():
        create_db_and_tables()
        create_heroes_and_teams()

    app.include_router(public_api)

    return app
