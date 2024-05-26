# src/arbrynnica/spell.py
"""This module defines the classes and functions related to spells in the RPG.

Typical usage example:

  spell = Spell("Fireball", 3, effect)
"""

from typing import Callable

class Spell:
    """Represents a spell in the RPG.

    Attributes:
        name (str): The name of the spell.
        level (int): The level of the spell.
        effect (Callable): The effect of the spell.
    """
    def __init__(self, name: str, level: int, effect: Callable) -> None:
        self.name = name
        self.level = level
        self.effect = effect

    def cast(self, caster: 'Character', target: 'Character') -> None:
        """Casts the spell on a target character.

        Args:
            caster (Character): The character casting the spell.
            target (Character): The target character.

        Example:
            fireball = Spell("Fireball", 3, fireball_effect)
            fireball.cast(caster, target)
        """
        self.effect(caster, target)
