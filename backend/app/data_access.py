# app/data_access.py

from .models import Spell
from app import create_app, db

app = create_app()


#Get random spells of a certain level
def get_random_spells(class_type, level, number):

    with app.app_context():

        class_col = getattr(Spell, class_type.lower())

        query = (Spell.query
                .filter(class_col == True,
                        Spell.level == level)
                .order_by(db.func.random())
                .limit(number)
                .all()
        )
        print(query[0].spell_name)
        print(query[0].m)

#Get random spells with a theme of a certain level
def get_random_themed_spells(class_type, level, number, damage_type=None, school=None):

    with app.app_context():

        class_col = getattr(Spell, class_type.lower())

        query = Spell.query.filter(class_col == True)  # filtering by class

        if school is not None:
                query = query.filter(Spell.school == school)   # checking to see if theres a school of magic filter

        if damage_type is not None:
                query = query.filter(Spell.damage_type == damage_type) # filtering by damage type

        return (Spell.query
                .filter(Spell.class_col == True,
                        Spell.level == level)
                .order_by(db.func.random())
                .limit(number)
                .all()
        )
