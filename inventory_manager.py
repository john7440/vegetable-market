from inventory import Inventory
from dataclasses import dataclass, field
from typing import List

@dataclass
class InventoryManager:
    items : List[Inventory] = field(default_factory=list)