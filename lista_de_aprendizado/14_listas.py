#Lista: representa uma sequência de valores, onde cada valor é identificado por um índice.
#As listas são mutáveis, ou seja, é possível alterar seus elementos após a criação.
#sintaxe: nome_lista = [valores]

# notas = [5, 7, 8, 6, 9]
# print(notas) #imprime a lista completa
# print(notas[0]) #imprime o primeiro elemento da lista (índice 0)


n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 4]

valores = n1 + n2 #concatenação de listas
# print(valores) #imprime a lista resultante da concatenação
# print(type(valores)) #imprime o tipo da variável valores (list)
# print(valores[0]) #imprime o primeiro elemento da lista valores (índice 0)
# print(len(valores)) #imprime o número de elementos da lista valores
# print(valores[-1]) #imprime o último elemento da lista valores (índice -1)
# print(valores[2:5]) #imprime os elementos da lista valores do índice 2 ao índice 4 (5-1)
# valores[0] = 10 #altera o valor do primeiro elemento da lista valores para 10
# print(valores) #imprime a lista valores após a alteração do primeiro elemento
# print(valores[3:3]) #imprime uma sublista vazia, pois o índice de início é igual ao índice de fim (3:3)
# print(valores[3:4]) #imprime o elemento da lista valores no índice 3, pois o índice de início é 3 e o índice de fim é 4 (4-1 = 3)
# print(sorted(valores)) #imprime a lista valores ordenada em ordem crescente, sem alterar a lista original
# print(sorted(valores, reverse=True)) #imprime a lista valores em ordem decrescente, sem alterar a lista original
# print(sum(valores)) #imprime a soma de todos os elementos da lista valores
# print(max(valores)) #imprime o maior valor da lista valores
# print(min(valores)) #imprime o menor valor da lista valores
# valores.append(15) #adiciona o valor 15 ao final da lista valores
# print(valores) #imprime a lista valores após a adição do valor 15
# valores.pop() #remove o último elemento da lista valores
# print(valores) #imprime a lista valores após a remoção do último elemento
# valores.pop(3) #remove o elemento no índice 3 da lista valores
# valores.insert(3, 20) #insere o valor 20 no índice 3 da lista valores
# print(valores) #imprime a lista valores após a inserção do valor 20 no índice 3
# print(20 in valores) #imprime o resultado da verificação se o valor 20 está presente na lista valores

planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']

for planeta in planetas:
    print(planeta) #imprime cada elemento da lista planetas em uma linha separada