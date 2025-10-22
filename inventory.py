from dataclasses import dataclass
from typing import Literal


@dataclass
class Inventory:
    """
    This class is made to manage products
    (vegetables and fruits), we have a definite
    stock and a price per unit or per kg.
    """
    product: str
    stock: float
    price: float
    sale_type: Literal['unit', 'kg']
    category: Literal['fruit', 'vegetable']
    # ex utilisation : kiwi = Inventory('Kiwi', stock = 5.0, price = 3.5, sale_type = 'kg', category = 'fruit')
                    #  potiron = Inventory('Potiron', stock = 6.0, price = 2.5, sale_type = 'unit', category = 'vegetable')


    def sell(self, quantity: float) -> float:
        """
        This function check if the quantity is available
        for the sell to succeed. If not or if the quantity is incorrect
        then it raise an error.
        :param quantity: the quantity to sell.
        :return: quantity * price (if available)
        """
        if quantity <= 0:
            raise ValueError('Quantity must be positive')
        if quantity > self.stock:
            raise ValueError('Quantity cannot be greater than stock')
        self.stock -= quantity
        return quantity * self.price


    def display(self) -> str:
        """
        This function display the product with the unit modified
        according to the sale type.
        :return: a formatted string.
        """
        unit = "unit" if self.sale_type == 'unit' else "kg"
        return f'{self.product:<20} | {self.stock:14.2f} {unit:5} |    {self.price:.2f} {unit}/€'


    def total_value(self) -> float:
        """
        This function calculates the total value of the inventory.
        :return: the value of the inventory.
        """
        return self.price * self.stock
