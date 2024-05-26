# src/arbrynnica/modifier.py
"""This module defines the classes and functions related to modifiers in the RPG.

Typical usage example:

  modifier = Modifier("Strength", 2, "flat", "global")
"""


class Modifier:
    """Represents a modifier in the RPG.

    Attributes:
        name (str): The name of the modifier.
        value (int): The value of the modifier.
        type (str): The type of the modifier (e.g., flat, percentage).
        scope (str): The scope of the modifier (e.g., global, combat).
        duration (int): The duration of the modifier (default is 0 for permanent).
    """
    def __init__(self, name: str, value: int, type: str, scope: str, duration: int = 0) -> None:
        self.name = name
        self.value = value
        self.type = type
        self.scope = scope
        self.duration = duration

    def apply_effect(self, character: 'Character') -> None:
        """Applies the effect of the modifier to the character.

        Args:
            character (Character): The character to apply the modifier to.
        """
        pass  # Implementation for applying effect

    def remove_effect(self, character: 'Character') -> None:
        """Removes the effect of the modifier from the character.

        Args:
            character (Character): The character to remove the modifier from.
        """
        pass  # Implementation for removing effect

    def is_active(self, character: 'Character') -> bool:
        """Checks if the modifier is active on the character.

        Args:
            character (Character): The character to check.

        Returns:
            bool: True if the modifier is active, otherwise False.
        """
        return True  # Implementation for checking if active
