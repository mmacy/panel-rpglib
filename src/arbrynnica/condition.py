# src/arbrynnica/condition.py
"""This module defines the classes and functions related to conditions in the RPG.

Conditions represent various states that can affect a character's abilities, actions, and overall gameplay. Conditions can be beneficial or detrimental and have a specific duration.

Typical usage example:

  condition = Condition("Poisoned", "Reduces health over time", 3)
"""

class Condition:
    """Represents a condition in the RPG.

    Conditions affect a character's abilities, actions, and overall gameplay. They can be applied to or removed from characters and have a specific duration.

    Attributes:
        name (str): The name of the condition.
        description (str): The description of the condition.
        duration (int): The duration of the condition in turns.

    Usage:
        - To create a condition, instantiate the Condition class with a name, description, and duration.
        - Apply the condition to a character using the `apply` method. This will impose the condition's effects on the character.
        - Remove the condition from a character using the `remove` method. This will revert any changes made by the condition.
        - Decrement the condition's duration at the end of each turn using the `tick` method. When the duration reaches zero, remove the condition.

    Example:
        ```python
        poisoned_condition = Condition("Poisoned", "Reduces health over time", 3)
        character.add_condition(poisoned_condition)
        poisoned_condition.apply(character)
        ```
    """
    def __init__(self, name: str, description: str, duration: int) -> None:
        """Initializes a condition.

        Args:
            name (str): The name of the condition.
            description (str): The description of the condition.
            duration (int): The duration of the condition in turns.

        Example:
            ```python
            poisoned_condition = Condition("Poisoned", "Reduces health over time", 3)
            ```
        """
        self.name = name
        self.description = description
        self.duration = duration

    def apply(self, character: 'Character') -> None:
        """Applies the condition to the character.

        Call this method to impose the condition's effects on the character. This method should be used in conjunction with character state updates.

        Args:
            character (Character): The character to apply the condition to.

        Example:
            ```python
            poisoned_condition.apply(character)
            ```
        """
        # Example implementation for applying condition effects
        if self.name == "Poisoned":
            character.hit_points -= 1  # Example effect: Reduce health by 1

    def remove(self, character: 'Character') -> None:
        """Removes the condition from the character.

        Call this method to remove the condition's effects from the character. This method should be used to revert any changes made by the condition.

        Args:
            character (Character): The character to remove the condition from.

        Example:
            ```python
            poisoned_condition.remove(character)
            ```
        """
        # Example implementation for removing condition effects
        if self.name == "Poisoned":
            character.hit_points += 1  # Example effect: Restore health by 1

    def tick(self) -> None:
        """Decrements the duration of the condition.

        Call this method at the end of each turn to decrease the remaining duration of the condition. When the duration reaches zero, the condition should be removed.

        Example:
            ```python
            poisoned_condition.tick()
            if poisoned_condition.duration <= 0:
                character.remove_condition(poisoned_condition)
            ```
        """
        self.duration -= 1
