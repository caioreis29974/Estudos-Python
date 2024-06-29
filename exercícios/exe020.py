from random import shuffle
n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
lista = [n1, n2, n3]
shuffle(lista)
print('A ordem da lista será: ')
print(lista)
