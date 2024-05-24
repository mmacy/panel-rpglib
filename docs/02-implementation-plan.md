# Turn-based RPG engine implementation plan

## Implementation phases

### Phase 1: Core utilities and base classes

1. **Utility module (DiceRoller)**

   - Implement `DiceRoller` class with methods for various dice rolls
   - Unit tests for `DiceRoller`

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

2. **Character module**

   - Implement `Character` and `CharacterFactory` classes
   - Serialization and deserialization methods
   - Character ability score rolling methods (3d6 and 4d6-drop-lowest)
   - Unit tests for `Character` and `CharacterFactory`

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

3. **Game save/load**

   - Implement `GameState` class with save and load functionality
   - Unit tests for `GameState`

   ```python
   import json

   class GameState:
       def __init__(self, characters: List[Character], adventure: Adventure, journal: Journal) -> None:
           self.characters = characters
           self.adventure = adventure
           self.journal = journal

       def save_game(self, file_path: str) -> None:
           state = {
               "characters": [char.__dict__ for char in self.characters],
               "adventure": self.adventure.__dict__,
               "journal": self.journal.__dict__
           }
           with open(file_path, 'w') as f:
               json.dump(state, f)

       def load_game(self, file_path: str) -> None:
           with open(file_path, 'r') as f:
               state = json.load(f)
           self.characters = [Character(**char_data) for char_data in state['characters']]
           self.adventure = Adventure(**state['adventure']]
           self.journal = Journal(**state['journal']]
   ```

### Phase 2: Core systems

1. **Combat module**

   - Implement `CombatManager` class
   - Define combat phases and state management
   - Implement attack and defense mechanics
   - Handle special combat scenarios (e.g., critical hits, multiple attacks)
   - Implement surprise round handling
   - Unit tests for `CombatManager`

2. **Magic module**

   - Implement `Spell`, `SpellEffect`, `AreaOfEffectSpellEffect`, and `BuffDebuffEffect` classes
   - Mechanism for casting spells (preparation and spontaneous casting)
   - Handling of various spell effects
   - Unit tests for `Spell` and `SpellEffect` classes

3. **Event system**

   - Implement `Event` and `EventManager` classes for managing game events
   - Unit tests for `Event` and `EventManager`

### Phase 3: Supporting systems

1. **Monsters and encounters**

   - Implement `Monster` class with core stats and behavior
   - Unit tests for `Monster`

2. **Treasure and equipment**

   - Implement `Inventory` and `Item` classes
   - Methods for adding and removing items
   - Unit tests for `Inventory` and `Item`

### Phase 4: Game structure and progression

1. **Adventure and exploration**

   - Implement `DungeonGenerator` class with procedural generation logic
   - Basic rules for movement, light, and traps
   - Unit tests for `DungeonGenerator`

2. **Adventure management**

   - Implement `Adventure` class to manage collections of dungeons and quests
   - Methods for tracking progress through an adventure
   - Unit tests for `Adventure`

3. **Quest system**

   - Implement `Quest` and `Objective` classes
   - Methods for quest tracking and completion
   - Unit tests for `Quest` and `Objective`

4. **Adventurer's journal**

   - Implement `Journal` and `JournalEntry` classes
   - Unit tests for `Journal` and `JournalEntry`

### Phase 5: Interactions and customization

1. **NPC interactions**

   - Implement `NPC`, `Dialogue`, and `DialogueOption` classes
   - Integration with OpenAI API for dynamic dialogue generation
   - Unit tests for `NPC` and `Dialogue`

2. **Configuration and customization**

   - Implement `Config` class for game settings
   - Unit tests for `Config`

### Phase 6: Documentation and sample project

1. **Documentation and examples**

   - Provide comprehensive documentation and examples for each module

2. **Sample project**

   - Develop a sample game to showcase the engine's capabilities

## Task assignments

### Art

1. **Combat module**
2. **Event system**
3. **Treasure and equipment** (collaborative task)

### Brynn

1. **Character module**
2. **Monsters and encounters**
3. **Quest system**
4. **Documentation and examples**

### Celica

1. **Magic module**
2. **NPC interactions**
3. **Configuration and customization**
4. **Sample project**

### Collaborative tasks

1. **Treasure and equipment**
2. **Adventure and exploration**
3. **Adventure management**
4. **Adventurer's journal**
5. **Utility module**
6. **Game save/load**

### Additional considerations

1. **Iterative development**:

   - Emphasizing unit tests for each module ensures we maintain high quality and catch issues early. Continuous integration and automated testing are key to maintaining a stable codebase.

2. **Collaboration**:

   - Collaborative tasks, such as treasure and equipment, adventure and exploration, and adventure management, will benefit from regular check-ins and shared responsibility to ensure consistency and integration across modules.

3. **Flexibility**:

   - While the plan is comprehensive, we should remain flexible and adapt to any new requirements or challenges that arise during development.
