#!/usr/bin/env python
# -*- coding: utf-8 -*-*
from sys import path_hooks

from history import History
from inventory import Inventory
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


def shopping(client: Client | None, sys: InventoryManager) -> None:
    """
    This function is called when a shopping cart is created.
    :param client: the actual client.
    :param sys: the InventoryManager.
    """
    if client:
        # show list
        sys.display_inventory()

        # ask product and quantity
        while True:
            # enter name of article
            article_name = input('Insert the article name: ').strip().capitalize()
            # get the item
            article = sys.get_item(article_name)
            # if item is got
            if article:
                # get desired quantity
                quantity = input(f"Insert the desired quantity of {article.product} in {article.sale_type}: ")
                # if the quantity is valid
                if quantity.isdigit() and int(quantity) <= article.stock:
                    # if the article is already present
                    if any(item.product == article.product for item in client.shopping_cart.articles_list.items):
                        quantity = int(quantity)

                        # Sell quantity
                        article.sell(quantity)

                        # Increase in our list
                        for sc_article in client.shopping_cart.articles_list.items:
                            if sc_article.product == article.product:
                                sc_article.stock += quantity
                    else:
                        # Sell
                        client.shopping_cart.add_article(article, int(quantity))
                        print(f'{article.product} has been added to your shopping cart')
                else:
                    print(f'We don\'t have enough {article_name} to sell')
                print('-' * 60)

            else:
                print(f'{article_name} don\'t exist')
            # Show my ticket
            client.shopping_cart.display()

            # Handle continue or stop
            pay_state = input('Do you want to pay and exit? (yes/no): ')

            if pay_state.lower() in ['y','yes','oui','o']:
                client.shopping_cart.pay()
                #exit the loop
                break
    else:
        print(' Please log-in the client before shopping')


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

    return Client.get_client(first_name, last_name)


def main():
    """
    This is the main function.
    """
    # Initiation of the manager
    manager = InventoryManager()

    #Add to inventory
    manager.add_item(Inventory(product ='Clémentine', stock = 6.0, price = 2.90, sale_type= 'kg', category= 'fruit'))
    manager.add_item(Inventory(product='Datte', stock= 4.0, price= 7.0, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Grenade', stock= 3.0, price= 3.5, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Kaki', stock= 3.0, price= 4.5, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Kiwi', stock= 5.0, price= 3.5, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Mandarine', stock= 6.0, price= 2.8, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Orange', stock= 8.0, price= 1.5, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Pamplemousse', stock= 8.0, price= 2.0, sale_type='unit', category='fruit'))
    manager.add_item(Inventory(product='Poire', stock= 5.0, price= 2.5, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Pomme', stock= 8.0, price= 1.5, sale_type='kg', category='fruit'))
    manager.add_item(Inventory(product='Carotte', stock= 7.0, price= 1.3, sale_type='kg', category='vegetable'))
    manager.add_item(Inventory(product='Choux de Bruxelles', stock= 4.0, price= 4.0, sale_type='kg', category='vegetable'))
    manager.add_item(Inventory(product='Chou vert', stock= 12.0, price= 2.5, sale_type='unit', category='vegetable'))
    manager.add_item(Inventory(product='Courge butternut', stock= 6.0, price= 2.5, sale_type='unit', category='vegetable'))
    manager.add_item(Inventory(product='Endive', stock= 5.0, price= 2.5, sale_type='kg', category='vegetable'))
    manager.add_item(Inventory(product='Épinard', stock= 4.0, price= 2.6, sale_type='kg', category='vegetable'))
    manager.add_item(Inventory(product='Poireau', stock= 5.0, price= 1.2, sale_type='kg', category='vegetable'))
    manager.add_item(Inventory(product='Potiron', stock= 6.0, price= 2.5, sale_type='unit', category='vegetable'))
    manager.add_item(Inventory(product='Radis noir', stock= 10.0, price= 5.0, sale_type='unit', category='vegetable'))
    manager.add_item(Inventory(product='Salsifis', stock= 3.0, price= 2.5, sale_type='kg', category='vegetable'))

    # Main menu loop
    main_menu(manager)


if __name__ == '__main__':
    main()
