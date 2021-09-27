from pydantic.types import Optional, List
from sqlmodel import Field, Relationship, SQLModel


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

    heroes: List["Hero"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int


class TeamUpdate(TeamBase):
    name: Optional[str] = None
    headquarters: Optional[str] = None
