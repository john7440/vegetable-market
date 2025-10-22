from dataclasses import dataclass
from typing import Literal


@dataclass
class InventoryManager:
    """
    This class is made to manage an inventory composed
    of products (vegetables and fruits), we have a definite
    stock and a price per unit or per kg.
    """
    product: str
    stock: float
    price: float
    sale_type: Literal['unit', 'kg']
    # ex utilisation : kiwi = InventoryManager('Kiwi', stock = 5.0, price = 3.5, sale_type = 'kg')
                    #  potiron = InventoryManager('Potiron', stock = 6.0, price = 2.5, sale_type = 'unit')

    def total_value(self) -> float:
        """
        This function calculates the total value of the inventory.
        :return: the value of the inventory.
        """
        return self.price * self.stock
