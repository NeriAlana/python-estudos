# Contador de pessoas

# Menu:

# 1 - Adicionar pessoa
# 2 - Ver total de pessoas
# 3 - Resetar contador
# 4 - Sair

pessoas = []

while True:
    opcao = input(
    '1 - Adicionar pessoa\n'
    '2 - Ver total de pessoas\n'
    '3 - Resetar contador\n'
    '4 - Sair\n'
    '5 - mostrar lista\n\n')

    if opcao == '1':
        adicionar = input('Informe o nome da pessoa a ser adicionada: ')
        pessoas.append(adicionar)

    elif opcao == '2':
        print(f'o total de pessoas é {len(pessoas)}')

    elif opcao == '3':
        pessoas = []  #OU pessoas.clear()
    elif opcao == '5':
        print(pessoas)

    else:
        print('encerrando a aplicação...')
        break







		