from fastapi import APIRouter, Depends, Query
from pydantic.types import List

from api.database import get_session
from api.public.team.crud import (
    create_team,
    update_team,
    delete_team,
    read_team,
    read_teams,
)

from sqlmodel import Session
from api.public.team.models import TeamCreate, TeamRead, TeamUpdate

router = APIRouter()


@router.post("", response_model=TeamRead)
def create_a_team(team: TeamCreate, db: Session = Depends(get_session)):
    return create_team(team=team, db=db)


@router.get("", response_model=List[TeamRead])
def get_teams(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    return read_teams(offset=offset, limit=limit, db=db)


@router.get("/{team_id}", response_model=TeamRead)
def get_a_team(team_id: int, db: Session = Depends(get_session)):
    return read_team(team_id=team_id, db=db)


@router.patch("/{team_id}", response_model=TeamRead)
def update_a_team(team_id: int, team: TeamUpdate, db: Session = Depends(get_session)):
    return update_team(team_id=team_id, team=team, db=db)


@router.delete("/{team_id}")
def delete_a_team(team_id: int, db: Session = Depends(get_session)):
    return delete_team(team_id=team_id, db=db)
