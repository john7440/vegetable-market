from product import Product
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class InventoryManager:
    """
    This class is made to manage the stock, we can easily add more items
    and display them.
    """
    items : List[Product] = field(default_factory=list)

    def display_inventory(self) -> str:
        """Display the inventory product by product and
        the total value of the inventory"""
        output = '=' * 60 + '\n'
        output += f"{'Product':<20} | {'Quantity':<20} | {'Price':<20}\n"
        output += '-' * 60 + '\n'
        for item in self.items:
            output += item.display() + '\n'
        output += '=' * 60 + '\n'
        total = sum(item.total_value() for item in self.items)
        output += f'Total value: {total:.2f} €\n'
        return output

    def add_item(self, item: Product) -> None:
        """Add an item to the inventory"""
        self.items.append(item)

    def get_item(self, item_name) -> Optional[Product]:
        """
        This function is made to get the item from the inventory
        :param item_name: the name of the product.
        :return: the matching inventory item, or None if there is no item.
        """
        for item in self.items:
            if item.product == item_name:
                return item
        return None
