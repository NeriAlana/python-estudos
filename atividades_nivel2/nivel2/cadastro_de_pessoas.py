# Desafio 4 — Cadastro de uma pessoa

# Crie um sistema que armazene:

# nome
# idade
# profissão

# Menu:

# 1 - Cadastrar
# 2 - Mostrar cadastro
# 3 - Sair

# Agora você começa a entender como acessar:

# pessoa["nome"]

import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
pessoas = []

while True:

    opcao = input('Menu:\n'

    '1 - Cadastrar\n'
    '2 - Mostrar cadastro\n'
    '3 - Sair\n')

    limpar_tela()
    
    if opcao not in ['1', '2', '3']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '3':
        print('Aplicação finalizada')
        break

    if opcao == '1':
        nome = input('informe o nome a ser cadastrado: ')
        idade = input('informe sua idade: ')
        profissao = input('informe sua profissão: ')
        pessoas.append({"nome": nome,
        "idade": idade,
        "profissao": profissao
        })

    if opcao == '2':
        print('PESSOAS CADASTRADAS\n')
        print(pessoas)






