# Desafio 18 — Loja

# Cada produto:

# nome
# preço
# quantidade

# Menu:

# 1 - Cadastrar produto
# 2 - Comprar
# 3 - Repor estoque
# 4 - Mostrar produtos
# 5 - Mostrar produtos sem estoque
# 6 - Sair


import os
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

stock = []

while True:

    option = input('Menu:\n'

    '1 - Register product\n'
    '2 - buy product\n'
    '3 - Restock\n'
    '4 - Show products\n'
    '5 - Show products out of stock\n'
    '6 - Exit\n')

    clear_window()

    if option not in ['1', '2', '3', '4', '5', '6']:
        print('Invalid opption! Try again.')
        continue

    if option == '6':
        print('Exited application...')
        break

    if option == '1':
        try:
            name = input('Enter product name: ').strip()
            if name == '':
                print('Product name cannot be empty!\n')
                continue
            for product in stock:
                if name == product["name"]:
                    print('Product already registered!\n')
                    break
            else:
                price = float(input('Enter product price: '))
                if price <= 0:
                    print('Price must be greater than zero!\n')
                    continue
                
                quantity = int(input('Enter product quantity: '))
                if quantity <= 0:
                    print('Product not registered! Please enter valid  quantity.\n')
                    continue
                
                stock.append({"name" : name, "price" : price, "quantity" : quantity})
                print(f'\nProduct {name} registered successfully!\n')
        except ValueError:
            print('Invalid input! Please enter a valid price or quantity.\n')
            continue

    if option == '2':
        try:
            if stock == []:
                print('No products registered!\n')
                continue
            
            print('STOCK')
            for product in stock:
                print(f' PRODUCT: {product["name"]} PRICE: {product["price"]}  QUANTITY: {product["quantity"]}\n')

            buy_product = input('Enter the product name you want to buy: \n').strip()
            
            if buy_product not in [product["name"] for product in stock]:
                print('Product not found!\n')
                continue
        
            for product in stock:
                if buy_product == product["name"] and product["quantity"] > 0:
                    quantity = int(input('Enter the quantity you want to buy: \n'))
                    if quantity <= 0 or quantity > product["quantity"]:
                        print(f'Enter the valid quantity!\n')
                    else:
                        product["quantity"] -= quantity
                        print(f'You bought {quantity} of {product["name"]} for {product["price"] * quantity:.2f}\n')
                elif buy_product == product["name"] and product["quantity"] == 0:
                    print(f'Product {product["name"]} is out of stock!\n')
        except ValueError:
            print('Invalid input! Please enter a valid quantity.\n')
            continue


    if option == '3':
        try:
            if stock == []:
                print('No products registered!\n')
                continue
            else:
                print('STOCK')
                for product in stock:
                    print(f'PRODUCT: {product["name"]} PRICE: {product["price"]}  QUANTITY: {product["quantity"]}') 
        
                restock = input('Enter the product name you want to restock: ').strip()
                
                if restock not in [product["name"] for product in stock]:
                    print('You cannot restock items that are not registered in stock!\n')
                
                for product in stock:
                    if restock == product["name"]:
                        quantity = int(input('Enter the quantity you want to restock: '))
                        if quantity > 0:
                            product["quantity"] += quantity
                            print(f'Restocked successfully! New quantity of {product["name"]} is {product["quantity"]}\n') 
                        else:
                            print('Quantity must be greater than zero!\n')
                continue
        except ValueError:
            print('Invalid input! Please enter a valid product name.\n')
            continue

    if option == '4':
        if stock == []:
            print('No products registered!\n')
            continue
        else:
            print('STOCK')
            for product in stock:
                print(f' PRODUCT: {product["name"]} PRICE: {product["price"]}  QUANTITY: {product["quantity"]}\n')
            
    if option == '5':
        if stock == []:
            print('No products registered!\n')
            continue
        else:
            print('PRODUCTS OUT OF STOCK')
            for product in stock:
                if product["quantity"] == 0:
                    print(f' PRODUCT: {product["name"]} PRICE: {product["price"]}  QUANTITY: {product["quantity"]}\n')


