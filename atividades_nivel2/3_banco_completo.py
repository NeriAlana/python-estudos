# Banco completo

# Menu:

# 1 - Ver saldo
# 2 - Depositar
# 3 - Sacar
# 4 - Transferir
# 5 - Extrato
# 6 - Sair

# Regras:

# saldo inicial = 1000
# guardar histórico:
# depósitos
# saques
# transferências
# mostrar extrato completo

saldo_conta = 1000.00
saldo_poupança = 0.00
extrato = []

while True:
    opcao = input('\nMenu:\n'

    '1 - Ver saldo\n'
    '2 - Depositar\n'
    '3 - Sacar\n'
    '4 - Transferir\n'
    '5 - Extrato\n'
    '6 - Sair\n')

    if opcao == '6':
        print('Finalizando...')
        break

    if opcao not in ['1', '2', '3', '4', '5', '6']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '1':
        print(f'o saldo é {saldo_conta:.2f}')

    elif opcao == '2':
        depositar = int(input('Digite o valor que deseja depositar: '))
        saldo_conta += depositar
        extrato.append(f'depósito de R${depositar:.2f}')

    elif opcao == '3':
        sacar = int(input('Digite o valor que deseja sacar: '))
        saldo_conta -= sacar
        extrato.append(f'saque de -R${sacar:.2f}')

    elif opcao == '4':
        transferir = int(input('Digite o valor que deseja transferir para a conta poupança: '))
        saldo_conta -= transferir
        saldo_poupança += transferir
        extrato.append(f'transferência de -R${transferir:.2f}')
        print(f'R${transferir:.2f} transferido com sucesso')

    elif opcao == '5':
        print('Extrato:')
        for item in extrato:
            print(item)