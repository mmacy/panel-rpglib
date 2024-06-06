# src/arbrynnica/character.py
"""This module defines the classes and functions related to character creation and management in the RPG.

Characters in the RPG are defined by their class, abilities, alignment, and other attributes. This module provides the structure and behavior for creating and managing characters, including leveling up, applying conditions and modifiers, and interacting with inventory and spells.

Typical usage example:

    ```python
    abilities = Abilities(15, 10, 10, 12, 14, 8)
    alignment = Alignment("Lawful")
    char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
    character = Character("Arthas", char_class, abilities, alignment)
    ```
"""

from typing import List
from arbrynnica.inventory import Item, Inventory
from arbrynnica.spell import Spell
from arbrynnica.modifier import Modifier
from arbrynnica.condition import Condition


class CharacterClass:
    """Represents a character class in the RPG.

    A character class determines the abilities, hit points, and skills of a character. Character classes define the character's role and abilities in the game. Common classes include Fighter, Magic-User, Cleric, and Thief. Each class has unique abilities and hit dice used to determine hit points.

    Attributes:
        name (str): The name of the character class, e.g., 'Fighter', 'Magic-User'.
        hit_die (int): The hit die associated with the class, determining hit points per level.
        prime_requisites (List[str]): The prime requisite abilities associated with the class, influencing experience gain.
        spells (List[Spell]): The spells available to the class, relevant for spellcasting classes.
        equipment (List[Item]): The equipment available to the class.
        skills (List[str]): The skills available to the class.

    Example:
        ```python
        # Creating a character class requires setting up spells, equipment, and skills
        # For brevity, we'll assume spells and equipment are already created.
        fighter_class = CharacterClass(
            "Fighter",
            10,
            ["strength"],
            [],  # Assume no spells for Fighter
            [sword, shield],  # sword and shield are instances of Item
            ["melee combat"]
        )
        ```
    """

    def __init__(
        self,
        name: str,
        hit_die: int,
        prime_requisites: List[str],
        spells: List[Spell],
        equipment: List[Item],
        skills: List[str],
    ) -> None:
        """Initializes a character class.

        Args:
            name (str): The name of the character class.
            hit_die (int): The hit die associated with the class.
            prime_requisites (List[str]): The prime requisite abilities associated with the class.
            spells (List[Spell]): The spells available to the class.
            equipment (List[Item]): The equipment available to the class.
            skills (List[str]): The skills available to the class.

        Example:
            ```python
            fighter_class = CharacterClass("Fighter", 10, ["strength"], [], [], ["melee combat"])
            ```
        """
        self.name = name
        self.hit_die = hit_die
        self.prime_requisites = prime_requisites
        self.spells = spells
        self.equipment = equipment
        self.skills = skills

    def level_up(self, character: "Character") -> None:
        """Levels up the character.

        Call this method when the character has gained enough experience points to reach a new level. This will increase their hit points and potentially grant new abilities or spells.

        Args:
            character (Character): The character to level up.

        Example:
            ```python
            # Assume character has gained enough experience points
            character.gain_experience(500)
            character.level_up()
            character.hit_points = character.calculate_hit_points()
            ```
        """
        pass  # Implementation for leveling up

    def apply_class_specific_bonuses(self, character: "Character") -> None:
        """Applies class-specific bonuses to the character.

        Call this method to apply bonuses specific to the character's class, such as bonus spells or special abilities. This should be done after leveling up or when class-specific conditions are met.

        Args:
            character (Character): The character to apply bonuses to.

        Example:
            ```python
            # After leveling up, apply class-specific bonuses
            character.level_up()
            character.char_class.apply_class_specific_bonuses(character)
            # Update attributes if necessary
            character.update_attributes()
            ```
        """
        pass  # Implementation for class-specific bonuses


