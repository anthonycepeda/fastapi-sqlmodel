from pydantic.types import List, Optional
from sqlmodel import Field, Relationship, SQLModel

from api.utils.generic_models import HeroTeamLink


class TeamBase(SQLModel):
    name: str
    headquarters: str

    class Config:
        schema_extra = {
            "example": {
                "name": "wonderful league",
                "headquarters": "Fortress of Solitude",
            }
        }


class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    heroes: List["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int
    name: Optional[str] = None
    headquarters: Optional[str] = None
    heroes: List = None


class TeamUpdate(TeamBase):
    name: Optional[str] = None
    headquarters: Optional[str] = None
