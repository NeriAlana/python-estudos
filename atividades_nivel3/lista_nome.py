# Menu:

# 1 - Cadastrar nome
# 2 - Mostrar nomes
# 3 - Buscar nome
# 4 - Sair

# Se o nome existir:

# Nome encontrado!

# Caso contrário:

# Nome não encontrado.

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
nomes = []

while True:
    
    
    opcao = input('\n Escolha uma opção:\n'
    '1 - Cadastrar nome\n'
    '2 - Mostrar nomes\n'
    '3 - Buscar nome\n'
    '4 - Sair\n')

    limpar_tela()
    if opcao not in ['1', '2', '3', '4']:
        print('Opção inválida!! Tente novamente.')
        continue

    if opcao  == '4':
        print('Finalizando p programa...')
        break

    if opcao == '1':
        cadastrar_nome = input('Informe o número a ser cadastrado: ')
        nomes.append(cadastrar_nome)

    if opcao == '2':
        print(f'Nomes cadastrados: \n{nomes}')

    if opcao == '3':
        buscar_nome = input('Informe o nome a ser localizado: ')
        
        if buscar_nome  in nomes:
            print(f'Nome {buscar_nome} encontrado!')
        else:
            print(f'Nome {buscar_nome } não encontrado.')
            
