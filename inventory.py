from dataclasses import dataclass

@dataclass
class InventoryManager:
    """
    This class is made to manage an inventory composed
    of products (vegetables and fruits), we have a definite
    stock and a price per unit or per kg.
    """
    product: str
    stock: int
    unit_price: float

    def total_value(self) -> float:
        """
        This function calculates the total value of the inventory.
        :return: the value of the inventory.
        """
        return self.unit_price * self.stock