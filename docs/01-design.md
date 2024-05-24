# Turn-based RPG engine design document

## Introduction

This document outlines the design for a Python-based turn-based RPG engine. The engine aims to replicate the gameplay style of classic RPGs like Bard's Tale and the Gold Box series while faithfully implementing the rules from the D&D Basic Set Rulebook. The goal is to provide a flexible and modular package for developers to create their own RPGs, whether GUI- or text-based.

## Core components

### Character module

#### Character creation

- **Ability scores**: Roll 3d6 or 4d6-drop-lowest for each of the six abilities: Strength, Intelligence, Wisdom, Dexterity, Constitution, and Charisma. Option for manual assignment.
- **Classes**: Implement core classes (Cleric, Dwarf, Elf, Fighter, Halfling, Magic-User, Thief) with unique abilities and restrictions.
- **Alignment**: Characters choose from Lawful, Neutral, or Chaotic.
- **Hit points**: Calculate based on class and Constitution.
- **Equipment**: Basic starting equipment for each class.

#### Character management

- **Serialization**: Methods to serialize and deserialize characters to JSON or other formats.
- **Factory pattern**: Use a factory pattern for character creation.

   ```python
   from typing import Dict, List, Optional

   class Character:
       def __init__(self, name: str, char_class: str, abilities: Dict[str, int], alignment: str) -> None:
           self.name = name
           self.char_class = char_class
           self.abilities = abilities
           self.alignment = alignment
           self.hit_points = self.calculate_hit_points()
           self.equipment: List[Item] = []

       def calculate_hit_points(self) -> int:
           # Logic to calculate hit points based on class and Constitution
           pass

       def roll_initiative(self) -> int:
           # Logic to roll initiative
           return DiceRoller.roll_dice(1, 20)[0] + self.abilities.get('Dexterity', 0)

   class CharacterFactory:
       @staticmethod
       def create_character(name: str, char_class: str, abilities: Dict[str, int], alignment: str) -> Character:
           return Character(name, char_class, abilities, alignment)
   ```

### Combat module

#### Combat mechanics

- **Turn-based system**: Manage combat phases with a state machine.
- **Actions**: Basic actions include attack, defend, cast spell, use item, and flee.
- **Initiative**: Determine turn order using per-character initiative rolls.
- **Surprise**: Handle surprise rounds where surprised characters/monsters cannot act.

#### Attack and defense

- **Attack rolls**: Use 1d20 for attack rolls, calculate damage based on weapon and abilities.
- **Damage calculation**: Based on weapon type and modifiers.

#### Special combat scenarios

- **Multiple attacks**: Handle characters or monsters capable of multiple attacks per round.
- **Critical hits**: Define and handle critical hit scenarios.
- **Status effects**: Apply and manage status effects like paralysis, poison, etc.

#### Monster AI

- **Basic AI**: Simple decision-making for monster actions.

   ```python
   from typing import List

   class CombatManager:
       def __init__(self, characters: List[Character], monsters: List[Monster]) -> None:
           self.characters = characters
           self.monsters = monsters
           self.turn_order = self.determine_turn_order()

       def determine_turn_order(self) -> List:
           # Use per-character initiative rolls to determine turn order
           return sorted(self.characters + self.monsters, key=lambda x: x.roll_initiative(), reverse=True)

       def execute_turn(self) -> None:
           for entity in self.turn_order:
               if isinstance(entity, Character):
                   self.player_turn(entity)
               else:
                   self.monster_turn(entity)

       def player_turn(self, player: Character) -> None:
           # Implement player actions (attack, defend, cast spell, use item, flee)
           pass

       def monster_turn(self, monster: Monster) -> None:
           # Implement basic AI for monster actions
           pass

       def resolve_attack(self, attacker: Character, defender: Character) -> None:
           attack_roll = DiceRoller.roll_dice(1, 20)[0] + attacker.abilities['Strength']
           if attack_roll >= defender.armor_class:
               damage = attacker.weapon.damage + attacker.abilities['Strength']
               defender.hit_points -= damage
               if attack_roll == 20:  # Critical hit
                   defender.hit_points -= damage
           if defender.hit_points <= 0:
               self.handle_defeat(defender)

       def handle_defeat(self, entity: Character) -> None:
           # Logic to handle character/monster defeat
           pass

       def apply_status_effect(self, entity: Character, effect: StatusEffect) -> None:
           # Logic to apply status effects (e.g., paralysis, poison)
           pass

       def handle_surprise(self, surprised_entities: List[Character]) -> None:
           # Logic to handle surprise rounds
           for entity in surprised_entities:
               # Surprised entities cannot act in the first round
               pass
   ```

