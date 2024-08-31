from ..data_access import get_random_spells, get_random_themed_spells

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
