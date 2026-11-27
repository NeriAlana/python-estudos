# Desafio 13 — Jogos

# Cada jogo possui:

# nome
# plataforma

# Permita pesquisar pelo nome.



import os
from pprint import pprint

def clear_window():
    os.system('cls' if os.name == 'nt' else 'clear')

games = []

while True:

    option = input('Menu\n'
    '1 - Register game\n'
    '2 - Find game\n'
    '3 - exit\n')  
    
    clear_window() 

    if option not in ['1', '2', '3']:
        print('Option invalid! Try again\n')
        continue

    if option == '3':
        print('Application exited.\n')
        break

    if option == '1':
        name = input('Enter game name: \n')
        platform = input('Enter platform name : \n')

        if name != '' and platform != '':
            games.append({"name" : name, "platform" : platform})
        else:
            print('Invalid data! Try again\n')


    if option == '2':
        found = input('\nEnter the name of the game are you looking for: \n')
        for game in games:
            if found == game["name"]:
                print(f'\nGame name:{game["name"]} \nPlatform:{game["platform"]}')

        if found != game["name"]:
            print('Game not found! Try again.\n')

























