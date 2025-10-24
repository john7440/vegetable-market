#!/usr/bin/env python
# -*- coding: utf-8 -*-*

from history import History
from product import Product
from inventory_manager import InventoryManager
from client import Client
import datetime


def main_menu(sys: InventoryManager) -> None:
    """
    This is the main menu, it gives the 5 options to the user.
    """
    client : Client | None = None
    """
    This is the main menu of the application.
    """
    while True:
        print('-' * 60)
        print(' ' * 15 + "Welcome to 'Au Bon Marché'!")
        print('-' * 60)
        print('Choose an option:')
        print('1 - Log In / New client')
        print('2 - Shopping')
        print('3 - Display Inventory')
        print('4 - Daily Sales')
        print('5 - Exit')
        print('-' * 60)

        while True:
            try:
                option = int(input('Enter your choice: '))
                if option in range(1, 6):
                    break
                else:
                    print('Invalid choice, please enter a number between 1 and 5')
            except ValueError:
                print('Invalid choice, please try again.')

        if option == 1:
            client = get_or_create_client()
            print(f'{client.first_name} {client.last_name} is now active.')

        if option == 2:
            shopping(client, sys)

        if option == 3:
            sys.display_inventory()

        if option == 4:
            history_today = History.get_by_date(datetime.datetime.now().date())
            for h in history_today:
                print('-'*60)
                print(h.owner.first_name,h.owner.last_name)
                h.articles_list.display_inventory()

        if option == 5:
            print('Thank you for shopping! See you soon!')
            break


def shopping(client: Client | None , sys: InventoryManager) -> None:
    """
    Handles the shopping process for a logged-in client.
    Displays inventory, manages item selection, quantity validation, and payment.
    """
    if not client:
        print('[Error] Please log in before shopping.')
        return

    print('-' * 60)
    print(f"[Shopping] Welcome {client.first_name} {client.last_name}!")
    sys.display_inventory()

    while True:
        article_name = input('Insert the article name: ').strip().capitalize()
        article = sys.get_item(article_name)

        if not article:
            print(f"[Error] '{article_name}' does not exist in inventory.")
            continue

        quantity_input = input(f"Insert the desired quantity of {article.product} in {article.sale_type}: ").strip()
        try:
            quantity = int(quantity_input)
            if quantity <= 0:
                print("[Error] Quantity must be a positive number.")
                continue
            if quantity > article.stock:
                print(f"[Error] Not enough stock for {article.product}. Available: {article.stock}")
                continue
        except ValueError:
            print("[Error] Invalid quantity. Please enter a number.")
            continue

        # Check if item already in cart
        existing_item = next((item for item in client.shopping_cart.articles_list.items if item.product == article.product), None)  # type: ignore

        article.sell(quantity)

        article_copy = Product(
            product=article.product,
            stock=quantity,
            price=article.price,
            sale_type=article.sale_type,
            category=article.category
        )

        if existing_item:
            existing_item.stock += quantity
            print(f"[Update] Added {quantity} more of {article.product} to your cart.")
        else:
            client.shopping_cart.add_article(article_copy, quantity)  # type: ignore
            print(f"[Add] {article.product} has been added to your shopping cart.")

        print('-' * 60)
        client.shopping_cart.display()  # type: ignore

        pay_state = input('Do you want to pay and exit? (yes/no): ').strip().lower()
        if pay_state in ['y', 'yes', 'oui', 'o']:
            client.shopping_cart.pay()  # type: ignore
            print("[Checkout] Thank you for your purchase!")
            break


def get_valid_name(label: str) -> str:
    """
    Prompt the user for a valid name (first or last).
    Removes non-alphabetic characters and ensures minimum length.
    """
    while True:
        name = input(f'Insert customer {label} name: ').strip().lower()
        name = ''.join(char for char in name if char.isalpha()).capitalize()
        if name and len(name) >= 3:
            return name
        print(f'Please enter a valid {label} name. At least 3 characters long.')


def get_or_create_client() -> Client:
    """
    Ask for first and last name, create the client if not found, or return existing one.
    """
    first_name = get_valid_name("first")
    last_name = get_valid_name("last")

    if not Client.exists(first_name, last_name):
        Client.clients.append(Client(first_name, last_name))
        print(f'[Register] {first_name} {last_name} has been created')
    else:
        print(f'[Login] Welcome back {first_name} {last_name}')

    return Client.get_client(first_name, last_name)  # type: ignore


def main():
    """
    This is the main function.
    """
    # Initiation of the manager
    manager = InventoryManager()

    #Add to inventory
    manager.add_item(Product(product ='Clémentine', stock = 6.0, price = 2.90, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Datte', stock= 4.0, price= 7.0, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Grenade', stock= 3.0, price= 3.5, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Kaki', stock= 3.0, price= 4.5, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Kiwi', stock= 5.0, price= 3.5, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Mandarine', stock= 6.0, price= 2.8, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Orange', stock= 8.0, price= 1.5, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Pamplemousse', stock= 8.0, price= 2.0, sale_type='unit', category='fruit'))
    manager.add_item(Product(product='Poire', stock= 5.0, price= 2.5, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Pomme', stock= 8.0, price= 1.5, sale_type='kg', category='fruit'))
    manager.add_item(Product(product='Carotte', stock= 7.0, price= 1.3, sale_type='kg', category='vegetable'))
    manager.add_item(Product(product='Choux de Bruxelles', stock= 4.0, price= 4.0, sale_type='kg', category='vegetable'))
    manager.add_item(Product(product='Chou vert', stock= 12.0, price= 2.5, sale_type='unit', category='vegetable'))
    manager.add_item(Product(product='Courge butternut', stock= 6.0, price= 2.5, sale_type='unit', category='vegetable'))
    manager.add_item(Product(product='Endive', stock= 5.0, price= 2.5, sale_type='kg', category='vegetable'))
    manager.add_item(Product(product='Épinard', stock= 4.0, price= 2.6, sale_type='kg', category='vegetable'))
    manager.add_item(Product(product='Poireau', stock= 5.0, price= 1.2, sale_type='kg', category='vegetable'))
    manager.add_item(Product(product='Potiron', stock= 6.0, price= 2.5, sale_type='unit', category='vegetable'))
    manager.add_item(Product(product='Radis noir', stock= 10.0, price= 5.0, sale_type='unit', category='vegetable'))
    manager.add_item(Product(product='Salsifis', stock= 3.0, price= 2.5, sale_type='kg', category='vegetable'))

    # Main menu loop
    main_menu(manager)


if __name__ == '__main__':
    main()