class Abilities:
    """Represents a character's abilities, such as strength and intelligence.

    These abilities influence various aspects of gameplay, including combat effectiveness, spellcasting, and skill checks.

    Attributes:
        strength (int): The strength ability score, affecting melee attack and damage rolls.
        intelligence (int): The intelligence ability score, affecting knowledge and spellcasting abilities.
        wisdom (int): The wisdom ability score, affecting perception and willpower.
        dexterity (int): The dexterity ability score, affecting ranged attack rolls and armor class.
        constitution (int): The constitution ability score, affecting hit points and stamina.
        charisma (int): The charisma ability score, affecting social interactions and leadership.

    Example:
        ```python
        abilities = Abilities(15, 10, 10, 12, 14, 8)
        ```
    """

    def __init__(
        self, strength: int, intelligence: int, wisdom: int, dexterity: int, constitution: int, charisma: int
    ) -> None:
        """Initializes a character's abilities with the given scores.

        Ability scores typically range from 3 to 18, as determined by rolling 3d6 for each ability, according to the game mechanics.

        Args:
            strength (int): The strength ability score.
            intelligence (int): The intelligence ability score.
            wisdom (int): The wisdom ability score.
            dexterity (int): The dexterity ability score.
            constitution (int): The constitution ability score.
            charisma (int): The charisma ability score.

        Example:
            ```python
            abilities = Abilities(15, 10, 10, 12, 14, 8)
            ```
        """
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.dexterity = dexterity
        self.constitution = constitution
        self.charisma = charisma

    @staticmethod
    def roll_3d6() -> int:
        """Rolls 3 six-sided dice and returns the sum.

        Use this method to generate a random ability score.

        Returns:
            int: The sum of the rolls.

        Example:
            ```python
            strength = Abilities.roll_3d6()
            ```
        """
        pass

    @staticmethod
    def roll_4d6_drop_lowest() -> int:
        """Rolls 4 six-sided dice, drops the lowest roll, and returns the sum.

        Use this method to generate a higher average ability score by discarding the lowest roll.

        Returns:
            int: The sum of the highest three rolls.

        Example:
            ```python
            strength = Abilities.roll_4d6_drop_lowest()
            ```
        """
        pass


class Alignment:
    """Represents a character's alignment.

    Alignment is simplified into three categories: Lawful, Neutral, and Chaotic. Each alignment represents a different moral and ethical outlook that can affect how characters interact with the game world and its inhabitants.

    Attributes:
        type (str): The alignment type. Options: 'Lawful', 'Neutral', 'Chaotic'.

    Example:
        ```python
        alignment = Alignment("Lawful")
        ```
    """

    def __init__(self, type: str) -> None:
        """Initializes a character's alignment.

        Args:
            type (str): The alignment of the character. Options: 'Lawful', 'Neutral', 'Chaotic'.
        """
        self.type = type


