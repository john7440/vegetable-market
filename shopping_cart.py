from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from product_classe import Product
from inventory_manager import InventoryManager

if TYPE_CHECKING:
    from client import Client

@dataclass
class ShoppingCart:
    """
    This class represents a shopping cart associated with a client.
    It manages articles added to the cart and handles payment.
    """
    owner: Client
    articles_list: 'InventoryManager' = field(default_factory=InventoryManager)


    def add_article(self, article : Product, quantity : int) -> None:
        """
        This function adds an article to the cart after validation.
        :param article: the product to add.
        :param quantity: the quantity desired.
        :return: ValueError if the product is not available.
        """
        try:
            article.sell(quantity)
            #create the article inside
            self.articles_list.add_item(Product(article.name, quantity, article.price, article.sale_type, article.category))
        except ValueError as error:
            print(f'{error}')


    def get_total_price(self) -> float:
        """
        This function calculate the total price of the shopping cart.
        :return: the total price.
        """
        return  sum(item.total_value() for item in self.articles_list.items)


    def pay(self) -> None:
        """
        This function finalises the purchase and save the cart to the client's history.
        """
        from history_record import History
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
