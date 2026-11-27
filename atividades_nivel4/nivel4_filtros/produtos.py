# Desafio 11 — Produtos

# Cada produto possui:

# nome
# preço

# Menu:

# 1 - Cadastrar
# 2 - Produtos acima de R$100
# 3 - Produtos abaixo de R$100
# 4 - Mostrar todos
# 5 - Sair



import os
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

products = []

while True:

    option = input('Menu:\n '
    '1 - Register\n'
    '2 - Products over R$100\n'
    '3 - Products below R$100\n'
    '4 - Show all\n'
    '5 - Exit\n')

    clear_window()
    
    if option not in ['1', '2', '3', '4', '5']:
        print('Option invalid! Tray again.')
        continue

    if option == '5':
        print('Application exited')
        break

    if option == '1':
        name = input('Enter the product name: ')
        price = float(input('Enter the product price: '))
        if name != '' and price > 0:
            products.append({"name" : name, "price" : price})
        else:
            print('Name or price invalid! Try again.')
            continue

    if option == '2':
        over = [product for product in products if product["price"] > 100]
        if over:
            for product in over:
                print(f'Product:{product["name"]}, Price: {product["price"]}')

    if option == '3':
        below = [product for product in products if product["price"] < 100]
        if below:
            for product in below:
                print(f'Product:{product["name"]}, Price: {product["price"]}')

    if option == '4':
        pprint(products)



























