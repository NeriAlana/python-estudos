# import math ## a importação de toda a biblioteca ou módulo deve ser feita SEMPRE no início do código, antes de qualquer outra linha de código. A partir a de agora, para usar as funções matemáticas, basta usar o nome do módulo seguido de um ponto e o nome da função. Exemplo: math.sqrt(16) para calcular a raiz quadrada de 16.
# from math import sqrt, pow, pi, e #importação de funções específicas do módulo math. Com essa forma de importação, não é necessário usar o nome do módulo para acessar as funções, basta usar o nome da função diretamente. Exemplo: sqrt(16) para calcular a raiz quadrada de 16.

# #temos a possibilidade de apelidar o módulo usando a palavra-chave 'as'. Exemplo: import math as m. Com essa forma de importação, podemos usar o apelido 'm' para acessar as funções do módulo math. Exemplo: m.sqrt(16) para calcular a raiz quadrada de 16.

# print(math.sqrt(16)) #calcula a raiz quadrada de 16
# print(math.pow(2, 3)) #calcula 2 elevado a 3
# print(math.pi) #imprime o valor de pi
# print(math.e) #imprime o valor de e

import numpy as np #importação do módulo numpy com o apelido 'np'. O numpy é uma biblioteca de computação científica que fornece suporte para arrays multidimensionais e funções matemáticas avançadas.

# import mod_func as mf


# if __name__ == '__main__':
#     mf.mesnsagem()
    
#     num = int(input('Digite um número inteiro: '))
    
#     print(f'\nCalcular o fatorial do número {num}')
#     fat = mf.fatorial(num)
#     print(f'O fatorial de {num} é: {fat}')

#     print(f'\nCalcular o Fibonacci do número {num}')
#     fib = mf.fibo(num)
#     print(f'O Fibonacci de {num} é: {fib}')

L = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) #criação de um array bidimensional (matriz) usando a função array do módulo numpy. O array é criado a partir de uma lista de listas, onde cada lista interna representa uma linha da matriz.
print(L) #imprime o array L