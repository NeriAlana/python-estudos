# Desafio 6 — Biblioteca

# Cada livro possui:

# título
# autor

# Menu:

# 1 - Cadastrar livro
# 2 - Ver livros
# 3 - Sair

# A estrutura deverá ficar parecida com:

# [
#     {"titulo":"Dom Casmurro","autor":"Machado"},
#     {"titulo":"1984","autor":"George Orwell"}
# ]

from pprint import pprint #biblioteca usada para fazer a quebra de linha automaticamente e deixar a visualização mais agradável
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear' )

livros = []

while True:

    opcao = input('Menu:\n'

    '1 - Cadastrar livro\n'
    '2 - Ver livros\n'
    '3 - Sair\n')
    
    limpa_tela()

    if opcao not in ['1', '2', '3']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '3':
        print('Finalizando a aplicação')
        break

    if opcao == '1':
        titulo = input('Informe o nome do livro a ser cadastrado: ')
        autor = input('Informe o nome do autor do livro: ')
        livros.append({
        "titulo": titulo, 
        "autor": autor
        })

    if opcao == '2':
        print('BIBLIOTECA')
        pprint(livros)
