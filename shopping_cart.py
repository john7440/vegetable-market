from dataclasses import dataclass
from inventory import Inventory
from inventory_manager import InventoryManager
from person import Person
from history import History


@dataclass
class ShoppingCart:
    articles_list : InventoryManager
    owner : Person


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
        self.owner.history_list.append(self.articles_list)