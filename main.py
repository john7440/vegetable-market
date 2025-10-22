#!/usr/bin/env python
# -*- coding: utf-8 -*-*

from inventory import Inventory
from inventory_manager import InventoryManager


def main_menu(sys: InventoryManager) -> None:
    """
    This is the main menu of the application.
    """
    while True:
        print('-' * 60)
        print('Welcome to Bon Marché!')
        print('-' * 60)
        print('Choose an option:')
        print('1 - Add new Customer')
        print('2 - Shopping')
        print('3 - Display Inventory')
        print('4 - Daily Sales')
        print('5 - Exit')
        print('-' * 60)
        option = int(input('Enter your choice: '))
        if option == 1:
            pass
        if option == 2:
            pass
        if option == 3:
            sys.display_inventory()
        if option == 4:
            pass
        if option == 5:
            break



def main():
    """
    This is the main function.
    """
    # Initiation of the system
    sys = InventoryManager()

    #Add to inventory
    sys.add_item(Inventory(product ='Clémentine', stock = 6.0, price = 2.90, sale_type= 'kg', category= 'fruit'))
    sys.add_item(Inventory(product='Datte', stock= 4.0, price= 7.0, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Grenade', stock= 3.0, price= 3.5, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Kaki', stock= 3.0, price= 4.5, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Kiwi', stock= 5.0, price= 3.5, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Mandarine', stock= 6.0, price= 2.8, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Orange', stock= 8.0, price= 1.5, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Pamplemousse', stock= 8.0, price= 2.0, sale_type='unit', category='fruit'))
    sys.add_item(Inventory(product='Poire', stock= 5.0, price= 2.5, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Pomme', stock= 8.0, price= 1.5, sale_type='kg', category='fruit'))
    sys.add_item(Inventory(product='Carotte', stock= 7.0, price= 1.3, sale_type='kg', category='vegetable'))
    sys.add_item(Inventory(product='Choux de Bruxelles', stock= 4.0, price= 4.0, sale_type='kg', category='vegetable'))
    sys.add_item(Inventory(product='Chou vert', stock= 12.0, price= 2.5, sale_type='unit', category='vegetable'))
    sys.add_item(Inventory(product='Courge butternut', stock= 6.0, price= 2.5, sale_type='unit', category='vegetable'))
    sys.add_item(Inventory(product='Endive', stock= 5.0, price= 2.5, sale_type='kg', category='vegetable'))
    sys.add_item(Inventory(product='Épinard', stock= 4.0, price= 2.6, sale_type='kg', category='vegetable'))
    sys.add_item(Inventory(product='Poireau', stock= 5.0, price= 1.2, sale_type='kg', category='vegetable'))
    sys.add_item(Inventory(product='Potiron', stock= 6.0, price= 2.5, sale_type='unit', category='vegetable'))
    sys.add_item(Inventory(product='Radis noir', stock= 10.0, price= 5.0, sale_type='unit', category='vegetable'))
    sys.add_item(Inventory(product='Salsifis', stock= 3.0, price= 2.5, sale_type='kg', category='vegetable'))

    main_menu(sys)

if __name__ == '__main__':
    main()