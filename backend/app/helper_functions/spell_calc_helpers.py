from ..data_access import get_random_spells, get_random_themed_spells
import math

#Some classes have the same number of cantrips at the same levels, thus a function
def cantrip_number(class_type, level):
    type_1 = ['bard', 'druid', 'warlock']
    type_2 = ['cleric', 'wizard']
    type_3 = ['sorceror']
    type_4 = ['paladin', 'ranger']

    #tiers are depending on the level, 1-3 is tier 1, 4-9 is tier 2, 10-20 is tier 3
    if level in range(1,4):
        tier = 1
    elif level in range(4, 10):
        tier = 2
    elif level in range(10, 21):
        tier = 3
    else:
        raise ValueError(f'level {level} is out of range')

    cantrip_number = 0

    if class_type in type_1:
        cantrip_number = tier + 1
    elif class_type in type_2:
        cantrip_number = tier + 2
    elif class_type in type_3:
        cantrip_number = tier + 3
    elif class_type in type_4:
        cantrip_number = 0
    else:
        raise ValueError(f'{class_type} is not a valid class')
    
    return cantrip_number


def highest_spell_slot(class_type, level):
    type_1 = ['bard', 'cleric', 'druid', 'sorceror', 'wizard'] # All share the same spell slot layout (fullcasters)
    type_2 = ['paladin', 'ranger'] # half-casters have a different layout than fullcasters
    type_3 = ['warlock'] # warlock is special

    if class_type in type_1:
        highest_slot = min(math.ceil(level/2), 9) # The formula for fullcasters is ceiling of level div 2 with slots capped at 9
    elif class_type in type_2:
        highest_slot = 0 if level == 1 else min(math.ceil(level/4), 5)   # The formula for halfcasters is ceiling of level div 4 with slots capped at 5
    elif class_type in type_3:
        highest_slot = min(math.ceil(level/2), 5) #same as the fullcaster but just capped at 5th level
    else:
        raise ValueError(f'{class_type} is not a valid class')
    
    return highest_slot

# Now to calculate the # of spells that each class will have in total 9excluding cantrips)

def bard_numb_of_spells(level, ability_modifier):
    bard_spells_known =  {1: 4, 2: 5, 3: 6, 4: 7, 5: 8, 6: 9, 7: 10, 8: 11, 9: 12, 10: 14,
                          11: 15, 12: 15, 13: 16, 14: 18, 15: 19, 16: 19, 17: 20, 18: 22, 19: 22, 20: 22}
    
    return bard_spells_known[level]


# classes that know the whole spell list of their class will get spells equal to the amount able to be prepared (level + spellcast modifier, default 5)

def cleric_numb_of_spells(level, ability_modifier):
    return max(level + ability_modifier, 1)

def druid_numb_of_spells(level, ability_modifier):
    return max(level + ability_modifier, 1)

def paladin_numb_of_spells(level, ability_modifier):
    return 0 if level == 1 else max((level // 2) + ability_modifier, 1)

def ranger_numb_of_spells(level, ability_modifier):
    return 0 if level == 1 else math.ceil(level / 2) + 1

def sorceror_numb_of_spells(level, ability_modifier):
    if level in range(1, 12):
        sorceror_spells_known = level + 1
    elif level in range(17, 21):
        sorceror_spells_known = 15
    else:
        spell_dict = {12: 12, 13: 13, 14: 13, 15: 14, 16: 14}
        sorceror_spells_known = spell_dict[level]
    
    return sorceror_spells_known

def warlock_numb_of_spells(level, ability_modifier):
    if level in range(1, 9):
        return level + 1
    else:
        return math.floor((level-9)/2) + 10 

def wizard_numb_of_spells(level, ability_modifier):
    return (2*(level-1)) + 6


# Now a dispatcher function to call the right one and to clean up code
def num_of_spells_by_class(class_type, level, ability_modifier=5):

    function_name = f"{class_type}_numb_of_spells"

    func_to_call = globals().get(function_name)
    
    return func_to_call(level, ability_modifier)
