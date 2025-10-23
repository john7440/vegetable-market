from __future__ import annotations

from copy import deepcopy
from typing import List
from dataclasses import dataclass, field
import datetime


@dataclass
class History:
    from inventory_manager import InventoryManager
    from client import Client
    owner: Client
    articles_list : 'InventoryManager' = field(default_factory=InventoryManager)
    date : datetime.date = field(default_factory=datetime.date.today)

    def __post_init__(self):
        self.articles_list = deepcopy(self.owner.shopping_cart.articles_list)


    @staticmethod
    def get_by_date(date : datetime.date):
        from client import Client
        list_of_article_by_date : List['History'] = list()
        users = Client.clients

        for u in users:
            list_of_article_by_date += u.get_history_by_date(date)

        return list_of_article_by_date