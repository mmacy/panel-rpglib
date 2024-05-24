# tests/test_dice_roller.py

import pytest
from arbrynnica.utils.dice_roller import DiceRoller

def test_roll_dice():
    """Test rolling a specified number of dice with a given number of sides."""
    rolls = DiceRoller.roll_dice(3, 6)
    assert len(rolls) == 3
    for roll in rolls:
        assert 1 <= roll <= 6

def test_roll_3d6():
    """Test rolling 3 six-sided dice and returning the sum."""
    total = DiceRoller.roll_3d6()
    assert 3 <= total <= 18

def test_roll_4d6_drop_lowest():
    """Test rolling 4 six-sided dice, dropping the lowest roll, and returning the sum of the remaining three."""
    total = DiceRoller.roll_4d6_drop_lowest()
    assert 3 <= total <= 18
