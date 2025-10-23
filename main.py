#!/usr/bin/env python
# -*- coding: utf-8 -*-*
from history import History
from inventory import Inventory
from inventory_manager import InventoryManager
from person import Person
import datetime

def main_menu(sys: InventoryManager) -> None:
    """
    This is the main menu of the application.
    """
    while True:
        print('-' * 60)
        print(' ' * 15 + "Welcome to 'Au Bon Marché'!")
        print('-' * 60)
        print('Choose an option:')
        print('1 - Add new Customer')
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
            # insert the first name
            while True:
                first_name = input('[Costumer manager] Insert costumer first name: ').strip().lower()
                first_name = ''.join(char for char in first_name if char.isalpha()).capitalize()
                if first_name and len(first_name) >= 3:
                    break
                print('Please enter a valid first name. At least 3 characters long.')

            while True:
                # insert the last name
                last_name = input('[Costumer manager] Insert costumer last name: ').strip().lower()
                last_name = ''.join(char for char in last_name if char.isalpha()).capitalize()
                if last_name and len(last_name) >= 3:
                    break
                print('Please enter a valid last name. At least 3 characters long.')

            if not Person.exists(first_name, last_name):
                Person.clients.append(Person(first_name, last_name))
                print(f'[Costumer manager] {first_name} {last_name} added to the system.')
            else:
                print(f'[Costumer manager] {first_name} {last_name} already exist.')

        if option == 2:
            client = login()
            print(f'[Debug] {client}')
        if option == 3:
            sys.display_inventory()

        if option == 4:
            history_today = History.get_by_date(datetime.datetime.now().date())
            for ht in history_today:
                print(ht.articles_list.display_inventory())

        if option == 5:
            print('Thank you for shopping! See you soon!')
            break


def login():
    """
    Function to login or register the client into the system
    :param first_name: string / First name of the flient
    :param last_name: string / Last name of the client
    :return: the client itself
    """
    # insert the first name
    while True:
        first_name = input('[Costumer manager] Insert costumer first name: ').strip().lower()
        first_name = ''.join(char for char in first_name if char.isalpha()).capitalize()
        if first_name and len(first_name) >= 3:
            break
        print('Please enter a valid first name. At least 3 characters long.')

    while True:
        # insert the last name
        last_name = input('[Costumer manager] Insert costumer last name: ').strip().lower()
        last_name = ''.join(char for char in last_name if char.isalpha()).capitalize()
        if last_name and len(last_name) >= 3:
            break
        print('Please enter a valid last name. At least 3 characters long.')

    if not Person.exists(first_name, last_name):
        Person.clients.append(Person(first_name, last_name))
        print(f'[Register] {first_name} {last_name} has been created')

    client = Person.get_client(first_name, last_name)
    print(f'[Login] Welcome {client.first_name} {client.last_name}')
    return client


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
