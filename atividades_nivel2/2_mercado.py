# Mercado

# Crie um sistema de compras.

# Menu:

# 1 - Adicionar produto
# 2 - Ver total da compra
# 3 - Finalizar compra

# Regras:

# usuário digita preço dos produtos
# acumular valor total
# ao finalizar:
# mostrar total
# encerrar


compras = []
total = 0
    
while True:
    opcao = input(
    '\nEscolha uma opção\n'
    'Menu:\n'

    '1 - Adicionar produto\n'
    '2 - Ver total da compra\n'
    '3 - Finalizar compra\n\n'
    )

    
    if opcao == '3':
        print('Compra finalizada\n')
        break

    if opcao not in ['1', '2', '3']:
        print('Opção inválida! Tente novamente\n')
        continue

    if opcao == '1':
        compra = float(input('Digite o valor do produto: \n'))
        compras.append(compra)
        total += compra

    elif opcao == '2':
        print(f'O total de compras é {total:.2f}\n')