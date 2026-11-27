# for contador_externo in range(1, 6):
#     print(f'\nContagem externa: {contador_externo}')
#     for contador_interno in range(4, 0, -1):
#         print(f'Contagem interna: {contador_interno}')
        
#     print('Contagem encerrada')

import random

for A in range(1, 6):
    print(f'\nconjunto: {A}')
    for B in range(5):
        num = random.randint(1, 100) #gera um número aleatório inteiro(randint) entre 1 e 100
        print(f'Número gerado: {num}')