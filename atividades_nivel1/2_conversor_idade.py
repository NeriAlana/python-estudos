# Exercício 2 — Conversor de idade

# Peça a idade da pessoa em anos e mostre:

# meses
# dias
# horas (aproximadamente)

idade = int(input('Digite a sua idade em anos: '))
meses = idade * 12
dias = meses * 30 #considerando um mês com 30 dias
horas = dias *24
print(f'Sua idade em anos: {idade}\nSua idade em meses: {meses}\nSua idade em dias: {dias} dias\nSua idade em horas: {horas} horas')