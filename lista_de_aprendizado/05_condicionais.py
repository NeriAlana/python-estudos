#Eles podem ser SIMPLES, COMPOSTOS ou ANINHADOS
#Por exemplo, o IF é uma estrutura condicional SIMPLES, o IF-ELSE é uma estrutura condicional COMPOSTA e o IF-ELSE-IF é uma estrutura condicional ANINHADA

#Estrutura condicional SIMPLES
# n1 = n2 = 0.0
# media = 0
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# #Calcular a média das notas
# media = (n1 + n2) / 2

# if (media >=7):
#     print("Aprovado")

# print(f'Sua média é: {media}')

#Estrutura condicional COMPOSTA
# n1 = n2 = 0.0
# media = 0
# n1 = float(input("Digite a primeira nota: "))
# n2 = float(input("Digite a segunda nota: "))

# #Calcular a média das notas
# media = (n1 + n2) / 2

# if (media >=7):
#     print("Aprovado")
# else:
#     print("Reprovado")

# print(f'Sua média é: {media}')

#Estrutura condicional ANINHADA
n1 = n2 = 0.0
media = 0
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

#Calcular a média das notas
media = (n1 + n2) / 2

if (media >=7):
    print("Aprovado")
elif (media >=5):
    print("Recuperação")
else:
    print("Reprovado")

print(f'Sua média é: {media}')