print('==========================')
print('    ALUGUEL DE CARROS    ')
print('==========================')
km = float(input('Por quantos Km você rodou ? '))
d = int(input('Por quantos dias você ficou com ele ? '))
kmf = km * 0.15
df = d * 60
total = kmf + df
print('O valor total a ser pago é de R${:.2f}.'.format(total))
