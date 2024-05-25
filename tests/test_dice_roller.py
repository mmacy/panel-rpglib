# tests/test_dice_roller.py

import pytest
from arbrynnica.utils.dice_roller import DiceRoller

def test_roll():
    """Test rolling a specified number of dice with a given number of sides."""
    result = DiceRoller.roll(3, 6)
    assert 3 <= result <= 18

def test_roll_with_drop_lowest():
    """Test rolling a specified number of dice with dropping the lowest roll."""
    result = DiceRoller.roll(4, 6, drop_lowest=True)
    assert 3 <= result <= 18

def test_roll_with_notation():
    """Test rolling dice using notation."""
    result = DiceRoller.roll('3d6')
    assert 3 <= result <= 18

    result_drop_lowest = DiceRoller.roll('4d6', drop_lowest=True)
    assert 3 <= result_drop_lowest <= 18

def test_parse_dice_notation():
    """Test parsing dice notation strings and rolling dice accordingly."""
    config_3d6 = DiceRoller._parse_dice_notation('3d6')
    assert config_3d6.num_dice == 3
    assert config_3d6.num_sides == 6
    assert not config_3d6.drop_lowest

    config_4d6_drop_lowest = DiceRoller._parse_dice_notation('4d6', drop_lowest=True)
    assert config_4d6_drop_lowest.num_dice == 4
    assert config_4d6_drop_lowest.num_sides == 6
    assert config_4d6_drop_lowest.drop_lowest

def test_roll_invalid_input():
    """Test rolling dice with invalid inputs."""
    with pytest.raises(ValueError):
        DiceRoller.roll(0, 6)
    with pytest.raises(ValueError):
        DiceRoller.roll(3, 0)
    with pytest.raises(ValueError):
        DiceRoller.roll(-1, 6)
    with pytest.raises(ValueError):
        DiceRoller.roll(3, -1)

def test_parse_dice_notation_invalid_input():
    """Test parsing invalid dice notation strings."""
    with pytest.raises(ValueError):
        DiceRoller._parse_dice_notation('2d')
    with pytest.raises(ValueError):
        DiceRoller._parse_dice_notation('d6')
    with pytest.raises(ValueError):
        DiceRoller._parse_dice_notation('3d6 drop')
    with pytest.raises(ValueError):
        DiceRoller._parse_dice_notation('3d6 keep highest')
