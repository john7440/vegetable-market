from inventory import Inventory
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class InventoryManager:
    """
    This class is made to manage the stock, we can easily add more items
    and display them.
    """
    items : List[Inventory] = field(default_factory=list)

    def display_inventory(self) -> None:
        """Display the inventory product by product and
        the total value of the inventory"""
        print('=' * 60)
        print(f"{'Product':<20} | {'Quantity':<20} | {'Price':<20} ")
        print('-' * 60)
        for item in self.items:
            print(item.display())
        print('=' * 60)

    def add_item(self, item: Inventory) -> None:
        """Add an item to the inventory"""
        self.items.append(item)

    def get_item(self, item_name) -> Optional[Inventory]:
        """
        This function is made to get the item from the inventory
        :param item_name: the name of the product.
        :return: the matching inventory item, or None if there is no item.
        """
        for item in self.items:
            if item.product == item_name:
                return item
        return None