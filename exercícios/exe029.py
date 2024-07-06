vel = int(input('Quantos Km seu carro está correndo ? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Seu carro foi multado em R${}.'.format(multa))
else:
    print('Tudo certo, seu carro não será multado.')
    print('Pode seguir na via.')