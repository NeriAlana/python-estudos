# Desafio 12 — Agenda

# Cada contato possui:

# nome
# telefone

# Menu:

# 1 - Cadastrar
# 2 - Buscar contato
# 3 - Mostrar todos
# 4 - Sair

import os 
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

contacts = []

while True:

    option = input('Menu: \n'
    '1 - Register\n'
    '2 - Find a contact\n'
    '3 - Show all\n'
    '4 - Exit\n')

    clear_window()

    if option not in ['1', '2', '3', '4']:
        print('Option invalid! Try again.\n')
        continue

    if option == '4':
        print('Application exited')
        break

    if option == '1':
        name = input('Enter your name: ')
        phone = input('Enter your phone number: ')
        if name != '' and phone != '' :
            contacts.append({"name" : name, "phone" : phone})
        else:
            print(f'Name or phone number invalid" Tray again\n')
            

    if option == '2':
        search_contact = input('Enter the phone number to search: \n')
        for contact in contacts:
            if search_contact == contact["phone"]:
                print(f'Foud contact:\n'
                f'Name: {contact["name"]}.\nPhone number:{contact["phone"]}') 
        if search_contact != contact["phone"]:
            print('Phone number not foud! Try again.\n')
                

    if option == '3':
        print(f'\nCONTACTS LIST\n')
        for contact in contacts:
            pprint(f'Name:{contact["name"]} | Phone Number:{contact["phone"]}\n')
























