n1 = float(input('Quanto você tirou na primeira prova? '))
n2 = float(input('Quanto você tirou na segunda prova? '))
m = (n1 + n2) / 2

if m < 5.0:
    print('Sua média foi {} e você está \033[4;31mREPROVADO\033[m.'.format(m))
elif m >= 5.0 and m <= 6.9:
    print('Sua média foi {} e ficou de \033[4;33mRECUPERAÇÃO\033[m.'.format(m))
else:
    print('Sua média foi {} e você foi \033[4;32mAPROVADO\033[m.'.format(m))
