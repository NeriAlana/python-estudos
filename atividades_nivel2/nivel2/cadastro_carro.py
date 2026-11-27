# Desafio 5 — Cadastro de um carro

# Guardar:

# modelo
# marca
# ano

# Mesmo esquema.

from pprint import pprint
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear' )

carros = []

while True:

    opcao = input('Cadastro de Carro:\n'

    '1 - Cadastrar\n'
    '2 - Buscar carro\n'
    '3 - Excluir carro\n'
    '4 - Mostrar carros cadastros\n'
    '5 - Sair\n')


    if opcao not in ['1', '2', '3', '4', '5']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '5':
        print('Finalizando a aplicação')
        break

    if opcao == '1':
        modelo = input('Informe o modelo do carro: ')
        marca = input('Informe a marca do carro: ')
        ano = input('Informe o ano do carro: ')
        carros.append({
        "modelo": modelo,
        "marca" : marca,
        "ano" : ano
        })

    if opcao == '2':
        buscar_carro = input('Informe o modelo do carro: ')
        if buscar_carro == carros.modelo:
            print(f'O carro {modelo}, {marca}, {ano} foi encontrado')
        else:
            print('Carro não encontrado!')

    if opcao == '3':
        excluir_modelo = input('Informe o modelo do carro: ')
        excluir_marca = input('Informe a marca do carro: ')
        excluir_ano = input('Informe o ano do carro: ')
        for carro in carros:
            if excluir_modelo != carro['modelo'] and excluir_marca != carro['marca'] and excluir_ano != carro['ano']:
                carros.remove(carro)


    if opcao == '4':
        pprint(carros)











