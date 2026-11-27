# Menu infinito
# Crie:

# 1 - Ver saldo
# 2 - Depositar
# 3 - Sair

# O programa só encerra quando escolher “3”



print('escolha uma opção: ')
saldo = 0

while True:
    opcao = input(
        '1 - Ver saldo\n'
        '2 - Depositar\n'
        '3 - Sair\n')

    if opcao == '1':
        print(f'Seu saldo é: R${saldo}')
    elif opcao == '2':
        deposito = float(input(f'Digite o valor a ser depositado: R$ '))
        saldo = deposito + saldo
    elif opcao == '3':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')