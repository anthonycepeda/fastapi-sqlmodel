from fastapi import Depends
from sqlmodel import Session

from api.config import settings
from api.database import get_session
from api.public.health.models import Health, Stats
from api.utils.logger import logger_config

logger = logger_config(__name__)


def get_health() -> Health:
    return Health(status="OK", environment=settings.ENV)
