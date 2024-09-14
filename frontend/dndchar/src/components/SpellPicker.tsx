import React, { useState } from "react";

const SpellPickerForm:  React.FC = () => {
  const [spellPickerData, setSpellPickerData] = useState({
    class_type: "",
    level: "",
    school: "",
    damage_type: "",
  });
  const [errors, setErrors] = useState<{ [key: string]: string }>({})
  const [spells, setSpells] = useState(null);
  const [submitted, setSubmitted] = useState(false); // To track if the form was submitted

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement | HTMLInputElement>) => {
    setSpellPickerData({ ...spellPickerData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    let validationErrors:{ [key: string]: string } = {};

    if (!spellPickerData.class_type) {
        validationErrors.class_type = "Class is required"
    }
    if (!spellPickerData.level) {
        validationErrors.level = "Level is required"
    }

    // validate level input (must be between 1 and 20)
    const numberValue = parseInt(spellPickerData.level, 10);
    if (numberValue < 1 || numberValue > 20 || isNaN(numberValue)) {
      validationErrors.level = "Please enter a number between 1 and 20.";
    }

    // If any validation errors, prevent submission and show errors   
    if (Object.keys(validationErrors).length > 0) {
        setErrors(validationErrors);
        return;
    }
    
    // Clear errors
    setErrors({});


    const response = await fetch("http://localhost:5000/spell-picker/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(spellPickerData),
    });

    if (response.ok) {
      const data = await response.json();
      // Redirect to the new page with data
      setSpells(data)
      setSubmitted(true)
    }
  };

  return (
    <div>
        <form onSubmit={handleSubmit}>
            <select name="class_type" value={spellPickerData.class_type} onChange={handleChange}>
                <option value="">Select Class</option>
                <option value="bard">Bard</option>
                <option value="cleric">Cleric</option>
                <option value="druid">Druid</option>
                <option value="paladin">Paladin</option>
                <option value="ranger">Ranger</option>
                <option value="sorceror">Sorcerer</option>
                <option value="warlock">Warlock</option>
                <option value="wizard">Wizard</option>
            </select>
            {errors.class_type && <p style={{ color: "red" }}>{errors.class_type}</p>}

            <input
                type="number" 
                name="level" 
                value={spellPickerData.level} 
                onChange={handleChange} 
                placeholder="Enter a number (1-20)"
            />
            {errors.level && <p style={{ color: "red" }}>{errors.level}</p>}

            <select name="school" value={spellPickerData.school} onChange={handleChange}>
                <option value="">Filter by School of Magic *Optional*</option>
                <option value="abjuration">Abjuration</option>
                <option value="conjuration">Conjuration</option>
                <option value="divination">Divination</option>
                <option value="enchantment">Enchantment</option>
                <option value="evocation">Evocation</option>
                <option value="illusion">Illusion</option>
                <option value="necromancy">Necromancy</option>
                <option value="transmutation">Transmutation</option>
            </select>

            <select name="damage_type" value={spellPickerData.damage_type} onChange={handleChange}>
                <option value="">Filter by Damage Type *Optional*</option>
                <option value="acid">Acid</option>
                <option value="bludgeoning">Bludgeoning</option>
                <option value="cold">Cold</option>
                <option value="fire">Fire</option>
                <option value="force">Force</option>
                <option value="lightning">Lightning</option>
                <option value="necrotic">Necrotic</option>
                <option value="piercing">Piercing</option>
                <option value="poison">Poison</option>
                <option value="psychic">Psychic</option>
                <option value="radiant">Radiant</option>
                <option value="slashing">Slashing</option>
                <option value="thunder">Thunder</option>
            </select>

            <button type="submit">Submit</button>
        </form>

        {submitted && spells && (
            <div>
                <p>{spells}</p>
            </div>
        )}
    </div>
  );
};

export default SpellPickerForm;
