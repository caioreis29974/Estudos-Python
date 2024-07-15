casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Quanto você recebe de salário? R$'))
anos = int(input('Em quantos anos você deseja pagar a casa? '))
prest = casa / (anos * 12)
min = salario * 30 / 100

print('Para pagar uma casa com o valor de \033[0;32mR${:.2f} \033[mem {} anos a prestação será no valor de \033[0;32mR${:.2f}\033[m.'.format(casa, anos, prest))

if prest <= min:
    print('Seu empréstimo foi \033[4;33mCONCEDIDO\033[m')
else:
    print('Desculpa, você \033[4;31mNÃO PODE\033[m pagar por essa casa.')