class Character:
    """Represents a character in the RPG.

    This class manages all aspects of a character, including their attributes, conditions, and modifiers, according to the game mechanics.

    Attributes:
        name (str): The name of the character.
        char_class (CharacterClass): The character's class, which defines their role and abilities.
        abilities (Abilities): The character's abilities, which affect various aspects of gameplay.
        alignment (Alignment): The character's alignment, influencing their moral decisions and interactions.
        hit_points (int): The character's hit points.
        experience_points (int): The character's experience points.
        level (int): The character's level.
        inventory (Inventory): The character's inventory.
        skills (List[str]): The character's skills.
        conditions (List[Condition]): The conditions affecting the character.
        modifiers (List[Modifier]): The modifiers affecting the character.

    Example:
        ```python
        # Creating a character involves setting up abilities, alignment, and character class
        abilities = Abilities(15, 10, 10, 12, 14, 8)
        alignment = Alignment("Lawful")
        char_class = CharacterClass("Fighter", 10, ["strength"], [], [], ["melee combat"])
        character = Character("Arthas", char_class, abilities, alignment)
        ```
    """

    def __init__(self, name: str, char_class: CharacterClass, abilities: Abilities, alignment: Alignment) -> None:
        """Initializes a player character with the given name, class, abilities, and alignment.

        Args:
            name (str): The name of the character.
            char_class (CharacterClass): The character's class.
            abilities (Abilities): The character's abilities.
            alignment (Alignment): The character's alignment.

        Example:
            ```python
            abilities = Abilities(15, 10, 10, 12, 14, 8)
            alignment = Alignment("Lawful")
            char_class = CharacterClass("Fighter", 10, ["strength"], [], [], ["melee combat"])
            character = Character("Arthas", char_class, abilities, alignment)
            ```
        """
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

        Call this method when initializing a character or after leveling up to determine the character's current hit points.

        Returns:
            int: The calculated hit points.

        Example:
            ```python
            character.hit_points = character.calculate_hit_points()
            ```
        """
        base_hp = self.char_class.hit_die + self.get_ability_modifier("constitution")
        active_modifiers = [mod for mod in self.modifiers if mod.is_active(self) and mod.scope == "global"]
        return base_hp + sum(mod.value for mod in active_modifiers if mod.name == "hit_points")

    def roll_initiative(self) -> int:
        """Rolls for initiative based on the character's dexterity and active modifiers.

        Call this method at the start of combat to determine the character's order in the initiative.

        Returns:
            int: The initiative roll result.

        Example:
            ```python
            initiative = character.roll_initiative()
            ```
        """
        pass

    def get_ability_modifier(self, ability: str) -> int:
        """Gets the modifier for a specified ability.

        Args:
            ability (str): The ability name.

        Returns:
            int: The ability modifier.

        Example:
            ```python
            strength_modifier = character.get_ability_modifier('strength')
            ```
        """
        base_modifier = (getattr(self.abilities, ability) - 10) // 2
        active_modifiers = [mod for mod in self.modifiers if mod.is_active(self) and mod.scope in ("global", "combat")]
        flat_modifiers = sum(mod.value for mod in active_modifiers if mod.name == ability and mod.type == "flat")
        percentage_modifiers = sum(
            mod.value for mod in active_modifiers if mod.name == ability and mod.type == "percentage"
        )
        return self.apply_percentage_modifier(base_modifier + flat_modifiers, percentage_modifiers)

    @staticmethod
    def apply_percentage_modifier(base_value: int, modifier_value: int) -> int:
        """Applies a percentage modifier to a base value.

        Args:
            base_value (int): The base value.
            modifier_value (int): The percentage modifier value.

        Returns:
            int: The modified value.

        Example:
            ```python
            adjusted_value = Character.apply_percentage_modifier(10, 20)
            ```
        """
        return base_value + (base_value * modifier_value // 100)

    def level_up(self) -> None:
        """Levels up the character.

        Call this method to increase the character's level, hit points, and potentially grant new abilities or spells. This should be called after gaining sufficient experience points.

        Example:
            ```python
            character.gain_experience(500)
            character.level_up()
            character.char_class.apply_class_specific_bonuses(character)
            character.update_attributes()
            ```
        """
        self.level += 1
        self.char_class.level_up(self)

    def gain_experience(self, points: int) -> None:
        """Gains experience points and checks for level-up.

        Call this method to add experience points to the character. If the character gains enough experience points, they will level up.

        Args:
            points (int): The experience points to gain.

        Example:
            ```python
            character.gain_experience(500)
            while character.check_level_up():
                character.level_up()
            ```
        """
        self.experience_points += points
        while self.check_level_up():
            pass  # Ensure multiple level-ups are handled

    def check_level_up(self) -> bool:
        """Checks if the character can level up.

        Call this method to verify if the character has enough experience points to level up. If so, the character levels up.

        Returns:
            bool: True if the character levels up, otherwise False.

        Example:
            ```python
            if character.check_level_up():
                character.level_up()
            ```
        """
        pass

    def equip_item(self, item: Item) -> None:
        """Equips an item and applies its modifiers.

        Call this method to equip an item and apply its modifiers to the character's attributes.

        Args:
            item (Item): The item to equip.

        Example:
            ```python
            character.equip_item(sword)
            character.update_attributes()
            ```
        """
        self.inventory.add_item(item)
        for mod in item.modifiers:
            self.apply_modifier(mod)

    def unequip_item(self, item: Item) -> None:
        """Unequips an item and removes its modifiers.

        Call this method to unequip an item and remove its modifiers from the character's attributes.

        Args:
            item (Item): The item to unequip.

        Example:
            ```python
            character.unequip_item(sword)
            character.update_attributes()
            ```
        """
        self.inventory.remove_item(item)
        for mod in item.modifiers:
            self.remove_modifier(mod)

    def use_item(self, item: Item) -> None:
        """Uses an item and applies its effects.

        Call this method to use an item, such as a potion, and apply its effects to the character.

        Args:
            item (Item): The item to use.

        Example:
            ```python
            character.use_item(health_potion)
            character.update_attributes()
            ```
        """
        item.use(self)

    def learn_spell(self, spell: Spell) -> None:
        """Learns a new spell.

        Call this method to add a new spell to the character's spell list.

        Args:
            spell (Spell): The spell to learn.

        Example:
            ```python
            character.learn_spell(fireball)
            character.update_attributes()
            ```
        """
        self.char_class.spells.append(spell)

    def cast_spell(self, spell: Spell, target: "Character") -> None:
        """Casts a spell on a target character.

        Call this method to cast a spell, targeting another character.

        Args:
            spell (Spell): The spell to cast.
            target (Character): The target character.

        Example:
            ```python
            character.cast_spell(fireball, target_character)
            character.update_attributes()
            ```
        """
        spell.cast(self, target)

    def apply_condition(self, condition: Condition) -> None:
        """Applies a condition to the character.

        Call this method to apply a condition, such as poisoned or stunned, to the character.

        Args:
            condition (Condition): The condition to apply.

        Example:
            ```python
            character.apply_condition(poisoned_condition)
            character.update_attributes()
            ```
        """
        existing_conditions = [cond for cond in self.conditions if cond.name == condition.name]
        if not existing_conditions:
            self.conditions.append(condition)
            condition.apply(self)

    def remove_condition(self, condition: Condition) -> None:
        """Removes a condition from the character.

        Call this method to remove a condition from the character.

        Args:
            condition (Condition): The condition to remove.

        Example:
            ```python
            character.remove_condition(poisoned_condition)
            character.update_attributes()
            ```
        """
        self.conditions = [cond for cond in self.conditions if cond.name != condition.name]
        condition.remove(self)

    def apply_modifier(self, modifier: Modifier) -> None:
        """Applies a modifier to the character.

        Call this method to apply a modifier, such as a strength boost, to the character's attributes.

        Args:
            modifier (Modifier): The modifier to apply.

        Example:
            ```python
            character.apply_modifier(strength_boost)
            character.update_attributes()
            ```
        """
        self.modifiers.append(modifier)
        modifier.apply_effect(self)
        self.update_attributes()

    def remove_modifier(self, modifier: Modifier) -> None:
        """Removes a modifier from the character.

        Call this method to remove a modifier from the character's attributes.

        Args:
            modifier (Modifier): The modifier to remove.

        Example:
            ```python
            character.remove_modifier(strength_boost)
            character.update_attributes()
            ```
        """
        self.modifiers.remove(modifier)
        modifier.remove_effect(self)
        self.update_attributes()

    def update_attributes(self) -> None:
        """Recalculates attributes based on current modifiers.

        Call this method to update the character's attributes, such as hit points, after applying or removing modifiers.

        Example:
            ```python
            character.update_attributes()
            ```
        """
        self.hit_points = self.calculate_hit_points()
        # Include logic for recalculating other attributes as needed

    def decrement_modifiers(self) -> None:
        """Decrements the duration of active modifiers and removes expired ones.

        Call this method at the end of each turn to decrement the duration of active modifiers and remove those that have expired.

        Example:
            ```python
            character.decrement_modifiers()
            character.update_attributes()
            ```
        """
        for mod in self.modifiers:
            if mod.duration:
                mod.duration -= 1
                if mod.duration <= 0:
                    self.remove_modifier(mod)
