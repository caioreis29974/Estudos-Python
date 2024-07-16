print('{:=^40}'.format(' LOJAS REIS '))
compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENDO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão (COM JUROS)''')
op = int(input('Escolha uma opção: '))

if op == 1:
    total = compras - (compras * 10 / 100)
elif op == 2:
    total = compras - (compras * 5 / 100)
elif op == 3:
    total = compras
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}.'.format(parcela))
elif op == 4:
    total = compras + (compras * 20 / 100)
    totpar = int(input('Em quantas parcelas? '))
    parcela = total / totpar
    print('Sua compra foi parecelada em {}x de R${:.2f} COM JUROS!'.format(totpar, parcela))
else:
    print('\033[4;31mOpção inválida, tente novamente!\033[m')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, total))
