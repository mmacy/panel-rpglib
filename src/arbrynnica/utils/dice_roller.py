# src/arbrynnica/utils/dice_roller.py

import random
from typing import Optional, Union

class DiceRollConfig:
    """Configuration class for dice rolling."""
    def __init__(self, num_dice: int, num_sides: int, drop_lowest: bool = False) -> None:
        self.num_dice = num_dice
        self.num_sides = num_sides
        self.drop_lowest = drop_lowest

class DiceRoller:
    """Utility class for rolling dice."""

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
        """
        if isinstance(num_dice, str):
            config = DiceRoller.parse_dice_notation(num_dice, drop_lowest)
            return DiceRoller.roll(config.num_dice, config.num_sides, config.drop_lowest)

        if num_dice < 1 or num_sides is None or num_sides < 1:
            raise ValueError("Number of dice and sides must be at least 1.")

        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        if drop_lowest:
            return sum(sorted(rolls)[1:])
        return sum(rolls)

    @staticmethod
    def parse_dice_notation(dice_notation: str, drop_lowest: bool = False) -> DiceRollConfig:
        """Parses a dice notation string and returns a configuration object.

        Args:
            dice_notation (str): String describing the dice roll format.
            drop_lowest (bool): Whether to drop the lowest roll. Defaults to False.

        Returns:
            DiceRollConfig: Configuration object based on the provided notation.

        Raises:
            ValueError: If the notation is not in the supported format.
        """
        try:
            num_dice, num_sides = map(int, dice_notation.split('d'))
        except ValueError:
            raise ValueError("Unsupported dice notation format.")

        return DiceRollConfig(num_dice=num_dice, num_sides=num_sides, drop_lowest=drop_lowest)
