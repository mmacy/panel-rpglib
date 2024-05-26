# src/arbrynnica/character.py
"""This module defines the classes and functions related to character creation and management in the RPG.

Typical usage example:

  abilities = Abilities(15, 10, 10, 12, 14, 8)
  alignment = Alignment("Lawful")
  char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
  character = Character("Arthas", char_class, abilities, alignment)
"""

from typing import List
from arbrynnica.inventory import Item, Inventory
from arbrynnica.spell import Spell
from arbrynnica.modifier import Modifier
from arbrynnica.condition import Condition

class CharacterClass:
    """Represents a character class in the RPG.

    Attributes:
        name (str): The name of the character class.
        hit_die (int): The hit die associated with the class.
        prime_requisites (List[str]): The prime requisite abilities associated with the class.
        spells (List[Spell]): The spells available to the class.
        equipment (List[Item]): The equipment available to the class.
        skills (List[str]): The skills available to the class.
    """
    def __init__(self, name: str, hit_die: int, prime_requisites: List[str], spells: List[Spell], equipment: List[Item], skills: List[str]) -> None:
        self.name = name
        self.hit_die = hit_die
        self.prime_requisites = prime_requisites
        self.spells = spells
        self.equipment = equipment
        self.skills = skills

    def level_up(self, character: 'Character') -> None:
        """Levels up the character."""
        pass  # Implementation for leveling up

    def apply_class_specific_bonuses(self, character: 'Character') -> None:
        """Applies class-specific bonuses to the character."""
        pass  # Implementation for class-specific bonuses

class Abilities:
    """Represents a character's abilities.

    Attributes:
        strength (int): The strength ability score.
        intelligence (int): The intelligence ability score.
        wisdom (int): The wisdom ability score.
        dexterity (int): The dexterity ability score.
        constitution (int): The constitution ability score.
        charisma (int): The charisma ability score.
    """
    def __init__(self, strength: int, intelligence: int, wisdom: int, dexterity: int, constitution: int, charisma: int) -> None:
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.constitution = constitution
        self.charisma = charisma

    @staticmethod
    def roll_3d6() -> int:
        """Rolls 3 six-sided dice and returns the sum."""
        pass

    @staticmethod
    def roll_4d6_drop_lowest() -> int:
        """Rolls 4 six-sided dice, drops the lowest roll, and returns the sum."""
        pass

class Alignment:
    """Represents a character's alignment.

    Attributes:
        type (str): The alignment type. Options: 'Lawful', 'Neutral', 'Chaotic'.
    """
    def __init__(self, type: str) -> None:
        self.type = type  # Options: 'Lawful', 'Neutral', 'Chaotic'

