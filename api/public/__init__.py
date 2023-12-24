from fastapi import APIRouter

from api.public.health import views as health
from api.public.hero import views as heroes
from api.public.team import views as teams

api = APIRouter()


api.include_router(health.router, prefix="/health", tags=["Health"])
api.include_router(heroes.router, prefix="/heroes", tags=["Heroes"])
api.include_router(teams.router, prefix="/teams", tags=["Teams"])
