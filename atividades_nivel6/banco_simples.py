# Desafio 15 — Banco simples

# Cada cliente possui:

# nome
# saldo

# Menu:

# 1 - Cadastrar cliente
# 2 - Depositar
# 3 - Sacar
# 4 - Ver clientes
# 5 - Sair


import os
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')


custumers = []

while True:

    option = input(
    'Menu:\n'
    '1 - Register custumers\n'
    '2 - Deposit\n'
    '3 - Withdraw\n'
    '4 - Show custumers\n'
    '5 - Exit\n')

    clear_window()

    if option not in ['1', '2', '3', '4', '5']:
        print('Invalid option" Tray again!\n')
        continue

    if option == '5':
        print('Exited application')
        break

    if option == '1':
        name = input('Enter your name: ')
        balance = 0
        print(f'custumer {name} registered successfully\n')
        custumers.append({"name" : name, "balance" : balance})

    if option == '2':
        while True:
            custumer_name = input('Register the custumer name: \n')
                                  
            
            for custumer in custumers:
                if custumer_name == custumer["name"]: 
                    balance_bank = float(input('Enter the value to add: '))
                    custumer["balance"] = custumer["balance"] + balance_bank
                    print('Deposit made successfully!\n')
                    break
            else:
                print('custumer not found! Tray again.\n')
                    
            option = input('Enter for continue or 2 - Back to menu\n')    
            if option == '2':
                break
            
                

    if option == '3':
        while True:
            custumer_name = input('Enter the custumer name: \n')
            
          
            for custumer in custumers:
                
                if custumer_name == custumer["name"]:
                    withdraw_bank = float(input('Enter the value to be withdrawn: \n'))
                    if withdraw_bank > custumer["balance"]:
                        print(f'Insufficient balance! Your balance is R${custumer["balance"]} \n')
                        break
                    else:
                        custumer["balance"] = custumer["balance"] - withdraw_bank
                        print('Withdraw made successfully!\n')
                        break
            else:
                print(f'custumer {custumer_name} not found! Tray again.\n')
            
            option = input('Enter for continue or 2 - Back to menu\n')    
            if option == '2':
                break
                    
                
    if option == '4':
        for custumer in custumers:
            print(f'custumer: {custumer["name"]}, Balance: {custumer["balance"]}\n')
