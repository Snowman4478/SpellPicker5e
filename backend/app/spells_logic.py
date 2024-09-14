from .helper_functions.spell_calc_helpers import num_of_spells_by_class, cantrip_number, highest_spell_slot
from .data_access import get_random_spells, get_random_themed_spells

import random


def generate_numb_spells_per_level(highest_spell_slot, numb_of_spells):

    if numb_of_spells < highest_spell_slot:
        raise ValueError("Number of spells cannot be less than the highest spell slot to ensure at least one spell per spell level")

    numb_of_spells_per_level = {i: 0 for i in range(1, 10)}

    weights = list()

    for i in range(1, highest_spell_slot + 1):
        numb_of_spells_per_level[i] = 1
        numb_of_spells -= 1 # This for loop ensures that every spell up to highest has at least one


    for i in range(1, highest_spell_slot + 1):
        ith_weight = highest_spell_slot - i + 1 # Weights are skewed towards the 1st level spells and lower the higher you go
        weights.append(ith_weight)

    selected_numbers = random.choices(range(1, highest_spell_slot + 1), weights=weights, k=numb_of_spells)

    for s in selected_numbers:
        numb_of_spells_per_level[s] += 1

    return numb_of_spells_per_level



def generate_spells(class_type, level, damage_type=None, school=None):

    if not 0 < level < 21:
        raise ValueError("Level must be a valid level (1-20)")
    
    numb_of_cantrips = cantrip_number(class_type, level)

    total_spells = num_of_spells_by_class(class_type, level)

    highest_slot = highest_spell_slot(class_type, level)

    numb_of_spells = generate_numb_spells_per_level(highest_slot, total_spells) # dictionary for amount of spells to generate

    numb_of_spells[0] = numb_of_cantrips #Adding the cantrips to the dictionary

    spells = dict()

    if damage_type == None and school == None: # If there's no theme

        for i in numb_of_spells:
            spells[i] = get_random_spells(class_type, i, numb_of_spells[i])

    else:
        for i in numb_of_spells:
            spells[i] = get_random_themed_spells(class_type, i, numb_of_spells[i], damage_type, school)
    
    return spells


