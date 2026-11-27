# Sistema de notas

# Menu:

# 1 - Adicionar nota
# 2 - Ver média
# 3 - Ver maior nota
# 4 - Sair

# Regras:

# usuário pode adicionar infinitas notas
# calcule média manualmente
# não use funções prontas tipo max()


notas = []

while True:

    opcao = input(
        'Escolha uma opção:\n'
        '1 - Adicionar nota\n'
        '2 - Ver média\n'
        '3 - Ver maior nota\n'
        '4 - Sair\n'
        '5 - Mostrar todas as notas\n'
    )

    if opcao == '4':
        print('Encerrando a aplicação...')
        break

    if opcao not in ('1', '2', '3', '4', '5'):
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '1':
        nota = float(input('Digite a nota a ser adicionada: '))
        notas.append(nota)

    elif opcao == '2':
        soma = 0
        for nota in notas:
            soma += nota
        media = soma / len(notas)
        print(f'A média das notas é: {media}')

    elif opcao == '3':
        maior = notas[0]
        for nota in notas:
            if nota > maior:
                maior = nota
        print(f'A maior nota é: {maior}')

    elif opcao == '5':
        print('Notas adicionadas:', notas)




