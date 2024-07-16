from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('''SUAS OPÇÕES;
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
op = int(input('Escolha sua opção: '))
print('=-' * 20)
print('O Computador jogou {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[op]))
print('=-' * 20)

if pc == 0:
    if op == 0:
        print('EMPATE!')
    elif op == 1:
        print('O JOGADOR VENCEU!')
    elif op == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
elif pc == 1:
    if op == 0:
        print('O COMPUTADOR VENCEU!')
    elif op == 1:
        print('EMPATE!')
    elif op == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
elif pc ==2:
    if op == 0:
        print('O JOGADOR VENCEU!')
    elif op == 1:
        print('O COMPUTADOR VENCEU!')
    elif op == 2:
        print('EMPATE!')
    else:
        print('\033[4;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
