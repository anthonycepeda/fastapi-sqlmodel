from api.public.hero.models import Hero
from api.public.team.models import Team
from api.database import engine
from sqlmodel import Session


def create_heroes_and_teams():
    with Session(engine) as session:
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret’s Bar")
        wornderful_league = Team(
            name="Wonderful-League", headquarters="Fortress of Solitude"
        )

        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            age=24,
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name="Spider-Boy",
            secret_name="Pedro Parqueador",
            age=37,
            teams=[team_preventers],
        )
        hero_super_good_boy = Hero(
            name="Super-Good-Boy",
            secret_name="John Goodman",
            age=30,
            teams=[wornderful_league, team_z_force],
        )

        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.add(hero_super_good_boy)
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)
        session.refresh(hero_super_good_boy)

        print("\n=========== MOCK DATA CREATED ===========\n")
        print("Deadpond:", hero_deadpond)
        print("Deadpond teams:", hero_deadpond.teams)
        print("Rusty-Man:", hero_rusty_man)
        print("Rusty-Man Teams:", hero_rusty_man.teams)
        print("Spider-Boy:", hero_spider_boy)
        print("Spider-Boy Teams:", hero_spider_boy.teams)
        print("Super-Good-Boy:", hero_super_good_boy)
        print("Super-Good-Boy Teams:", hero_super_good_boy.teams)
        print("\n===========================================\n")
