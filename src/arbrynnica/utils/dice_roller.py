# src/arbrynnica/utils/dice_roller.py

import random
from typing import List

class DiceRoller:
    """Utility class for rolling dice."""

    @staticmethod
    def roll_dice(num_dice: int, num_sides: int) -> List[int]:
        """Rolls a specified number of dice with a given number of sides.

        Args:
            num_dice (int): Number of dice to roll.
            num_sides (int): Number of sides on each die.

        Returns:
            List[int]: Results of the dice rolls.
        """
        return [random.randint(1, num_sides) for _ in range(num_dice)]

    @staticmethod
    def roll_3d6() -> int:
        """Rolls 3 six-sided dice and returns the sum.

        Returns:
            int: Sum of the dice rolls.
        """
        return sum(DiceRoller.roll_dice(3, 6))

    @staticmethod
    def roll_4d6_drop_lowest() -> int:
        """Rolls 4 six-sided dice, drops the lowest roll, and returns the sum of the remaining three.

        Returns:
            int: Sum of the three highest dice rolls.
        """
        rolls = DiceRoller.roll_dice(4, 6)
        return sum(sorted(rolls)[1:])