class Character:
    """Represents a character in the RPG.

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
        self.modifiers: List[Modifier] = []
        self.conditions: List[Condition] = []
        self.hit_points = self.calculate_hit_points()
        self.experience_points = 0
        self.level = 1
        self.inventory = Inventory()
        self.skills: List[str] = char_class.skills

    def calculate_hit_points(self) -> int:
        """Calculates the character's hit points based on class hit die, constitution modifier, and active modifiers.

        Returns:
            int: The calculated hit points.
        """
        base_hp = self.char_class.hit_die + self.get_ability_modifier('constitution')
        active_modifiers = [mod for mod in self.modifiers if mod.is_active(self) and mod.scope == 'global']
        return base_hp + sum(mod.value for mod in active_modifiers if mod.name == 'hit_points')

    def roll_initiative(self) -> int:
        """Rolls for initiative based on the character's dexterity and active modifiers.

        Returns:
            int: The initiative roll result.
        """
        pass

    def get_ability_modifier(self, ability: str) -> int:
        """Gets the modifier for a specified ability.

        Args:
            ability (str): The ability name.

        Returns:
            int: The ability modifier.
        """
        base_modifier = (getattr(self.abilities, ability) - 10) // 2
        active_modifiers = [mod for mod in self.modifiers if mod.is_active(self) and mod.scope in ('global', 'combat')]
        flat_modifiers = sum(mod.value for mod in active_modifiers if mod.name == ability and mod.type == 'flat')
        percentage_modifiers = sum(mod.value for mod in active_modifiers if mod.name == ability and mod.type == 'percentage')
        return self.apply_percentage_modifier(base_modifier + flat_modifiers, percentage_modifiers)

    @staticmethod
    def apply_percentage_modifier(base_value: int, modifier_value: int) -> int:
        """Applies a percentage modifier to a base value.

        Args:
            base_value (int): The base value.
            modifier_value (int): The percentage modifier value.

        Returns:
            int: The modified value.
        """
        return base_value + (base_value * modifier_value // 100)

    def level_up(self) -> None:
        """Levels up the character."""
        self.level += 1
        self.char_class.level_up(self)

    def gain_experience(self, points: int) -> None:
        """Gains experience points and checks for level-up.

        Args:
            points (int): The experience points to gain.
        """
        self.experience_points += points
        while self.check_level_up():
            pass  # Ensure multiple level-ups are handled

    def check_level_up(self) -> bool:
        """Checks if the character can level up.

        Returns:
            bool: True if the character levels up, otherwise False.
        """
        pass

    def equip_item(self, item: Item) -> None:
        """Equips an item and applies its modifiers.

        Args:
            item (Item): The item to equip.
        """
        self.inventory.add_item(item)
        for mod in item.modifiers:
            self.apply_modifier(mod)

    def unequip_item(self, item: Item) -> None:
        """Unequips an item and removes its modifiers.

        Args:
            item (Item): The item to unequip.
        """
        self.inventory.remove_item(item)
        for mod in item.modifiers:
            self.remove_modifier(mod)

    def use_item(self, item: Item) -> None:
        """Uses an item and applies its effects.

        Args:
            item (Item): The item to use.
        """
        item.use(self)

    def learn_spell(self, spell: Spell) -> None:
        """Learns a new spell.

        Args:
            spell (Spell): The spell to learn.
        """
        self.char_class.spells.append(spell)

    def cast_spell(self, spell: Spell, target: 'Character') -> None:
        """Casts a spell on a target character.

        Args:
            spell (Spell): The spell to cast.
            target (Character): The target character.
        """
        spell.cast(self, target)

    def apply_condition(self, condition: Condition) -> None:
        """Applies a condition to the character.

        Args:
            condition (Condition): The condition to apply.
        """
        existing_conditions = [cond for cond in self.conditions if cond.name == condition.name]
        if not existing_conditions:
            self.conditions.append(condition)
            condition.apply(self)

    def remove_condition(self, condition: Condition) -> None:
        """Removes a condition from the character.

        Args:
            condition (Condition): The condition to remove.
        """
        self.conditions = [cond for cond in self.conditions if cond.name != condition.name]
        condition.remove(self)

    def apply_modifier(self, modifier: Modifier) -> None:
        """Applies a modifier to the character.

        Args:
            modifier (Modifier): The modifier to apply.
        """
        self.modifiers.append(modifier)
        modifier.apply_effect(self)
        self.update_attributes()

    def remove_modifier(self, modifier: Modifier) -> None:
        """Removes a modifier from the character.

        Args:
            modifier (Modifier): The modifier to remove.
        """
        self.modifiers.remove(modifier)
        modifier.remove_effect(self)
        self.update_attributes()

    def update_attributes(self) -> None:
        """Recalculates attributes based on current modifiers."""
        self.hit_points = self.calculate_hit_points()
        # Include logic for recalculating other attributes as needed

    def decrement_modifiers(self) -> None:
        """Decrements the duration of active modifiers and removes expired ones."""
        for mod in self.modifiers:
            if mod.duration:
                mod.duration -= 1
                if mod.duration <= 0:
                    self.remove_modifier(mod)
