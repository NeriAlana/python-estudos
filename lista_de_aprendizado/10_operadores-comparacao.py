x = y = z = False
n1 = n2 = 0


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

x  = n1 == n2
print(f'{n1} é igual a {n2}? {x}')

z = n1 != n2
print(f'{n1} é diferente de {n2}? {z}')

z = n1 > n2
print(f'{n1} é maior que {n2}? {z}')


#Operadores de comparação : ==, !=, >, <, >=, <=
#Operadores de comparação retornam um valor booleano (True ou False) dependendo do resultado da comparação.