# Sistema de temperatura

# Menu:

# 1 - Adicionar temperatura
# 2 - Ver maior temperatura
# 3 - Ver menor temperatura
# 4 - Ver média
# 5 - Sair

temperaturas = []
maior = 0
menor = 0
media = 0
soma = 0

while True:

    opcao = input('Menu:\n'

    '\n1 - Adicionar temperatura\n'
    '2 - Ver maior temperatura\n'
    '3 - Ver menor temperatura\n'
    '4 - Ver média\n'
    '5 - Sair\n')


    if opcao == '5':
        print('Encerrando aplicação...')
        break

    if opcao not in ['1', '2', '3', '4', '5']:
        print('opção inválida! Tente novamente')
        continue

    if opcao == '1':
        temperatura = int(input('Digite a temperatura a ser adicionada: \n'))
        temperaturas.append(temperatura)
        soma += temperatura

    elif opcao == '2':
        print(f'A maior temperatura registrada foi { max(temperaturas)}')

    elif opcao == '3':
        print(f'A menor temperatura registrada foi { min(temperaturas)}')

    elif opcao == '4':
        media = soma/len(temperaturas)
        print(f'A média de temperatura é {media:.0f}')