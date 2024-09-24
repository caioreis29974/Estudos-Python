print('=============')
print('Gerador de PA')
print('=============')
p1 = int(input('Digite o valor do primeiro termo: '))
r = int(input('Dogote o valor da razão: '))
termo = p1
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    c += 1
print('Fim.')