### Magic module

#### Spell management

- **Spell list**: Core spells for Magic-Users and Clerics.
- **Spell casting**: Mechanism for casting spells, including preparation and spontaneous casting.

#### Spell effects

- **Effect handling**: Abstract spell effects for flexibility.

   ```python
   class SpellEffect:
       def apply(self, caster: Character, target: Character) -> None:
           pass

   class AreaOfEffectSpellEffect(SpellEffect):
       def apply(self, caster: Character, targets: List[Character]) -> None:
           # Logic for area-of-effect spells
           pass

   class BuffDebuffEffect(SpellEffect):
       def apply(self, caster: Character, target: Character) -> None:
           # Logic for buffs and debuffs
           pass

   class Spell:
       def __init__(self, name: str, level: int, effect: SpellEffect) -> None:
           self.name = name
           self.level = level
           self.effect = effect

       def cast(self, caster: Character, target: Optional[Character] = None, targets: Optional[List[Character]] = None) -> None:
           if targets:
               self.effect.apply(caster, targets)
           else:
               self.effect.apply(caster, target)

   fireball = Spell('Fireball', 3, AreaOfEffectSpellEffect())
   ```

### Monsters and encounters

#### Monster statistics

- **Core stats**: Implement basic stats such as hit points, attack power, and abilities.
- **Behavior**: Simple AI for monster behavior in encounters.

   ```python
   class Monster:
       def __init__(self, name: str, hit_points: int, attack_power: int) -> None:
           self.name = name
           self.hit_points = hit_points
           self.attack_power = attack_power

       def attack(self, target: Character) -> None:
           # Simple attack logic
           pass
   ```

### Treasure and equipment

#### Inventory system

- **Basic inventory**: Manage character inventory with items, weapons, and armor.
- **Core items**: Implement essential items and their effects.

   ```python
   class Item:
       def __init__(self, name: str, item_type: str, value: int) -> None:
           self.name = name
           self.item_type = item_type
           self.value = value

   class Inventory:
       def __init__(self) -> None:
           self.items: List[Item] = []

       def add_item(self, item: Item) -> None:
           self.items.append(item)

       def remove_item(self, item: Item) -> None:
           self.items.remove(item)
   ```

### Adventure and exploration

#### Dungeon mapping

- **Basic mapping**: Generate simple dungeon maps with rooms and corridors.
- **Exploration mechanics**: Implement basic rules for movement, light, and traps.

   ```python
   class DungeonGenerator:
       def generate(self) -> None:
           # Simple procedural generation logic
           pass
   ```

### Quest system

#### Quest management

- **Quest log**: Maintain a list of active and completed quests.
- **Quest structure**: Define quests with objectives, rewards, and conditions for completion.

   ```python
   class Objective:
       def __init__(self, description: str, is_complete: bool) -> None:
           self.description = description
           self.is_complete = is_complete

   class Quest:
       def __init__(self, title: str, description: str, objectives: List[Objective], rewards: List[Item]) -> None:
           self.title = title
           self.description = description
           self.objectives = objectives
           self.rewards = rewards
           self.completed = False

       def check_completion(self) -> bool:
           if all(objective.is_complete for objective in self.objectives):
               self.completed = True
               return True
           return False
   ```

### Adventurer's journal

#### Journal management

- **Entry logging**: Log significant events, discoveries, and interactions.
- **Organization**: Organize entries by date and category for easy reference.

   ```python
   class JournalEntry:
       def __init__(self, date: str, content: str) -> None:
           self.date = date
           self.content = content

   class Journal:
       def __init__(self) -> None:
           self.entries: List[JournalEntry] = []

       def add_entry(self, entry: JournalEntry) -> None:
           self.entries.append(entry)
   ```

