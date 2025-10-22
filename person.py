from __future__ import annotations
from dataclasses import dataclass, field


from inventory_manager import InventoryManager
#from shopping_cart import ShoppingCart
from typing import List, ClassVar, Optional


@dataclass
class Person:
    first_name : str
    last_name : str
    shopping_cart : Optional['ShoppingCart'] = None
    history_list : List[InventoryManager] = field(default_factory=list)

    #static
    clients: ClassVar[List['Person']] = []
    def get_histories(self):
        histories_list = ''
        for i in range(len(self.history_list)):
            histories_list += str(i) + '\n'


    def get_history_n(self, number : int):
        if 0 <= number <= len(self.history_list)-1:
            return self.history_list[number].display_inventory()
        else:
            return 'no available history number'

    @staticmethod
    def exists(first_name, last_name):
        for client in Person.clients:
            if client.first_name == first_name and client.last_name == last_name:
                return True
        #not created i came there
        return False