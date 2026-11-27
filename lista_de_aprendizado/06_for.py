# lista = ["Python", "Java", "C++", "JavaScript"]
# palavra = 'Alana'
# for linguagem in lista:
#     print(linguagem)
    
    
# for letra in palavra:
#     print(letra)



# # FUNÇÃO RANGE( pode ser operada com um, dois ou três parâmetros)
    
# for numero in range(1,11):
#     print(numero)
    
# for numero in range(11):
#     print(numero)
    
# nome = input("Digite seu nome: ")
# for i in range(10):
#     print(f'{i+1} - {nome}')
    
#range( valor_inicial, valor_final, passo/incremento)
# for i in range(2,21,2):
#     print(i)
    
# for i in range(20,1,-2):
#     print(i)

pedras = ('Rubi', 'Safira', 'Esmeralda', 'Diamante', 'Ametista', 'Topázio', 'Turmalina', 'Opala', 'Quartzo', 'Ágata')
#construindo uma iteração para imprimir as pedras, mas pulando a pedra 'Quartzo'
for pedra in pedras:
    if pedra == 'Quartzo':
        continue #pula a iteração atual e passa para a próxima
    print(pedra)    