### NPC interactions

#### NPC system

- **NPC creation**: Define NPCs with stats, dialogues, and behaviors.
- **Dialogue system**: Implement a simple dialogue tree for interactions.

   ```python
   class DialogueOption:
       def __init__(self, text: str, next_dialogue: Optional['Dialogue'] = None, condition: Optional[Callable[['Character'], bool]] = None) -> None:
           self.text = text
           self.next_dialogue = next_dialogue
           self.condition = condition

   class Dialogue:
       def __init__(self, text: str, options: List[DialogueOption]) -> None:
           self.text = text
           self.options = options

   class NPC:
       def __init__(self, name: str, dialogue: Dialogue) -> None:
           self.name = name
           self.dialogue = dialogue

       def interact(self, player: Character) -> None:
           # Logic for interacting with the player
           pass
   ```

#### OpenAI API for dialogue generation

- **Live dialogue**: Use the OpenAI API to generate dialogue dynamically during gameplay.
- **Pregenerated dialogue**: Use the API to create dialogue for NPCs in the dialogue tree.

   ```python
   import openai

   def generate_dialogue(prompt: str) -> str:
       response = openai.Completion.create(
           engine="davinci",
           prompt=prompt,
           max_tokens=150
       )
       return response.choices[0].text.strip()
   ```

### Utility module

### Dice rolling

- **Dice roller class**: Implement a utility class for rolling dice with various configurations, including 3d6 and 4d6-drop-lowest.

   ```python
   import random
   from typing import List

   class DiceRoller:
       @staticmethod
       def roll_dice(num_dice: int, num_sides: int) -> List[int]:
           return [random.randint(1, num_sides) for _ in range(num_dice)]

       @staticmethod
       def roll_3d6() -> int:
           return sum(DiceRoller.roll_dice(3, 6))

       @staticmethod
       def roll_4d6_drop_lowest() -> int:
           rolls = DiceRoller.roll_dice(4, 6)
           return sum(sorted(rolls)[1:])
   ```

### Event system

#### Event handling

- **Event class**: Define events that trigger specific actions in the game.
- **Event manager**: Manage and trigger events based on game state and player actions.

   ```python
   from typing import Callable, Dict, List

   class Event:
       def __init__(self, name: str, action: Callable) -> None:
           self.name = name
           self.action = action

   class EventManager:
       def __init__(self) -> None:
           self.events: Dict[str, List[Callable]] = {}

       def register_event(self, event_name: str, action: Callable) -> None:
           if event_name not in self.events:
               self.events[event_name] = []
           self.events[event_name].append(action)

       def deregister_event(self, event_name: str, action: Callable) -> None:
           if event_name in self.events:
               self.events[event_name].remove(action)
               if not self.events[event_name]:
                   del self.events[event_name]

       def trigger_event(self, event_name: str) -> None:
           if event_name in self.events:
               for action in self.events[event_name]:
                   action()
   ```

## Key design principles

1. **Modularity**: Ensure each component (character, combat, magic, etc.) is modular and easy to extend.
2. **User-friendly interfaces**: Focus on providing clear and intuitive interfaces for both text-based and potential GUI implementations.
3. **Essential features first**: Implement core mechanics first, ensuring a playable and enjoyable experience.
4. **Documentation and examples**: Provide clear documentation and examples for each feature to help developers integrate and use the package effectively.

## Coding style guidelines

We will adhere to Google's Python Style Guide for all code written for this project. This includes:
- Using `docstrings` for all public modules, classes, functions, and methods.
- Following naming conventions for variable names, function names, and class names.
- Writing unit tests for all significant code components.
- Keeping code within the recommended line length.

## Python version

We will use Python 3.11 for this project to leverage the latest features and improvements.

## Sample project

- **Sample game**: Include a sample project or demo game that showcases the engine's capabilities. This will serve as a practical reference for developers and help them get started quickly.

By focusing on these simplified yet essential components, we can create a solid foundation for our turn-based RPG engine while ensuring it remains faithful to the D&D Basic ruleset. This approach will allow us to deliver a robust, flexible, and user-friendly package for developers.
