print('=============')
print('Gerador de PA')
print('=============')
p1 = int(input('Digite o valor do primeiro termo: '))
r = int(input('Dogote o valor da razão: '))
termo = p1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Finalizando... {} termos foram mostrados.'.format(total))
