n1 = int(input('Digite o \033[0;33mprimeiro \033[mnúmero: '))
n2 = int(input('Digite o \033[0;33msegundo \033[mnúmero: '))

if n1 > n2:
    print('O \033[0;34mprimeiro \033[mvalor é maior.')
elif n2 > n1:
    print('O \033[0;34msegundo \033[mvalor é maior.')
else:
    print('\033[4;31mNão existe valor maior, ambos são iguais.\033[m')
