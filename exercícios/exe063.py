print('-='*30)
print('Sequência de Fibonacci v1.0')
print('-='*30)
n = int(input('Quantos termos devo mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('-='*30)
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont+= 1
print(' -> FIM')
print('-='*30)
