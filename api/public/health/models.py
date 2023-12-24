from enum import Enum

from pydantic import BaseModel


class Status(str, Enum):
    OK = "OK"
    KO = "KO"


class Environment(str, Enum):
    dev = "development"
    stg = "staging"
    prd = "production"


class Health(BaseModel):
    status: Status | None
    environment: Environment | None


class Stats(BaseModel):
    heroes: int | None
    teams: int | None
