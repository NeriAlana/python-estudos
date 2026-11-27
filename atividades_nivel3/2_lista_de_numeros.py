# Menu:

# 1 - Adicionar número
# 2 - Mostrar números
# 3 - Mostrar maior número
# 4 - Mostrar menor número
# 5 - Sair

# ⚠️ Não use max() nem min().


numeros = []


while True:

    opcao = input('\nMenu:\n'

    '1 - Adicionar número\n'
    '2 - Mostrar números\n'
    '3 - Mostrar maior número\n'
    '4 - Mostrar menor número\n'
    '5 - Sair\n')

    if opcao not in ['1', '2', '3', '4', '5']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '5':
        print('Finalizando a aplicação...')
        break

    if opcao == '1':
        numero = int(input('Informe o número a ser adicionado: '))
        numeros.append(numero)
        print(f'O número {numero} foi adicionado com sucesso!')

    if opcao == '2':
        print(numeros)

    if opcao == '3':
        maior = numeros[0]
        for numero in numeros:
            if numero > maior:
                maior = numero
                
            else:
                numero = maior
        print(f'O maior número da lista é: {maior}')
    if opcao == '4':
        menor = numeros[0]
        for numero in numeros:
            if numero < menor:
                menor = numero
            else:
                numero = menor 
        print(f'O menor número da lista é: {menor}')