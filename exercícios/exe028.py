from random import randint
from time import sleep
n = randint(1, 5)
print('=' * 40)
resp = int(input('Tente adivinhar o número entre 0 e 5. '))
print('=' * 40)
print('Processando...')
sleep(2)
if resp == n:
    print('Parabéns, você acertou o número.')
else:
    print('Você errou. O número correto era {} e não {}.'.format(n, resp))