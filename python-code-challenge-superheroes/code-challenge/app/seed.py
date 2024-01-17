from app import app, db
from models import Hero, Power, HeroPower
from test import all_names, powers_data, heros_powers_data


def hero_add():
    with app.app_context():
        hero_objects = [
            Hero(name=hero["name"], super_name=hero["super_name"]) for hero in all_names
        ]
        db.session.bulk_save_objects(hero_objects)
        db.session.commit()
        
        
def power_add():
    with app.app_context():
        power_objects = [
            Power(name=power["name"], description=power["description"]) for power in powers_data
        ]

        db.session.bulk_save_objects(power_objects)
        db.session.commit()

def hero_power_add():
    with app.app_context():
        hero_power_objects = [
            HeroPower(hero_id=hero["hero_id"], power_id=hero["power_id"]) for hero in heros_powers_data
        ]

        db.session.bulk_save_objects(hero_power_objects)
        db.session.commit()


# if __name__ == '__main__':
    # hero_power_add()
    # power_add()
    # hero_add()
