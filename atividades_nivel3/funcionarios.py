# Desafio 8 — Funcionários

# Cada funcionário possui:

# nome
# salário

# Menu:

# 1 - Cadastrar
# 2 - Mostrar funcionários
# 3 - Mostrar salários
# 4 - Sair

from pprint import pprint
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


funcionarios = []

while True:


    opcao = input('Menu:\n'

    '1 - Cadastrar\n'
    '2 - Mostrar funcionários\n'
    '3 - Mostrar salários\n'
    '4 - Sair\n')
    
    limpa_tela()

    if opcao not in ['1', '2', '3', '4']:
        print('Option invalid! tray again.')
        continue

    if opcao == '4':
        print('closing application...')
        break

    if opcao == '1':
        name = input('Informe o nome d funcionário a ser cadastrado: ')
        salario = input(f'Informe o valor do salário do funcionário {name}: ')
        funcionarios.append({"name" : name, "salario" : salario})

    if opcao == '2':
        for funcionario in funcionarios:
            pprint(funcionario['name'])

    if opcao == '3':
        for funcionario in funcionarios:
            pprint(funcionario['salario'])

















