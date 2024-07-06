sal = float(input('Digite o seu salário atual: R$'))

if sal >= 1250:
    aumento = sal * 10 / 100
    novo = sal + aumento
else:
    aumento = sal * 15 / 100
    novo = sal + aumento

print('O seu salário antigo era R${:.2f} e com o aumento de R${:.2f} você irá ganhar R${:.2f}.'.format(sal, aumento, novo))