# Desafio 10 — Pessoas

# Cada pessoa possui:

# nome
# idade

# Menu:

# 1 - Cadastrar
# 2 - Mostrar maiores de idade
# 3 - Mostrar menores de idade
# 4 - Mostrar todos
# 5 - Sair


import os
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

people = []

while True:

    option = input('Menu:\n'
    '1 - Register\n'
    '2 - Show adults\n'
    '3 - Show minors\n'
    '4 - Show all\n'
    '5 - Exit\n')

    clear_window()
    
    if option not in ['1', '2', '3', '4', '5']:
        print('	Option invalid! try again.')
        continue


    if option == '5':
        print(' Application exited')
        break

    if option == '1':
        name = input('Enter your name: ')
        age = int(input('Enter your age: '))
        if name == '' or age == 0:
            print('Invalid name or age! Try again.')
            continue
        people.append({"name": name, "age": age})

    if option == '2':
        adults = [person for person in people if person["age"] >= 18]
        if adults:
            print('ADULTS')
            for person in adults:
                pprint(f'{person["name"]}, age {person["age"]}')
        else:
            print('No minors registered!')

    if option == '3':
        minors = [person for person in people if person["age"] < 18]
        if minors:
            print('MINORS')
            for person in minors:
                pprint(f'{person["name"]}, age {person["age"]}')
        else:
                print('No minors registered!')

    if option == '4':
            if people:
                print('ALL PEOPLE')
                for person in people:
                    pprint(f' Name: {person["name"]}, age: {person["age"]}')
            else:
                print('No people registered!')