# src/arbrynnica/spell.py
"""This module defines the classes and functions related to spells in the RPG.

Spells represent magical abilities that characters can use during the game. Each spell has a name, level, and effect.

Typical usage example:

    ```python
    def fireball_effect(caster, target):
        # Implementation of the fireball effect
        target.hit_points -= 10

    spell = Spell("Fireball", 3, fireball_effect)
    caster = Character("Mage", magic_user_class, abilities, alignment)
    target = Character("Goblin", fighter_class, abilities, alignment)
    spell.cast(caster, target)
    ```
"""

from typing import Callable

class Spell:
    """Represents a spell in the RPG.

    Spells are magical abilities that characters can cast on targets, causing various effects.

    Attributes:
        name (str): The name of the spell.
        level (int): The level of the spell.
        effect (Callable): The effect of the spell, a function that defines what happens when the spell is cast.

    Example:
        ```python
        # Define a spell effect
        def fireball_effect(caster, target):
            target.hit_points -= 10

        # Create a spell
        fireball = Spell("Fireball", 3, fireball_effect)
        ```
    """
    def __init__(self, name: str, level: int, effect: Callable) -> None:
        """Initializes a spell.

        Args:
            name (str): The name of the spell.
            level (int): The level of the spell.
            effect (Callable): The effect of the spell, a function that defines what happens when the spell is cast.

        Example:
            ```python
            def fireball_effect(caster, target):
                target.hit_points -= 10

            fireball = Spell("Fireball", 3, fireball_effect)
            ```
        """
        self.name = name
        self.level = level
        self.effect = effect

    def cast(self, caster: 'Character', target: 'Character') -> None:
        """Casts the spell on a target character.

        Call this method to cast the spell from the caster to the target, applying the spell's effect.

        Args:
            caster (Character): The character casting the spell.
            target (Character): The target character.

        Example:
            ```python
            # Define the caster and target characters
            caster = Character("Mage", magic_user_class, abilities, alignment)
            target = Character("Goblin", fighter_class, abilities, alignment)

            # Define a spell effect
            def fireball_effect(caster, target):
                target.hit_points -= 10

            # Create and cast the spell
            fireball = Spell("Fireball", 3, fireball_effect)
            fireball.cast(caster, target)
            ```
        """
        self.effect(caster, target)
