# Desafio 7 — Filmes

# Cada filme possui:

# nome
# gênero

# Menu:

# 1 - Cadastrar filme
# 2 - Mostrar filmes
# 3 - Sair

# from pprint import pprint
import os 

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

filmes = []


while True:

    opcao = input('Menu:\n'

    '1 - Cadastrar filme\n'
    '2 - Mostrar filmes\n'
    '3 - Sair\n')

    limpa_tela()
    
    if opcao not in ['1', '2', '3']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '3':
        print('Encerrando a aplicação...')
        break

    if opcao == '1':
        filme = input('Informe o nome do filme a ser cadastrado: ')
        genero = input('Informe o gênero do filme: ')
        filmes.append({"nome":filme,
        "gênero":genero})

    if opcao == '2':
        for filme in filmes:
            print(f'Nome: {filme["nome"]} | Gênero: {filme["gênero"]}')