# src/arbrynnica/inventory.py
"""This module defines the classes and functions related to inventory management in the RPG.

Typical usage example:

  item = Item("Sword", "weapon", 10)
  inventory = Inventory()
  inventory.add_item(item)
"""

from typing import List, Dict

class Item:
    """Represents an item in the RPG.

    Attributes:
        name (str): The name of the item.
        item_type (str): The type of the item (e.g., weapon, armor, potion).
        value (int): The value of the item.
    """
    def __init__(self, name: str, item_type: str, value: int) -> None:
        self.name = name
        self.item_type = item_type
        self.value = value

class Inventory:
    """Represents an inventory for a character.

    Attributes:
        items (List[Item]): A list of items in the inventory.
    """
    def __init__(self) -> None:
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """Adds an item to the inventory.

        Args:
            item (Item): The item to add.
        """
        self.items.append(item)

    def remove_item(self, item: Item) -> None:
        """Removes an item from the inventory.

        Args:
            item (Item): The item to remove.
        """
        self.items.remove(item)

    def has_item(self, item: Item) -> bool:
        """Checks if the inventory contains a specific item.

        Args:
            item (Item): The item to check.

        Returns:
            bool: True if the item exists in the inventory, otherwise False.
        """
        return item in self.items

    def get_total_value(self) -> int:
        """Calculates the total value of all items in the inventory.

        Returns:
            int: The total value of all items.
        """
        return sum(item.value for item in self.items)

    def get_summary_by_type(self) -> Dict[str, int]:
        """Provides a summary of items in the inventory categorized by type.

        Returns:
            Dict[str, int]: A dictionary with item types as keys and counts as values.
        """
        summary = {}
        for item in self.items:
            if item.item_type in summary:
                summary[item.item_type] += 1
            else:
                summary[item.item_type] = 1
        return summary
