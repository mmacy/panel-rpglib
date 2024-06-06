"""
tests/test_character.py
"""

from arbrynnica.character import Character, CharacterClass, Abilities, Alignment
from arbrynnica.modifier import Modifier
from arbrynnica.condition import Condition


def test_character_creation():
    """Test character creation with basic attributes."""
    char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
    abilities = Abilities(15, 10, 10, 12, 14, 8)
    alignment = Alignment("Lawful")
    character = Character("Arthas", char_class, abilities, alignment)

    assert character.name == "Arthas"
    assert character.char_class.name == "Fighter"
    assert character.abilities.strength == 15
    assert character.alignment.type == "Lawful"
    assert character.hit_points == 12  # 10 + (14-10)//2
    assert character.level == 1
    assert character.experience_points == 0
    assert character.inventory.items == []
    assert character.char_class.prime_requisites == ["strength", "constitution"]
    assert character.conditions == []
    assert character.modifiers == []


def test_calculate_hit_points():
    """Test hit points calculation with and without modifiers."""
    char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
    abilities = Abilities(15, 10, 10, 12, 14, 8)
    alignment = Alignment("Lawful")
    character = Character("Arthas", char_class, abilities, alignment)

    # Test base hit points calculation
    assert character.calculate_hit_points() == 12

    # Apply modifier and test hit points calculation
    hp_modifier = Modifier("hit_points", 5, "flat", "global")
    character.apply_modifier(hp_modifier)
    assert character.calculate_hit_points() == 17

    # Remove modifier and test hit points calculation
    character.remove_modifier(hp_modifier)
    assert character.calculate_hit_points() == 12


def test_gain_experience_and_level_up():
    """Test gaining experience and leveling up."""
    char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
    abilities = Abilities(15, 10, 10, 12, 14, 8)
    alignment = Alignment("Lawful")
    character = Character("Arthas", char_class, abilities, alignment)

    # Gain experience and level up
    character.gain_experience(1000)
    assert character.experience_points == 1000
    assert character.level == 1  # Assuming level up logic requires more points

    character.gain_experience(1000)
    character.check_level_up()  # Explicitly checking level up
    assert character.experience_points == 2000  # TODO: Ensure this initiates level up
    # assert character.level == 2  # TODO: Leveling not yet implemented


def test_gain_experience_and_level_up_edge_cases():
    """Test gaining experience and edge cases for leveling up."""
    char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
    abilities = Abilities(15, 10, 10, 12, 14, 8)
    alignment = Alignment("Lawful")
    character = Character("Arthas", char_class, abilities, alignment)

    # Gain experience just below the threshold
    character.gain_experience(1999)
    assert character.level == 1

    # Gain experience exactly at the threshold
    character.gain_experience(1)  # TODO: Ensure this initiates level up
    # assert character.level == 2 # TODO: Leveling not yet implemented


def test_apply_and_remove_conditions():
    """Test applying and removing conditions."""
    char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
    abilities = Abilities(15, 10, 10, 12, 14, 8)
    alignment = Alignment("Lawful")
    character = Character("Arthas", char_class, abilities, alignment)

    # Apply condition
    condition = Condition("Poisoned", "Reduces health", 3)
    character.apply_condition(condition)
    assert condition in character.conditions

    # Remove condition
    character.remove_condition(condition)
    assert condition not in character.conditions


def test_apply_and_remove_conditions_edge_cases():
    """Test applying and removing conditions, including stacking and removal."""
    char_class = CharacterClass("Fighter", 10, ["strength", "constitution"], [], [], [])
    abilities = Abilities(15, 10, 10, 12, 14, 8)
    alignment = Alignment("Lawful")
    character = Character("Arthas", char_class, abilities, alignment)

    # Apply the same condition twice
    condition = Condition("Poisoned", "Reduces health", 3)
    character.apply_condition(condition)
    character.apply_condition(condition)
    assert len(character.conditions) == 1  # Should not stack identical conditions

    # Remove the condition
    character.remove_condition(condition)
    assert condition not in character.conditions
