# Caixa eletrônico simples

# Crie um sistema com menu infinito:

# 1 - Ver saldo
# 2 - Depositar
# 3 - Sacar
# 4 - Sair

# Regras:

# saldo começa com R$1000
# não pode sacar mais que o saldo
# o programa só encerra no 4


saldo = 1000

while True:
    opcao = input('1 - Ver saldo\n'
                    '2 - Depositar\n'
                    '3 - Sacar\n'
                    '4 - Sair\n')
    if opcao == '1':
        print(f'Seu saldo é: {saldo}')
        
    elif opcao == '2':
        valor_depositado = float(input('Digite o valor a ser depositado: '))
        saldo += valor_depositado
    
    elif opcao == '3':
        valor_sacado = float(input('Digite o valor a ser sacado: '))
        if valor_sacado > saldo:
            print(f'Não é possível sacar um valor maior do que o seu saldo!\nSeu saldo é {saldo}\nTente novamente')
        else:
            saldo -= valor_sacado
    elif opcao == '4':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')