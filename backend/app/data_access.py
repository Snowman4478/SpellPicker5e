# app/data_access.py

from .models import Spell
from app import create_app, db

app = create_app()


#Get random spells of a certain level
def get_random_spells(class_type, level, number):

    with app.app_context():

        class_col = getattr(Spell, class_type.lower())

        return (Spell.query
                .filter(class_col == True,
                        Spell.level == level)
                .order_by(db.func.random())
                .limit(number)
                .all()
        )
        

#Get random spells with a theme of a certain level
def get_random_themed_spells(class_type, level, number, damage_type=None, school=None):

    with app.app_context():

        class_col = getattr(Spell, class_type.lower())

        query = Spell.query.filter(class_col == True, Spell.level == level)  # filtering by class and level (needed)

        if school != None:
                query = query.filter(Spell.school == school)   # school of magic filter
        

        if damage_type != None:
                damage_type = damage_type.capitalize()
                damage_query = query.filter(Spell.damage_type.contains(damage_type)) # filtering by damage type
        else:
              damage_query = query  #if no damage type then its just the prev query


        results = damage_query.order_by(db.func.random()).all()   # our spells

        

        # Store ids of already selected spells
        selected_spell_ids = [spell.spell_name for spell in results]


        if len(results) < number:  #If both damage and school filter is too little we remove damage filter
                remaining_needed = number - len(results)
                no_damage_query = (Spell.query
                .filter(Spell.spell_name.notin_(selected_spell_ids), class_col == True, Spell.level == level, Spell.school == school)
                .order_by(db.func.random())
                .limit(remaining_needed)
                .all()
                )
                
                results.extend(no_damage_query)

                selected_spell_ids.extend([spell.spell_name for spell in no_damage_query])



        if len(results) < number: # Remove school filter to populate with random spells from that class
              remaining_needed = number - len(results)
              remaining_query = (Spell.query
                .filter(Spell.spell_name.notin_(selected_spell_ids), class_col == True, Spell.level == level)
                .order_by(db.func.random())
                .limit(remaining_needed)
                .all()
                )
              results.extend(remaining_query)

        return results[:number]
