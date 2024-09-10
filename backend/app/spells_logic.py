from .helper_functions.spell_calc_helpers import num_of_spells_by_class, cantrip_number, highest_spell_slot
from .data_access import get_random_spells, get_random_themed_spells


print(get_random_themed_spells('druid', 3, 3, damage_type='Lightning', school='Conjuration'))