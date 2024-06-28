from math import hypot
c1 = float(input('Digite o comprimento do cateto oposto: '))
c2 = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(c1, c2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))

'''Segundo método de como encontrar uma hipotenusa (usando módulos)'''