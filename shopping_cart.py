import datetime
from dataclasses import dataclass, field
from typing import Optional

from history import History
from inventory import Inventory
from inventory_manager import InventoryManager
from client import Client


@dataclass
class ShoppingCart:
    owner: Client
    articles_list: 'InventoryManager' = field(default_factory=InventoryManager)


    def add_article(self, article : Inventory, quantity : int):
        try:
            sold_article_price = article.sell(quantity)
            #create the article inside
            self.articles_list.add_item(Inventory(article.product, quantity, sold_article_price, article.sale_type, article.category))
        except ValueError as error:
            print(f'{error}')


    def get_total_price(self):
        return  sum(item.total_value() for item in self.articles_list.items)


    def display_cart(self):
        return self.articles_list.display_inventory()


    def pay(self):
        self.owner.history_list.append(History(self.articles_list, self.owner, datetime.datetime.now().date()))