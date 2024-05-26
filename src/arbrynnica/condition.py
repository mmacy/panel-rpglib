# src/arbrynnica/condition.py
"""This module defines the classes and functions related to conditions in the RPG.

Typical usage example:

  condition = Condition("Poisoned", "Reduces health", 3)
"""

class Condition:
    """Represents a condition in the RPG.

    Attributes:
        name (str): The name of the condition.
        description (str): The description of the condition.
        duration (int): The duration of the condition.
    """
    def __init__(self, name: str, description: str, duration: int) -> None:
        self.name = name
        self.description = description
        self.duration = duration

    def apply(self, character: 'Character') -> None:
        """Applies the condition to the character.

        Args:
            character (Character): The character to apply the condition to.
        """
        pass  # Implementation for applying condition

    def remove(self, character: 'Character') -> None:
        """Removes the condition from the character.

        Args:
            character (Character): The character to remove the condition from.
        """
        pass  # Implementation for removing condition
