sal = float(input('Digite seu salário atual: R$'))
aumento = sal * 15 / 100
novo = sal + aumento
print('Seu salário antigo era de R${:.2f} e o novo será de R${:.2f}.'.format(sal, novo))
