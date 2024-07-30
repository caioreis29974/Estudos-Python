n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end= ' ')
        cont = cont + 1
    else:
        print('\033[31m', end= ' ')
    print('{} '.format(c), end= ' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, cont))
if cont == 2:
    print('E por isso ele é um número \033[32mPRIMO\033[m.')
else:
    print('E por isso ele é um número \033[31mNÃO PRIMO\033[m.')