from __future__ import annotations
from typing import List
from dataclasses import dataclass
import datetime

from person import Person

@dataclass
class History:
    articles_list : 'InventoryManager'
    owner : 'Person'
    date : datetime.date


    @staticmethod
    def get_by_date(date : datetime.date):
        list_of_article_by_date : List['InventoryManager'] = list()
        users = Person.clients

        for u in users:
            list_of_article_by_date += u.get_history_by_date(date)

        return list_of_article_by_date