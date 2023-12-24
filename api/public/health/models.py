from enum import Enum
from typing import Literal

from pydantic import BaseModel


class Status(str, Enum):
    OK = "OK"
    KO = "KO"


class Health(BaseModel):
    app_status: Status | None
    db_status: Status | None
    environment: Literal["development", "staging", "production"] | None


class Stats(BaseModel):
    heroes: int | None
    teams: int | None
