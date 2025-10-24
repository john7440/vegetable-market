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
    history_list : List['History'] = field(default_factory=list)  # type: ignore

    def __post_init__(self):
        """
        This function initialise the shopping cart.
        """
        from shopping_cart import ShoppingCart
        self.shopping_cart = ShoppingCart(owner=self)

    #static
    clients: ClassVar[List['Client']] = []


    def get_histories(self) -> str:
        """
        This function list the buying history.
        :return: A list of the buying history.
        """
        histories_list = ''
        for i in range(len(self.history_list)):
            histories_list += str(i) + '\n'
        return histories_list


    def get_history_n(self, number : int) -> str:
        """
        This function list the buying history by index.
        :param number: the index of the buying history.
        :return: Inventory details or error message.
        """
        if 0 <= number <= len(self.history_list)-1:
            return self.history_list[number].articles_list.display_inventory()  # type: ignore
        else:
            return 'no available history number'


    @staticmethod
    def exists(first_name: str, last_name: str) -> bool:
        """
        This function check if a client exists.
        :param first_name: client first name.
        :param last_name: client last name.
        :return: True if client exists, False otherwise.
        """
        for client in Client.clients:
            if client.first_name == first_name and client.last_name == last_name:
                return True
        return False


    @staticmethod
    def get_client(first_name: str, last_name: str) -> Optional[Client]:
        """
        This function get a client by its first name and last name.
        :param first_name: first name of the client.
        :param last_name: last name of the client.
        :return: the client if exists, None otherwise.
        """
        for client in Client.clients:
            if client.first_name == first_name and client.last_name == last_name:
                return client
        return None

    def get_history_by_date(self, date : datetime.date) -> List[History]:  # type: ignore
        """
        This function list the buying history by date.
        :param date: The date to filter in history.
        :return: a list of history matching date.
        """
        history_list_by_date : List['history'] = []  # type: ignore
        for history in self.history_list:
            if history.date == date:
                history_list_by_date.append(history)
        return history_list_by_date