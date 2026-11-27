# Desafio 14 — Sistema de estoque

# Cada produto possui:

# nome
# quantidade

# Menu:

# 1 - Cadastrar
# 2 - Adicionar estoque
# 3 - Retirar estoque
# 4 - Mostrar estoque
# 5 - Sair


import os
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

products = []

while True:

    option = input('Menu:\n'

    '1 - Register\n'
    '2 - Add stock\n'
    '3 - Remove from stok\n'
    '4 - Show stock\n'
    '5 - Exit\n')

    clear_window()

    if option not in ['1', '2', '3', '4','5']:
        print('Option invalid! Try again.')
        continue

    if option == '5':
        print('Exited application.')
        break

    if option == '1':
        name = input('Enter product name: ')
        quantity = int(input('Specify the quantity of this product: '))
        if name == '' or quantity == 0:
            print('Name or quantity of product invalid! Tray again.\n')
        else:
            products.append({"name" : name, "quantity" : quantity})


    if option == '2':
        print('REGISTERED PRODUCTS: ')
        for product in products:
            pprint(f'Product: {product["name"]} Quantity: {product["quantity"]}\n')

        
        add_stock = input('Enter product name to add to stock: ')
        if add_stock != product["name"]:
            print(f'Product {product["name"]} not found.\n')
        else:
            quantity_product = int(input('Enter the quantity of this product: '))
        
        for product in products:
            if add_stock == product["name"]:
                product["quantity"] = product["quantity"] + quantity_product
                print(f'The product {product["name"]} was added successfully.\n')

    if option == '3':
        print('REGISTERED PRODUCTS: ')
        for product in products:
            pprint(f'Product: {product["name"]}, Quantity: {product["quantity"]}\n')

        remove_stock = input('Enter the product name to remove it from stock: \n')
        if remove_stock != product["name"]:
            print(f'Product {product["name"]} not found.\n')
        else:
            quantity_product = int(input('Enter the quantity of this product: '))

        for product in products:
            if remove_stock == product["name"]:
                if quantity_product > product["quantity"]:
                    print('Cannot remove a quantity greater than available stock')
                else:
                    product["quantity"] = product["quantity"] - quantity_product
                    print('Product removed successfully.')    
           

    if option == '4':
        print('STOCK: ')
        for product in products:
            if product["name"] == '' or product["quantity"] == 0:
                print('No products in stock.')    
            else:
                pprint(f'Product: {product["name"]}, Quantity: {product["quantity"]}')