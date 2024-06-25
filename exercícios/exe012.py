valor = float(input('Digite o valor do produto: R$'))
desconto = valor * 5 / 100
final = valor - desconto
print('O produto que custava R${}, na promoção de 5% de desconto começou a custar R${:.2f}.'.format(valor, final))
