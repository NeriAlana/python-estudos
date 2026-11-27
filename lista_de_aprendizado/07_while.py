# num = 1

# while num <= 10:
#     print(num)
#     num += 1

nome = None

while True:
    nome = input('Digite seu nome ou x para parar: ')
    
    if nome == 'x' or nome == 'X':
        break
    print(f'Olá, {nome}')
print('Programa encerrado')