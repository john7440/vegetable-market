from __future__ import annotations
from copy import deepcopy
from typing import List
from dataclasses import dataclass, field
import datetime


@dataclass
class History:
    """
    This class represents a snapshot of a client's shopping history at a
    specific date.
    """
    from inventory_manager import InventoryManager
    from client import Client

    owner: Client
    articles_list : 'InventoryManager' = field(default_factory=InventoryManager)
    date : datetime.date = field(default_factory=datetime.date.today)


    def __post_init__(self) -> None:
        """
        This method initializes the history by coping the current shopping cart
        of the client.
        """
        self.articles_list = deepcopy(self.owner.shopping_cart.articles_list)  # type: ignore


    @staticmethod
    def get_by_date(date : datetime.date) -> List[History]:
        """
        This method retrieves all history across all client that
        matches the given date.
        :param date: The date to retrieve history for.
        :return: A list of History entries.
        """
        from client import Client
        list_of_article_by_date : List['History'] = list()
        users = Client.clients

        for u in users:
            list_of_article_by_date += u.get_history_by_date(date)

        return list_of_article_by_date