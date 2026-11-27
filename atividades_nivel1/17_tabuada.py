# Peça um número e mostre a tabuada dele.

# Exemplo:

# 5 x 1 = 5
# 5 x 2 = 10


print('TABUADA')
num = int(input('Digite um número: '))
operacao = input('Escolha a operação: +, -, *, /: ')  

if operacao == '+':
    for i in range(10):
        print(f'{num} + {i + 1} = {num + (i + 1)}')
elif operacao == '-':
    for i in range(10):
        print(f'{num} - {i + 1} = {num - (i + 1)}')
elif operacao == '*':
    for i in range(10):
        print(f'{num} * {i + 1} = {num * (i + 1)}')
else:
    for i in range(10):
        print(f'{num} / {i + 1} = {num / (i + 1):.2f}')