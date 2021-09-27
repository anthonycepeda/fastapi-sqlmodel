from pydantic.types import Optional
from sqlmodel import Field, Relationship, SQLModel

from api.public.team.models import Team


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None

    team_id: Optional[int] = Field(default=None, foreign_key="team.id")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Super Man",
                "secret_name": "Clark Kent",
                "age": 27,
                "team_id": 1,
            }
        }


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    team: Optional[Team] = Relationship(back_populates="heroes")


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(HeroBase):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
    team_id: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Super Man",
                "secret_name": "Clark Kent",
                "age": 27,
                "team_id": 1,
            }
        }
