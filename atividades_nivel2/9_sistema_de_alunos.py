# Sistema de alunos

# Cada aluno deve ter:

# nome
# nota





banco_alunos = []

while True:

    opcao = input('Menu:\n'

    '1 - Cadastrar aluno\n'
    '2 - Ver alunos\n'
    '3 - Ver aprovados\n'
    '4 - Ver reprovados\n'
    '5 - Sair\n')

    if opcao not in ['1', '2', '3', '4', '5']:
        print('Opção inválida! Tente novamente.\n')
        continue

    if opcao == '5':
        print('Finalizando...')
        break

    if opcao  == '1':
        nome = input('Informe o nome do aluno a ser cadastrado: ')
        nota = float(input('Informe a nota do aluno: '))
       
       #criando um novo dicionário para armazenar dados do aluno e adicionar à lista banco_alunos
        novo_aluno = {"nome_aluno": nome, "nota_aluno": nota}
        banco_alunos.append(novo_aluno)
        print('Aluno cadastrado com sucesso!\n')

    if opcao == '2':
        for aluno in banco_alunos:
            print(f'Aluno: {aluno["nome_aluno"]}, Nota: {aluno["nota_aluno"]}\n')

    if opcao == '3':
        for aluno in banco_alunos:
            if aluno["nota_aluno"] >= 7:
                print(f'Aprovados\n Aluno: {aluno["nome_aluno"] }\n Nota: {aluno["nota_aluno"]}\n')

    if opcao == '4':
        for aluno in banco_alunos:
            if aluno["nota_aluno"] < 7:
                print(f'Reprovados\n Aluno: {aluno["nome_aluno"]}\n Nota: {aluno["nota_aluno"]}\n')

