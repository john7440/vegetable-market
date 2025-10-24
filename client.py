from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from typing import List, ClassVar, Optional, TYPE_CHECKING
from shopping_cart import ShoppingCart

if TYPE_CHECKING:
    from history_record import History


@dataclass
class Client:
    first_name : str
    last_name : str
    shopping_cart : Optional['ShoppingCart'] = field(init=False)
    history_list : List['History'] = field(default_factory=list)

    def __post_init__(self) -> None:
        """
        This function initialise the shopping cart.
        """
        from shopping_cart import ShoppingCart
        self.shopping_cart = ShoppingCart(owner=self)

    #static
    clients: ClassVar[List[Client]] = []


    def get_histories(self) -> str:
        """
        This function list the buying history.
        :return: A list of the buying history.
        """
        return '\n'.join(str(i) for i in range(len(self.history_list)))


    def get_history_n(self, number : int) -> str:
        """
        This function list the buying history by index.
        :param number: the index of the buying history.
        :return: Inventory details or error message.
        """
        if 0 <= number < len(self.history_list):
            return self.history_list[number].articles_list.display_inventory()
        return 'No available history number.'


    @staticmethod
    def exists(first_name: str, last_name: str) -> bool:
        """
        This function check if a client exists.
        :param first_name: client first name.
        :param last_name: client last name.
        :return: True if client exists, False otherwise.
        """
        return any(
            client.first_name == first_name and client.last_name == last_name
            for client in Client.clients
        )


    @staticmethod
    def get_client(first_name: str, last_name: str) -> Client | None:
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

    def get_history_by_date(self, date : datetime.date) -> List[History]:
        """
        This function list the buying history by date.
        :param date: The date to filter in history.
        :return: a list of history matching date.
        """
        return [history for history in self.history_list if history.date == date]