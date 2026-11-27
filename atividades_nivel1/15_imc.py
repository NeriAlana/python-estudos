# Calculadora de IMC

# Peça: peso e altura

# Calcule:

# imc = peso / altura ** 2

# Mostre classificação:

# abaixo do peso
# normal
# sobrepeso
# obesidade

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura ** 2

if imc < 18.5: 
    print('abaixo do peso')
elif imc > 18.5 and imc < 25:
    print('Normal')
elif imc >24.9 and imc < 29.9:
    print('Sobrepeso')
elif imc > 29.9 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade grave')