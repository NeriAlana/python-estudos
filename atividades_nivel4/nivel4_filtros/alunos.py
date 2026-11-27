# Desafio 9 — Alunos (parecido com o seu)

# Cada aluno possui:

# nome
# nota

# Menu:

# 1 - Cadastrar
# 2 - Mostrar todos
# 3 - Mostrar aprovados
# 4 - Mostrar reprovados
# 5 - Sair

# Aprovado:

# nota >= 7

from pprint import pprint 
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
alunos = []

while True:
    opcao = input('Menu:\n'

    '1 - Cadastrar\n'
    '2 - Mostrar todos\n'
    '3 - Mostrar aprovados\n'
    '4 - Mostrar reprovados\n'
    '5 - Sair\n')

    limpa_tela()
    
    if opcao not in ['1', '2', '3', '4', '5']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '5':
        print('Aplicação finalizada.')
        break

    if opcao == '1':
        nome = input('Informe o nome do aluno a ser cadastrado:')
        nota = float(input(f'Informe a nota do aluno {nome}: ')) 
        alunos.append({"nome" : nome,
        "nota" : nota})

    if opcao == '2':
        for aluno in alunos:
            pprint(f'Aluno: {aluno["nome"]}, Nota:{aluno["nota"]}\n')

    if opcao == '3':
        for aluno in alunos:
            if aluno["nota"] >= 7:
                pprint(f' Aluno: {aluno["nome"]}, Nota: {aluno["nota"]} APROVADO.\n')

    if opcao == '4':
        for aluno in alunos:
            if aluno["nota"] < 7:
                pprint(f' Aluno: {aluno["nome"]}, Nota: {aluno["nota"]} REPROVADO.\n')






