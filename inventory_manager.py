from inventory import Inventory
from dataclasses import dataclass, field
from typing import List

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
        #total = sum(item.total_value() for item in self.items)
        #print(f'Total inventory value: {total:.2f} €')

    def add_item(self, item: Inventory) -> None:
        """Add an item to the inventory"""
        self.items.append(item)

    def get_item(self, item_name):
        for item in self.items:
            if item.product == item_name:
                return item
        return None