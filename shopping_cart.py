from __future__ import annotations
from dataclasses import dataclass, field
from product import Product
from inventory_manager import InventoryManager

@dataclass
class ShoppingCart:
    owner: 'Client'
    articles_list: 'InventoryManager' = field(default_factory=InventoryManager)


    def add_article(self, article : Product, quantity : int):
        try:
            article.sell(quantity)
            #create the article inside
            self.articles_list.add_item(Product(article.product, quantity, article.price, article.sale_type, article.category))
        except ValueError as error:
            print(f'{error}')


    def get_total_price(self):
        return  sum(item.total_value() for item in self.articles_list.items)


    def display_cart(self):
        return self.articles_list.display_inventory()


    def pay(self):
        from history import History
        self.owner.history_list.append(History(self.owner))
        self.articles_list.items.clear()

    def display(self) -> None:
        """Display the inventory product by product and
        the total value of the inventory"""
        print('=' * 60)
        print(f"{'Product':<20} | {'Quantity':<20} | {'Price':<20} ")
        print('-' * 60)
        for item in self.articles_list.items:
            print(item.display())
        print('=' * 60)
        total = sum(item.total_value() for item in self.articles_list.items)
        print(f'Total of shopping cart: {total:.2f} €')