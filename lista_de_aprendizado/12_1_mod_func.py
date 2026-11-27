#Módulo com funções variadas para exemplificar a importação de módulos e funções em Python.

#Função que exibe mensagem de boas-vindas:
def mesnsagem():
    print('Bem-vindo ao módulo de funções variadas!\nAqui você encontrará diversas funções para exemplificar a importação de módulos e funções em Python.')
    
#Função para cálculo do fatorial de um número:
def fatorial(numero):
    if numero < 0:
        return 'Digite um valor maior ou igual a zero'
    else:
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * fatorial(numero - 1)
        
#Função para retornar ua série de #Fibonacci até um determinado número:
def fibo(n):
    resultado  = [ ]
    a, b = 0, 1
    while b <= n:
        resultado.append(b)
        a, b = b, a + b
    return resultado

# 0  1  2  3  5  8  13  21  34  55  89  144
# a  b
#    a  b
#       a  b
#          a  b
#              a  b
                #  a  b
                #      a  b
                #         a  b
