# Crie um sistema com o menu:

# 1 - Adicionar produto
# 2 - Ver produtos
# 3 - Sair

# Regras:

# Crie uma lista vazia.
# Sempre que escolher 1, peça o nome do produto.
# Adicione na lista.
# Em "Ver produtos", mostre todos os produtos cadastrados.
# O sistema só encerra no 3.


produtos = []

while True:

    opcao = input('\nEscolha uma opção:\n'
    '1 - Adicionar produto\n'
    '2 - Ver produtos\n'
    '3 - Sair\n')

    if opcao not in ['1', '2', '3']:
        print('Opção inválida! Tente novamente.')
        continue


    if opcao == '3':
        print('Finalizando...')
        break

    if opcao == '1':
        cadastrar = input('Informe o produto a ser cadastrado: ')
        
        #criando uma nova lista para armazenar os produtos cadastrados e adicionar à lista produtos
        novo_produto = {"nome_produto": cadastrar}
        produtos.append(novo_produto)

    if opcao == '2':
        for produto in produtos: 
            print(f'Produto: {produto["nome_produto"]}')
          