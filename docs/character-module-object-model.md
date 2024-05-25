# Character module object model

## Primary components

### Character

- **Attributes**:

  - `name: str`
  - `class: CharacterClass`
  - `abilities: Abilities`
  - `alignment: Alignment`
  - `hit_points: int`
  - `experience_points: int`
  - `level: int`
  - `inventory: Inventory`
  - `skills: List[Skill]`
  - `conditions: List[Condition]`
  - `modifiers: List[Modifier]`

- **Methods**:

  - `calculate_hit_points()`
  - `roll_initiative()`
  - `get_ability_modifier(ability: str)`
  - `level_up()`
  - `gain_experience(points: int)`
  - `equip_item(item: Item)`
  - `unequip_item(item: Item)`
  - `use_item(item: Item)`
  - `learn_spell(spell: Spell)`
  - `cast_spell(spell: Spell, target: Character)`
  - `apply_condition(condition: Condition)`
  - `remove_condition(condition: Condition)`
  - `apply_modifier(modifier: Modifier)`
  - `remove_modifier(modifier: Modifier)`
  - `update_attributes()`
  - `decrement_modifiers()`

### CharacterClass

- **Attributes**:

  - `name: str`
  - `hit_die: int`
  - `abilities: List[str]`
  - `spells: List[Spell]`
  - `equipment: List[Item]`
  - `skills: List[Skill]`

- **Methods**:

  - `level_up(character: Character)`
  - `apply_class_specific_bonuses(character: Character)`

### Abilities

- **Attributes**:

  - `strength: int`
  - `intelligence: int`
  - `wisdom: int`
  - `dexterity: int`
  - `constitution: int`
  - `charisma: int`

- **Methods**:

  - `roll_3d6()`
  - `roll_4d6_drop_lowest()`

### Alignment

- **Attributes**:

  - `type: str`  # Options: 'Lawful', 'Neutral', 'Chaotic'

### Inventory

- **Attributes**:

  - `items: List[Item]`

- **Methods**:

  - `add_item(item: Item)`
  - `remove_item(item: Item)`
  - `list_items()`

### Item

- **Attributes**:

  - `name: str`
  - `type: str`
  - `value: int`
  - `effect: str`
  - `modifiers: List[Modifier]`

- **Methods**:

  - `use(character: Character)`
  - `apply_to_character(character: Character)`

### Spell

- **Attributes**:

  - `name: str`
  - `level: int`
  - `effect: str`
  - `casting_time: int`
  - `duration: int`
  - `range: int`

- **Methods**:

  - `cast(caster: Character, target: Character)`

### Skill

- **Attributes**:

  - `name: str`
  - `level: int`
  - `effect: str`

- **Methods**:

  - `use_skill(target: Optional[Character] = None)`

### Condition

- **Attributes**:

  - `name: str`
  - `effect: str`
  - `duration: int`

- **Methods**:

  - `apply(character: Character)`
  - `remove(character: Character)`

### Modifier

- **Attributes**:

  - `name: str`
  - `value: int`
  - `duration: Optional[int]`
  - `type: str`
  - `condition: Optional[Callable[['Character'], bool]]`
  - `scope: str`
  - `source: str`

- **Methods**:

  - `is_active(character: Character)`
  - `apply_effect(character: Character)`
  - `remove_effect(character: Character)`

### Experience

- **Attributes**:

  - `points: int`

- **Methods**:

  - `gain(points: int)`
  - `check_level_up(character: Character)`

## Hierarchy

```plaintext
Character
│
├── CharacterClass
│   ├── name
│   ├── hit_die
│   ├── abilities
│   ├── spells
│   ├── equipment
│   ├── skills
│   └── Methods
│       ├── level_up(character)
│       └── apply_class_specific_bonuses(character)
│
├── Abilities
│   ├── strength
│   ├── intelligence
│   ├── wisdom
│   ├── dexterity
│   ├── constitution
│   ├── charisma
│   └── Methods
│       ├── roll_3d6()
│       └── roll_4d6_drop_lowest()
│
├── Alignment
│   └── type
│
├── Inventory
│   ├── items
│   └── Methods
│       ├── add_item(item)
│       ├── remove_item(item)
│       └── list_items()
│
├── Item
│   ├── name
│   ├── type
│   ├── value
│   ├── effect
│   └── modifiers
│
├── Spell
│   ├── name
│   ├── level
│   ├── effect
│   ├── casting_time
│   ├── duration
│   └── range
│
├── Skill
│   ├── name
│   ├── level
│   └── effect
│
├── Condition
│   ├── name
│   ├── effect
│   └── duration
│
├── Modifier
│   ├── name
│   ├── value
│   ├── duration
│   ├── type
│   ├── condition
│   ├── scope
│   └── source
│
└── Experience
    ├── points
    └── Methods
        ├── gain(points)
        └── check_level_up(character)
```