i = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        i = i + n
        cont = cont + 1
print('A soma entre todos os {} números pares informados é: {}.'.format(cont, i))
