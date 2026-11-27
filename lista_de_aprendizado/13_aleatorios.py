import random

# # valor = random.randint(1, 10) #gera um número aleatório inteiro(randint) entre 1 e 10
# # print(f'Número gerado: {valor}')

# #para gerar 5 números aleatórios entre 1 e 50

# for i in range(5):
#     valor = random.randint(1, 50)
#     print(f'{i + 1}º  Número gerado: {valor}')
    
#     #Para gerar numeros aleatórios entre 0 e 1, podemos usar a função random.random(), que retorna um número de ponto flutuante aleatório no intervalo [0.0, 1.0]).
    
# num = random.random() #gera um número aleatório de ponto flutuante entre 0 e 1
# print(f'Número aleatório entre 0 e 1: {num}')

# #para conseguir um número aleatório entre 0 e 10, podemos multiplicar o resultado de random.random() por 10:

# num = random.random() * 10 #gera um número aleatório de ponto flutuante entre 0 e 10
# print(f'Número aleatório entre 0 e 10: {round(num, 2)}') #arredonda o número para 2 casas decimais

# valor = random.uniform(1, 100) #gera um número aleatório de ponto flutuante entre 1 e 100
# print(f'Número aleatório entre 1 e 100: {round(valor, 2)}') #arredonda o número para 2 casas decimais

L= [2, 4, 6, 9, 10, 13, 14, 16, 18, 20, 21, 27, 33]
# n = random.choice(L) #escolhe um elemento aleatório da lista L
# print(f'Número aleatório escolhido da lista: {n}')

# n = random.sample(L, 3) #escolhe 3 elementos aleatórios da lista L sem repetição
# print(f'3 números aleatórios escolhidos da lista: {n}')

# para embaralhar a lista L, podemos usar a função random.shuffle(), que embaralha os elementos da lista em ordem aleatória:
print(L) #imprime a lista original
random.shuffle(L) #embaralha a lista L
print(f'Lista embaralhada: {L}') #imprime a lista embaralhada