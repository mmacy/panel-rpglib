# src/arbrynnica/inventory.py
"""This module defines the classes and functions related to inventory management in the RPG.

Characters can carry various items in their inventory, such as weapons, armor, and potions. This module provides the structure and behavior for managing these items.

Typical usage example:

    ```python
    item = Item("Sword", "weapon", 10)
    inventory = Inventory()
    inventory.add_item(item)
    ```
"""

from typing import List, Dict


class Item:
    """Represents an item in the RPG.

    Attributes:
        name (str): The name of the item.
        item_type (str): The type of the item (e.g., weapon, armor, potion).
        value (int): The value of the item.

    Example:
        ```python
        # Creating an item
        sword = Item("Sword", "weapon", 10)
        ```
    """

    def __init__(self, name: str, item_type: str, value: int) -> None:
        """Initializes an item.

        Args:
            name (str): The name of the item.
            item_type (str): The type of the item (e.g., weapon, armor, potion).
            value (int): The value of the item.

        Example:
            ```python
            sword = Item("Sword", "weapon", 10)
            ```
        """
        self.name = name
        self.item_type = item_type
        self.value = value


class Inventory:
    """Represents an inventory for a character.

    The inventory holds multiple items and provides methods to add, remove, and query items.

    Attributes:
        items (List[Item]): A list of items in the inventory.

    Example:
        ```python
        # Creating an inventory and adding an item
        inventory = Inventory()
        sword = Item("Sword", "weapon", 10)
        inventory.add_item(sword)
        ```
    """

    def __init__(self) -> None:
        """Initializes an empty inventory.

        Example:
            ```python
            inventory = Inventory()
            ```
        """
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """Adds an item to the inventory.

        Call this method to add an item to the character's inventory.

        Args:
            item (Item): The item to add.

        Example:
            ```python
            inventory = Inventory()
            sword = Item("Sword", "weapon", 10)
            inventory.add_item(sword)
            ```
        """
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        """Removes an item from the inventory.

        Call this method to remove an item from the character's inventory.

        Args:
            item (Item): The item to remove.

        Example:
            ```python
            inventory = Inventory()
            sword = Item("Sword", "weapon", 10)
            inventory.add_item(sword)
            inventory.remove_item(sword)
            ```
        """
        self.items.remove(item)

    def has_item(self, item: Item) -> bool:
        """Checks if the inventory contains a specific item.

        Call this method to check if a specific item is in the character's inventory.

        Args:
            item (Item): The item to check.

        Returns:
            bool: True if the item exists in the inventory, otherwise False.

        Example:
            ```python
            inventory = Inventory()
            sword = Item("Sword", "weapon", 10)
            inventory.add_item(sword)
            has_sword = inventory.has_item(sword)  # returns True
            ```
        """
        return item in self.items

    def get_total_value(self) -> int:
        """Calculates the total value of all items in the inventory.

        Call this method to get the total value of the items the character is carrying.

        Returns:
            int: The total value of all items.

        Example:
            ```python
            inventory = Inventory()
            sword = Item("Sword", "weapon", 10)
            shield = Item("Shield", "armor", 15)
            inventory.add_item(sword)
            inventory.add_item(shield)
            total_value = inventory.get_total_value()  # returns 25
            ```
        """
        return sum(item.value for item in self.items)

    def get_summary_by_type(self) -> Dict[str, int]:
        """Provides a summary of items in the inventory categorized by type.

        Call this method to get a summary of how many items of each type the character is carrying.

        Returns:
            Dict[str, int]: A dictionary with item types as keys and counts as values.

        Example:
            ```python
            inventory = Inventory()
            sword = Item("Sword", "weapon", 10)
            shield = Item("Shield", "armor", 15)
            potion = Item("Potion", "potion", 5)
            inventory.add_item(sword)
            inventory.add_item(shield)
            inventory.add_item(potion)
            summary = inventory.get_summary_by_type()  # returns {'weapon': 1, 'armor': 1, 'potion': 1}
            ```
        """
        summary = {}
        for item in self.items:
            if item.item_type in summary:
                summary[item.item_type] += 1
            else:
                summary[item.item_type] = 1
        return summary
