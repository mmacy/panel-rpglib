"""
src/arbrynnica/character.py
"""

from typing import Dict, List, Optional
from arbrynnica.inventory import Item, Inventory
from arbrynnica.spell import Spell
from arbrynnica.modifier import Modifier
from arbrynnica.condition import Condition

class CharacterClass:
    def __init__(self, name: str, hit_die: int, abilities: List[str], spells: List[Spell], equipment: List[Item], skills: List[str]) -> None:
        self.name = name
        self.hit_die = hit_die
        self.abilities = abilities
        self.spells = spells
        self.equipment = equipment
        self.skills = skills

    def level_up(self, character: 'Character') -> None:
        pass  # Implementation for leveling up

    def apply_class_specific_bonuses(self, character: 'Character') -> None:
        pass  # Implementation for class-specific bonuses

class Abilities:
    def __init__(self, strength: int, intelligence: int, wisdom: int, dexterity: int, constitution: int, charisma: int) -> None:
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.constitution = constitution
        self.charisma = charisma

    @staticmethod
    def roll_3d6() -> int:
        # Implementation for rolling 3d6
        pass

    @staticmethod
    def roll_4d6_drop_lowest() -> int:
        # Implementation for rolling 4d6 and dropping the lowest
        pass

class Alignment:
    def __init__(self, type: str) -> None:
        self.type = type  # Options: 'Lawful', 'Neutral', 'Chaotic'

class Character:
    """
    Represents a character in the RPG.

    Attributes:
        name (str): The name of the character.
        char_class (CharacterClass): The character's class.
        abilities (Abilities): The character's abilities.
        alignment (Alignment): The character's alignment.
        hit_points (int): The character's hit points.
        experience_points (int): The character's experience points.
        level (int): The character's level.
        inventory (Inventory): The character's inventory.
        skills (List[str]): The character's skills.
        conditions (List[Condition]): The conditions affecting the character.
        modifiers (List[Modifier]): The modifiers affecting the character.
    """
    def __init__(self, name: str, char_class: CharacterClass, abilities: Abilities, alignment: Alignment) -> None:
        self.name = name
        self.char_class = char_class
        self.abilities = abilities
        self.alignment = alignment
        self.hit_points = self.calculate_hit_points()
        self.experience_points = 0
        self.level = 1
        self.inventory = Inventory()
        self.skills: List[str] = char_class.skills
        self.conditions: List[Condition] = []
        self.modifiers: List[Modifier] = []

    def calculate_hit_points(self) -> int:
        base_hp = self.char_class.hit_die + self.get_ability_modifier('constitution')
        active_modifiers = [mod for mod in self.modifiers if mod.is_active(self) and mod.scope == 'global']
        return base_hp + sum(mod.value for mod in active_modifiers if mod.name == 'hit_points')

    def roll_initiative(self) -> int:
        # Implementation for rolling initiative
        pass

    def get_ability_modifier(self, ability: str) -> int:
        base_modifier = (getattr(self.abilities, ability) - 10) // 2
        active_modifiers = [mod for mod in self.modifiers if mod.is_active(self) and mod.scope in ('global', 'combat')]
        flat_modifiers = sum(mod.value for mod in active_modifiers if mod.name == ability and mod.type == 'flat')
        percentage_modifiers = sum(mod.value for mod in active_modifiers if mod.name == ability and mod.type == 'percentage')
        return self.apply_percentage_modifier(base_modifier + flat_modifiers, percentage_modifiers)

    @staticmethod
    def apply_percentage_modifier(base_value: int, modifier_value: int) -> int:
        return base_value + (base_value * modifier_value // 100)

    def level_up(self) -> None:
        self.level += 1
        self.char_class.level_up(self)

    def gain_experience(self, points: int) -> None:
        self.experience_points += points
        while self.check_level_up():
            pass  # Ensure multiple level-ups are handled

    def check_level_up(self) -> bool:
        # Implementation for checking if character can level up
        pass

    def equip_item(self, item: Item) -> None:
        self.inventory.add_item(item)
        for mod in item.modifiers:
            self.apply_modifier(mod)

    def unequip_item(self, item: Item) -> None:
        self.inventory.remove_item(item)
        for mod in item.modifiers:
            self.remove_modifier(mod)

    def use_item(self, item: Item) -> None:
        item.use(self)

    def learn_spell(self, spell: Spell) -> None:
        self.char_class.spells.append(spell)

    def cast_spell(self, spell: Spell, target: 'Character') -> None:
        spell.cast(self, target)

    def apply_condition(self, condition: Condition) -> None:
        existing_conditions = [cond for cond in self.conditions if cond.name == condition.name]
        if not existing_conditions:
            self.conditions.append(condition)
            condition.apply(self)

    def remove_condition(self, condition: Condition) -> None:
        self.conditions = [cond for cond in self.conditions if cond.name != condition.name]
        condition.remove(self)

    def apply_modifier(self, modifier: Modifier) -> None:
        self.modifiers.append(modifier)
        modifier.apply_effect(self)
        self.update_attributes()

    def remove_modifier(self, modifier: Modifier) -> None:
        self.modifiers.remove(modifier)
        modifier.remove_effect(self)
        self.update_attributes()

    def update_attributes(self) -> None:
        # Recalculate attributes based on current modifiers
        self.hit_points = self.calculate_hit_points()
        # Include logic for recalculating other attributes as needed

    def decrement_modifiers(self) -> None:
        for mod in self.modifiers:
            if mod.duration:
                mod.duration -= 1
                if mod.duration <= 0:
                    self.remove_modifier(mod)
