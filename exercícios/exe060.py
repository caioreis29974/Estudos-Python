n = int(input('Digite um número para encontrar seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    if c == 1:
        print(' = ',end='')
    else:
        print(' x ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))