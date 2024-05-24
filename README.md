
# Arbrynnica

Arbrynnica is a Python-based turn-based RPG engine designed to replicate the gameplay style of classic RPGs like Bard's Tale and the Gold Box series while faithfully implementing the rules from the D&D Basic Set Rulebook. This engine provides a flexible and modular package for developers to create their own RPGs, whether GUI- or text-based. It is designed for ease of customization and extension, allowing developers to build on a solid foundation.

> [!WARNING]
> Nearly all the code and documentation in this repo (including this README, but not this note) has been or will be created by an LLM guided with the ["panel of experts" prompting strategy](https://sourcery.ai/blog/panel-of-experts/). Take it with an LLM-sized grain of salt and caveat emptor and all that. 🙂 *—Marsh*

## About the project

Arbrynnica is an experimental project to explore how far one might get with a project in which all planning, documentation, and code is created by a Large Language Model (LLM) with guidance from a "panel of experts" prompting strategy. This project aims to demonstrate the potential and limitations of LLM-driven development.

> *"Arbrynnica" is a combination of the code names of the three fictitious "experts" in the LLM's panel of experts: Art, Brynn, and Celica.*

## Features

- **Character creation and management**: Supports character creation with various classes, ability scores, and alignments.
- **Combat system**: Implements turn-based combat with attack, defense, magic, and special combat scenarios.
- **Magic system**: Manages spell casting, spell effects, and different types of magic.
- **Monsters and encounters**: Includes monster stats and behavior for dynamic encounters.
- **Inventory system**: Manages character inventory, items, and equipment.
- **Adventure and exploration**: Generates dungeons and tracks exploration progress.
- **Quest system**: Tracks quests, objectives, and rewards.
- **Adventurer's journal**: Logs significant events and interactions.
- **NPC interactions**: Handles NPC dialogues and interactions with dynamic dialogue generation.
- **Event system**: Manages game events and triggers.
- **Game save/load**: Supports saving and loading game states.

## Prerequisites

- [Python 3.12](https://www.python.org/downloads/)+
- [Rye](https://rye.astral.sh)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/mmacy/panel-rpglib.git
   cd arbrynnica
   ```

1. Create and activate a virtual environment with Rye:

   ```sh
   rye sync
   ```

## Usage

### Character creation

```python
"""NOT YET IMPLEMENTED"""
from arbrynnica.character import CharacterFactory

abilities = {
    "Strength": 15,
    "Intelligence": 12,
    "Wisdom": 10,
    "Dexterity": 14,
    "Constitution": 13,
    "Charisma": 11
}

character = CharacterFactory.create_character(name="Arthas", char_class="Fighter", abilities=abilities, alignment="Lawful")
print(character)
```

### Combat system

```python
"""NOT YET IMPLEMENTED"""
from arbrynnica.combat import CombatManager

# Example characters and monsters would be set up here

combat_manager = CombatManager(characters=[character], monsters=[monster])
combat_manager.execute_turn()
```

### Magic system

```python
"""NOT YET IMPLEMENTED"""
from arbrynnica.magic import Spell, SpellEffect, AreaOfEffectSpellEffect

# Define a new spell effect
class FireballEffect(AreaOfEffectSpellEffect):
    def apply(self, caster, targets):
        for target in targets:
            damage = DiceRoller.roll_dice(6, 6)  # 6d6 fire damage
            target.hit_points -= sum(damage)

# Create a fireball spell
fireball = Spell(name="Fireball", level=3, effect=FireballEffect())

# Cast the spell
fireball.cast(caster=character, targets=[monster])
```

### Inventory system

```python
"""NOT YET IMPLEMENTED"""
from arbrynnica.inventory import Inventory, Item

# Create a new inventory and add items
inventory = Inventory()
sword = Item(name="Sword", item_type="Weapon", value=10)
inventory.add_item(sword)

# Remove an item
inventory.remove_item(sword)
```

## Contributing

We welcome contributions to Arbrynnica! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to get started.

## License

This project is licensed under the Creative Commons CC0 1.0 Universal. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue on GitHub.
