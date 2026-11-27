# Calculadora infinita

# Menu:

# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair

# Regras:

# pedir 2 números
# mostrar resultado
# voltar ao menu

# Desafio:

# impedir divisão por zero



while True:
    opcao = input(
        'Menu:\n\n'

        '1 - Somar\n'
        '2 - Subtrair\n'
        '3 - Multiplicar\n'
        '4 - Dividir\n'
        '5 - Sair\n'
    )

    if opcao == '5':
        print('Encerrando a aplicação...\n')
        break
    if opcao not in ['1', '2', '3', '4']:
        print('Opção inválida! Tente novamente.\n')
        continue

    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    
    if opcao == '1':
        print(f'A soma entre {a} e {b} é {a+b} \n')

    elif opcao == '2':
        print(f'A subtração entre {a} e {b} é {a-b} \n')

    elif opcao == '3':
        print(f'A multiplicação entre {a} e {b} é {a*b} \n')

    elif opcao == '4':
        if b == 0:
            print('Não é possível fazer a divisão por 0. Tente novamente.\n')
        else:
            print(f'A divisão entre {a} e {b} é {a/b:.2f} \n')
    