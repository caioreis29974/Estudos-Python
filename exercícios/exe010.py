x = float(input('Digite quantos reais você tem: R$'))
real = 5.44
dolar = x / real
print('Com R${:.2f} você poderia comprar US${:.2f}'.format(x, dolar))