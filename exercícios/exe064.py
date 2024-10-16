soma = cont = n = 0
n = int(input('digite um valor [999] para parar! '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('digite um valor [999] para parar! '))
print('Vc digitou {} numeros e a soma deles foi {}.'.format(cont, soma))
