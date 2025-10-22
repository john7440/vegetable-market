from dataclasses import dataclass, field


from inventory_manager import InventoryManager
from shopping_cart import ShoppingCart
from typing import List


@dataclass
class Person:
    name : str
    surname : str
    shopping_car : ShoppingCart
    history_list : List[InventoryManager]

    def get_histories(self):
        histories_list = ''
        for i in range(len(self.history_list)):
            histories_list += str(i) + '\n'


    def get_history_n(self, number : int):
        if 0 <= number <= len(self.history_list)-1:
            return self.history_list[number].display_inventory()
        else:
            return 'no available history number'
