# Sistema de notas

# Média:

# ≥ 7 → aprovado
# ≥ 5 → recuperação
# < 5 → reprovado

# nota1 = float(input('Digite a primeira nota'))

notas = []

for i in range(4):  # Supondo que sejam 4 notas
    nota = float(input(f'Digite a nota {i + 1}: '))
    notas.append(nota)
    
media = sum(notas) / len(notas)
    
if media>= 7:
    print(f'Média: {media}. Aprovado!')
elif media >= 5  and media <= 6.9:
    print(f'Média: {media}. Recuperação!')
else: 
    print(f'Média: {media}. Reprovado!')