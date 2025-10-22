from dataclasses import dataclass

@dataclass
class InventoryManager:
    product: str
    stock: int
    unit_price: float

    def total_value(self):
        """
        This function calculates the total value of the inventory.
        :return: the value of the inventory.
        """
        return self.unit_price * self.stock