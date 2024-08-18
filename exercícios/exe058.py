from random import randint
n = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == n:
        acerto = True
    else:
        if jogador < n:
            print('Mais... Tente Novamente!')
        elif jogador > n:
            print('Menos... Tente Novamente!')
print('Parabéns, você acertou o número com {} palpites.'.format(palpites))