from dataclasses import dataclass

@dataclass
class InventoryManager:
    product: str
    stock: int
    unit_price: float