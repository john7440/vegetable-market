from __future__ import annotations

import datetime
from dataclasses import dataclass, field

from typing import List, ClassVar, Optional
from shopping_cart import ShoppingCart


@dataclass
class Client:
    first_name : str
    last_name : str
    shopping_cart : Optional['ShoppingCart'] = field(init=False)
    history_list : List['History'] = field(default_factory=list)

    def __post_init__(self):
        from shopping_cart import ShoppingCart  # import aqui para evitar circular import
        self.shopping_cart = ShoppingCart(owner=self)

    #static
    clients: ClassVar[List['Client']] = []
    def get_histories(self):
        histories_list = ''
        for i in range(len(self.history_list)):
            histories_list += str(i) + '\n'


    def get_history_n(self, number : int):
        if 0 <= number <= len(self.history_list)-1:
            return self.history_list[number].articles_list.display_inventory()
        else:
            return 'no available history number'

    @staticmethod
    def exists(first_name, last_name):
        for client in Client.clients:
            if client.first_name == first_name and client.last_name == last_name:
                return True
        #not created i came there
        return False

    @staticmethod
    def get_client(first_name, last_name):
        for client in Client.clients:
            if client.first_name == first_name and client.last_name == last_name:
                return client
        # not created i came there
        return False

    def get_history_by_date(self, date : datetime.date):
        history_list_by_date : List['history'] = list()
        for history in self.history_list:
            if history.date == date:
                history_list_by_date.append(history)
        return history_list_by_date