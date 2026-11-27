# Menu:

# 1 - Adicionar contato
# 2 - Ver contatos
# 3 - Buscar contato
# 4 - Remover contato
# 5 - Sair

    
contatos = []


while True:

    opcao = input('Menu:\n'

    '1 - Adicionar contato\n'
    '2 - Ver contatos\n'
    '3 - Buscar contato\n'
    '4 - Remover contato\n'
    '5 - Sair\n')


    if opcao not in ['1', '2', '3', '4', '5']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '5':
        print('Fechando a agenda...')
        break

    if opcao == '1':
        adicionar_contato = input('Informe o contato a ser adicionado: ')
        contatos.append(adicionar_contato)

    if opcao == '2':
        for contato in contatos:
            print (contato)

    if opcao == '3':
        buscar_contato = input('Informe o número do contato a ser buscado: ')
        for contato in contatos:
            if buscar_contato == contato:
                print(f'contato encontrado: {contato}')
            else:
                print('Esse contato não existe na agenda. Você pode adicioná-lo')


    if opcao == '4':
        remover_contato = input('Informe o número a ser removido da lista de contatos: ')
        contatos.remove(remover_contato)


