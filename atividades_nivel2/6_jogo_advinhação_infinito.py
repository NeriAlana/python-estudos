# Exercício 11 — Jogo de adivinhação infinito
# computador escolhe número aleatório
# usuário tenta acertar
# menu:
# jogar novamente
# sair

# Treina:

# loops
# estado do jogo
# importação de módulo
import random

while True:

    opcao = input('MENU:\n'
    '1-jogar novamente\n'
    '2-sair\n')

    if opcao not in ['1', '2']:
        print('Opção inválida! Tente novamente.')
        continue

    if opcao == '2':
        print('Finalizando sistema...')
        break

    if opcao == '1':
        num = int(input('Adivinhe o número entre 1 e 20: '))
        num_aleatorio = random.randint(1, 20)
        if num_aleatorio == num:
            print('Parabéns, você acertou!! O número foi {num}')
        else:
            print(f'RESULTADO: {num_aleatorio} - Não foi dessa vez. Tente novamente')
