from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from api.database import Session, get_session
from api.public.health.crud import get_health, get_stats
from api.public.health.models import Health, Stats
from api.utils.logger import logger_config

router = APIRouter()
logger = logger_config(__name__)


@router.get(
    "",
    response_model=Health,
    status_code=status.HTTP_200_OK,
    responses={200: {"model": Health}},
)
def health(db: Session = Depends(get_session)):
    return get_health(db=db)


@router.get(
    "/stats",
    response_model=Stats,
    status_code=status.HTTP_200_OK,
    responses={200: {"model": Stats}},
)
def health_stats(db: Session = Depends(get_session)):
    return get_stats(db=db)
