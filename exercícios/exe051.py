print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print('{}'.format(c), end= ' -> ')
print('Fim')
