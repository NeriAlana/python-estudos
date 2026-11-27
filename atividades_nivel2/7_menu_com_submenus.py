# Exercício 10 — Menu com submenus
# 1 - Matemática
# 2 - Texto
# 3 - Sair

# Se entrar em Matemática:

# 1 - Somar
# 2 - Multiplicar
# 3 - Voltar

# Se entrar em Texto:

# 1 - Contar letras
# 2 - Transformar em maiúsculo
# 3 - Voltar

letras = []
somar = 0
multiplicar = 0

while True:

    opcao = input(
        'MENU:\n'
    '1 - Matemática\n'
    '2 - Texto\n'
    '3 - Sair\n')

    if opcao not in ['1', '2', '3' ]:
        print('opção inválida! Tente novamente.')
        continue

    if opcao == '3':
        print('Sistema finalizado')
        break

    if opcao == '1':
        menu_matematica = input('Escolha a operação\n'
        '1 - Somar\n'
        '2 - Multiplicar\n'
        '3 - Voltar\n')

        if menu_matematica not in ['1', '2', '3']:
            print('Opção inválida! Tente novamente.')
            continue
        
        if opcao == '3':
            print('Voltando ao menu principal...')
            continue       

        if menu_matematica == '1':
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            somar = num1 + num2
            print(f'A soma entre {num1} e {num2} é: {somar}')
        
        if menu_matematica == '2':
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            multiplicar = 0
            multiplicar = num1 * num2
            print(f'A multiplicação entre {num1} e {num2} é: {multiplicar}')

        if menu_matematica == '3':
            print('Voltando ao menu principal...')
            continue
        
    if opcao == '2':
        menu_texto = input(
            '1 - Contar letras\n'
            '2 - Transformar em maiúsculo\n'
            '3 - Voltar\n')
        
        if menu_texto not in ['1', '2', '3']:
            print('Opção inválida! Tente novamente.')
            continue
        
        if menu_texto == '3':
            print('Voltando ao menu principal...')
            continue    
          
        if menu_texto == '1':
            texto = input('digite uma palavra:')
            letras = list(texto)
            print(f' A palavra {texto} tem {len(letras)} letras')
            
        if menu_texto == '2':
            texto = input('digite uma palavra em CAPS LOOK:')
            print(texto.lower())
            