# Pode dirigir?

# Peça:

# idade
# possui CNH? (True/False ou sim/não)

# Só poderá dirigir se:

# idade ≥ 18
# E possuir CNH

idade = int(input('Digite a sua idade: '))
cnh = input('Você possui CNH? (sim/não): ').strip().lower()

if idade>= 18 and cnh == 'sim':
    print('Você pode dirigir!')
else:
    print('Você não pode dirigir!')