# app/data_access.py

from app.models import Spell
from app import db

#Get random spells of a certain level
def get_random_spells(class_type, level, number):

    class_col = getattr(Spell, class_type.lower())

    return (Spell.query
            .filter(Spell.class_col == True,
                    Spell.level == level)
            .order_by(db.func.random())
            .limit(number)
            .all()
    )

#Get random spells with a theme of a certain level
def get_random_themed_spells(class_type, level, number, damage_type=None, school=None):

    class_col = getattr(Spell, class_type.lower())

    query = Spell.query.filter(Spell.class_col == True)  # filtering by class

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
