# Exercício 9 — Sistema de estoque

# Menu:

# 1 - Adicionar produto
# 2 - Remover produto
# 3 - Ver estoque
# 4 - Sair

# Regras:

# usar lista
# impedir remover produto inexistente


estoque = []
produto = None

while True:

    opcao = input('Menu:\n'

    '1 - Adicionar produto\n'
    '2 - Remover produto\n'
    '3 - Ver estoque\n'
    '4 - Sair\n')


    if opcao not in ['1', '2', '3', '4']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '4':
        print('Sistema finalizado.')
        break 

    if opcao == '1':
        produto = input('Informe o produto a ser adicionado: ')
        estoque.append(produto)
        estoque.append(f' Quantidade em estoque: {len(estoque)}')

    elif opcao == '2':
        produto = input('Informe o produto a ser removido do estoque: ')
        if produto in estoque:
            estoque.remove(produto)
            estoque.remove(f' Quantidade em estoque: {len(estoque)}')
            print(f'Produto removido do estoque: {produto}')
        else:
            print('Produto não encontrado no estoque.')

    elif opcao == '3':
        print(estoque)
