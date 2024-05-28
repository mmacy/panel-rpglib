# src/arbrynnica/utils/dice_roller.py
"""This module defines the classes and functions related to dice rolling in the RPG.

Dice rolling is a fundamental mechanic in many RPGs, used to determine the outcome of various actions and events. This module provides utility functions for rolling dice, including support for standard dice notation and optional rules such as dropping the lowest roll.

Typical usage example:

    ```python
    result = DiceRoller.roll(3, 6)
    print(result)

    result = DiceRoller.roll('3d6')
    print(result)

    result = DiceRoller.roll('4d6', drop_lowest=True)
    print(result)
    ```
"""

import random
from typing import Optional, Union

class _DiceRollConfig:
    """Configuration class for dice rolling.

    This class holds the configuration for a dice roll, including the number of dice, the number of sides on each die, and whether to drop the lowest roll.

    Attributes:
        num_dice (int): Number of dice to roll.
        num_sides (int): Number of sides on each die.
        drop_lowest (bool): Whether to drop the lowest roll. Defaults to False.

    Example:
        ```python
        config = _DiceRollConfig(3, 6, drop_lowest=True)
        result = DiceRoller.roll(config.num_dice, config.num_sides, config.drop_lowest)
        print(result)  # Example output: 14 (actual result will vary)
        ```
    """
    def __init__(self, num_dice: int, num_sides: int, drop_lowest: bool = False) -> None:
        """Initializes the dice roll configuration.

        Args:
            num_dice (int): Number of dice to roll.
            num_sides (int): Number of sides on each die.
            drop_lowest (bool): Whether to drop the lowest roll. Defaults to False.

        Example:
            ```python
            config = _DiceRollConfig(3, 6, drop_lowest=True)
            result = DiceRoller.roll(config.num_dice, config.num_sides, config.drop_lowest)
            print(result)  # Example output: 14 (actual result will vary)
            ```
        """
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.drop_lowest = drop_lowest

class DiceRoller:
    """Utility class for rolling dice.

    This class provides methods for rolling dice, including support for dice notation (e.g., '3d6') and optional rules such as dropping the lowest roll.

    Example:
        ```python
        result = DiceRoller.roll(3, 6)
        print(result)
        ```
    """

    @staticmethod
    def roll(num_dice: Union[int, str], num_sides: Optional[int] = None, drop_lowest: bool = False) -> int:
        """Rolls a specified number of dice with a given number of sides.

        Args:
            num_dice (Union[int, str]): Number of dice to roll or dice notation (e.g., '3d6').
            num_sides (Optional[int]): Number of sides on each die. Required if num_dice is an int.
            drop_lowest (bool): Whether to drop the lowest roll. Defaults to False.

        Returns:
            int: Sum of the dice rolls based on the provided configuration.

        Raises:
            ValueError: If num_dice or num_sides is less than 1, or if the notation is not supported.

        Examples:
            ```python
            # Roll 3 six-sided dice
            result = DiceRoller.roll(3, 6)
            print(result)  # Example output: 10 (actual result will vary)

            # Roll using dice notation
            result = DiceRoller.roll('3d6')
            print(result)  # Example output: 12 (actual result will vary)

            # Roll with the lowest die dropped
            result = DiceRoller.roll('4d6', drop_lowest=True)
            print(result)  # Example output: 14 (actual result will vary)
            ```
        """
        if isinstance(num_dice, str):
            config = DiceRoller._parse_dice_notation(num_dice, drop_lowest)
            return DiceRoller.roll(config.num_dice, config.num_sides, config.drop_lowest)

        if num_dice < 1 or num_sides is None or num_sides < 1:
            raise ValueError("Number of dice and sides must be at least 1.")

        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        if drop_lowest:
            return sum(sorted(rolls)[1:])
        return sum(rolls)

    @staticmethod
    def _parse_dice_notation(dice_notation: str, drop_lowest: bool = False) -> _DiceRollConfig:
        """Parses a dice notation string and returns a configuration object.

        Args:
            dice_notation (str): String describing the dice roll format (e.g., '3d6').
            drop_lowest (bool): Whether to drop the lowest roll. Defaults to False.

        Returns:
            _DiceRollConfig: Configuration object based on the provided notation.

        Raises:
            ValueError: If the notation is not in the supported format.

        Example:
            ```python
            config = DiceRoller._parse_dice_notation('3d6', drop_lowest=True)
            result = DiceRoller.roll(config.num_dice, config.num_sides, config.drop_lowest)
            print(result)  # Example output: 14 (actual result will vary)
            ```
        """
        try:
            num_dice, num_sides = map(int, dice_notation.split('d'))
        except ValueError:
            raise ValueError("Unsupported dice notation format.")

        return _DiceRollConfig(num_dice=num_dice, num_sides=num_sides, drop_lowest=drop_lowest)
