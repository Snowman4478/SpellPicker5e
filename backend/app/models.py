from app import db

class Spell(db.Model):

    spell_name = db.Column(db.String(100), primary_key=True, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    school = db.Column(db.String(50), nullable=False)
    ritual = db.Column(db.Boolean, default=False)
    casting_time = db.Column(db.String(50), nullable=False)
    range = db.Column(db.String(50), nullable=False)
    target_area = db.Column(db.String(100))
    v = db.Column(db.Boolean, default=False)  # Verbal Component
    s = db.Column(db.Boolean, default=False)  # Somatic Component
    m = db.Column(db.Boolean, default=False)  # Material Component
    components = db.Column(db.String(100))
    cost = db.Column(db.Integer, nullable=True)
    concentration = db.Column(db.Boolean, default=False)
    duration = db.Column(db.String(50), nullable=False)
    attack_saving_throw_effect = db.Column(db.String(100))
    damage_type = db.Column(db.String(50))
    damage_heal = db.Column(db.String(50))
    sourcebook = db.Column(db.String(100), nullable=False)
    page_number = db.Column(db.Integer, nullable=False)
    additional_detail = db.Column(db.Text, nullable=True)
    per_higher_spell_level = db.Column(db.String(100))
    bard = db.Column(db.Boolean, default=False)
    cleric = db.Column(db.Boolean, default=False)
    druid = db.Column(db.Boolean, default=False)
    paladin = db.Column(db.Boolean, default=False)
    ranger = db.Column(db.Boolean, default=False)
    sorceror = db.Column(db.Boolean, default=False)
    warlock = db.Column(db.Boolean, default=False)
    wizard = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Spell {self.spell_name}>'
    
    def to_dict(self):
        return {
            "spell_name": self.spell_name,
            "level": self.level,
            "school": self.school,
            "ritual": self.ritual,
            "casting_time": self.casting_time,
            "range": self.range,
            "target_area": self.target_area,
            "v": self.v,
            "s": self.s,
            "m": self.m,
            "components": self.components,
            "cost": self.cost,
            "concentration": self.concentration,
            "duration": self.duration,
            "attack_saving_throw_effect": self.attack_saving_throw_effect,
            "damage_type": self.damage_type,
            "damage_heal": self.damage_heal,
            "sourcebook": self.sourcebook,
            "page_number": self.page_number,
            "additional_detail": self.additional_detail,
            "per_higher_spell_level": self.per_higher_spell_level,
            "bard": self.bard,
            "cleric": self.cleric,
            "druid": self.druid,
            "paladin": self.paladin,
            "ranger": self.ranger,
            "sorceror": self.sorceror,
            "warlock": self.warlock,
            "wizard": self.wizard
        }