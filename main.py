#!/usr/bin/env python
# -*- coding: utf-8 -*-*

from history_record import History
from product import Product
from inventory_manager import InventoryManager
from client import Client
import datetime


def main_menu(manager: InventoryManager) -> None:
    """
    This is the main menu, it gives the 5 options to the user.
    """
    client : Client | None = None
    while True:
        print('')
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

        option: int
        while True:
            try:
                option = int(input('Enter your choice: '))
                if option in range(1, 6):
                    break
                else:
                    print('\nInvalid choice, please enter a number between 1 and 5')
            except ValueError:
                print('\nInvalid choice, please try again.')

        match option:
            case 1:
                client = get_or_create_client()
                if client is not None:
                    print(f'{client.first_name} {client.last_name} is now active.')

            case 2:
                shopping(client, manager)

            case 3:
                print(manager.display_inventory())

            case 4:
                history_today = History.get_by_date(datetime.datetime.now().date())
                print('-----------------------Today\'s Resume-----------------------')
                for h in history_today:
                    print('-'*60)
                    print('Client: '+ h.owner.first_name,h.owner.last_name)
                    print(h.articles_list.display_inventory())

            case 5:
                print('\nThank you for shopping! See you soon!')
                break


def shopping(client: Client | None, manager: InventoryManager) -> None:
    """
    Handles the shopping process for a logged-in client.
    Displays inventory, manages item selection, quantity validation, and payment.
    :param manager:  InventoryManager.
    :type client: Client | None.
    """
    if not client:
        print('\n[Error] Please log in before shopping.')
        return

    print('-' * 60)
    print(f"\n[Shopping] Welcome {client.first_name} {client.last_name}!\n")
    print(manager.display_inventory())

    while True:
        article_name = input('\nInsert the article name: ').strip().capitalize()
        article = manager.get_item(article_name)

        if not article:
            print(f"[Error] '{article_name}' does not exist in inventory.")
            continue

        quantity_input = input(f"\nInsert the desired quantity of {article.product} in {article.sale_type}: ").strip()
        try:
            quantity = int(quantity_input)
            if quantity <= 0:
                print("\n[Error] Quantity must be a positive number.")
                continue
            if quantity > article.stock:
                print(f"\n[Error] Not enough stock for {article.product}. Available: {article.stock}")
                continue
        except ValueError:
            print("\n[Error] Invalid quantity. Please enter a number.")
            continue

        # Check if item already in cart
        if client is not None:
            existing_item = next(
                (item for item in client.shopping_cart.articles_list.items if item.product == article.product),
                None)

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
                print(f"\n[Update] Added {quantity} more of {article.product} to your cart.")
            else:
                client.shopping_cart.add_article(article_copy, quantity)
                print(f"\n[Add] {article.product} has been added to your shopping cart.")

        print('-' * 60)
        client.shopping_cart.display()

        pay_state = input('Do you want to pay and exit? (yes/no): ').strip().lower()
        if pay_state in ['y', 'yes', 'oui', 'o']:
            client.shopping_cart.pay()
            print("\n[Checkout] Thank you for your purchase!")
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


def get_or_create_client() -> Client | None:
    """
    Ask for first and last name, create the client if not found, or return existing one.
    :return: client or None.
    """
    first_name = get_valid_name("first")
    last_name = get_valid_name("last")

    if not Client.exists(first_name, last_name):
        Client.clients.append(Client(first_name, last_name))
        print(f'\n[Register] {first_name} {last_name} has been created')
    else:
        print(f'\n[Login] Welcome back {first_name} {last_name}')

    return Client.get_client(first_name, last_name)


def initialize_inventory(manager: InventoryManager) -> None:
    """
    Populates the inventory with predefined products.
    """
    products = [
        ("Clémentine", 6.0, 2.90, "kg", "fruit"),
        ("Datte", 4.0, 7.0, "kg", "fruit"),
        ("Grenade", 3.0, 3.5, "kg", "fruit"),
        ("Kaki", 3.0, 4.5, "kg", "fruit"),
        ("Kiwi", 5.0, 3.5, "kg", "fruit"),
        ("Mandarine", 6.0, 2.8, "kg", "fruit"),
        ("Orange", 8.0, 1.5, "kg", "fruit"),
        ("Pamplemousse", 8.0, 2.0, "unit", "fruit"),
        ("Poire", 5.0, 2.5, "kg", "fruit"),
        ("Pomme", 8.0, 1.5, "kg", "fruit"),
        ("Carotte", 7.0, 1.3, "kg", "vegetable"),
        ("Choux de Bruxelles", 4.0, 4.0, "kg", "vegetable"),
        ("Chou vert", 12.0, 2.5, "unit", "vegetable"),
        ("Courge butternut", 6.0, 2.5, "unit", "vegetable"),
        ("Endive", 5.0, 2.5, "kg", "vegetable"),
        ("Épinard", 4.0, 2.6, "kg", "vegetable"),
        ("Poireau", 5.0, 1.2, "kg", "vegetable"),
        ("Potiron", 6.0, 2.5, "unit", "vegetable"),
        ("Radis noir", 10.0, 5.0, "unit", "vegetable"),
        ("Salsifis", 3.0, 2.5, "kg", "vegetable"),
    ]

    for name, stock, price, sale_type, category in products:
        manager.add_item(Product(product=name, stock=stock, price=price, sale_type=sale_type, category=category))

def main():
    """
    This is the main function. It initializes inventory and launch
    the main menu.
    """
    manager = InventoryManager()
    initialize_inventory(manager)
    main_menu(manager)


if __name__ == '__main__':
    main()
