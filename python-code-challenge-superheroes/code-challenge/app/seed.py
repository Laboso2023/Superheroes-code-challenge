from app import app, db
from models import Hero
from test import all_names


def hero_add():
    with app.app_context():
        hero_objects = [
            Hero(name=hero["name"], super_name=hero["super_name"]) for hero in all_names
        ]
        db.session.bulk_save_objects(hero_objects)
        db.session.commit()




# hero_add()
