# Condicionais (if, elif, else)
# Exercício 1 — Número positivo

# Peça um número:

# positivo
# negativo
# zero

num = int(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")