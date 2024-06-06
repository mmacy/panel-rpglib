# src/arbrynnica/modifier.py
"""This module defines the classes and functions related to modifiers in the RPG.

Modifiers provide temporary or permanent changes to a character's attributes or abilities, influencing gameplay in various ways.

Typical usage example:

    ```python
    modifier = Modifier("Strength", 2, "flat", "global")
    ```
"""


class Modifier:
    """Represents a modifier in the RPG.

    Modifiers can alter a character's attributes or abilities, either temporarily or permanently, and can have various scopes and types.

    Attributes:
        name (str): The name of the modifier.
        value (int): The value of the modifier.
        type (str): The type of the modifier (e.g., flat, percentage).
        scope (str): The scope of the modifier (e.g., global, combat).
        duration (int): The duration of the modifier in turns (default is 0 for permanent).

    Example:
        ```python
        # Creating a modifier
        strength_modifier = Modifier("Strength", 2, "flat", "global")
        ```
    """

    def __init__(self, name: str, value: int, type: str, scope: str, duration: int = 0) -> None:
        """Initializes a modifier.

        Args:
            name (str): The name of the modifier.
            value (int): The value of the modifier.
            type (str): The type of the modifier (e.g., flat, percentage).
            scope (str): The scope of the modifier (e.g., global, combat).
            duration (int): The duration of the modifier in turns (default is 0 for permanent).

        Example:
            ```python
            strength_modifier = Modifier("Strength", 2, "flat", "global", 5)
            ```
        """
        self.name = name
        self.value = value
        self.type = type
        self.scope = scope
        self.duration = duration

    def apply_effect(self, character: "Character") -> None:
        """Applies the effect of the modifier to the character.

        Call this method to apply the modifier's effect to the character's attributes or abilities.

        Args:
            character (Character): The character to apply the modifier to.

        Example:
            ```python
            strength_modifier.apply_effect(character)
            character.update_attributes()
            ```
        """
        pass  # Implementation for applying effect

    def remove_effect(self, character: "Character") -> None:
        """Removes the effect of the modifier from the character.

        Call this method to remove the modifier's effect from the character's attributes or abilities.

        Args:
            character (Character): The character to remove the modifier from.

        Example:
            ```python
            strength_modifier.remove_effect(character)
            character.update_attributes()
            ```
        """
        pass  # Implementation for removing effect

    def is_active(self, character: "Character") -> bool:
        """Checks if the modifier is active on the character.

        Call this method to check if the modifier is still active on the character.

        Args:
            character (Character): The character to check.

        Returns:
            bool: True if the modifier is active, otherwise False.

        Example:
            ```python
            if strength_modifier.is_active(character):
                print("Modifier is active")
            ```
        """
        return True  # Implementation for checking if active
