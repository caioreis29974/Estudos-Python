d = int(input('Qual foi a distância da viagem em Km? '))
if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45

print('O valor da passagem será de R${:.2f}.'.format(v))
