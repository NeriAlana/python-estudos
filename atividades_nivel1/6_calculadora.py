# Operadores Aritméticos
# Exercício 1 — Calculadora

# Peça dois números e mostre:

# soma
# subtração
# multiplicação
# divisão
# potência

print('Calculadora')
num1= int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2
pot = num1 ** num2

print(f'Operações com os números {num1} e {num2}\nSoma: {soma}\nSubtração: {sub}\nMultiplicação: {multi}\nDivisão: {div}\nPotência: {pot}')