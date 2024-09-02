from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
resp = 0
while resp != 5:
    print('''========== MENU ==========

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Fechar Programa''')
    resp = int(input('\nEscolha uma opção: '))
    print('==========================')
    if resp == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif resp == 2:
        mult = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, mult))
    elif resp == 3:
        if n1 > n2:
            print('O número {} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('O número {} é maior que {}'.format(n2, n1))
        else:
            print('Os números {} e {} são iguais.'.format(n1, n2))
    elif resp == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        print('Substituindo valores...')
        sleep(0.7)
    elif resp == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Essa opção não existe. Tente Novamente!')
    print('==========================')
print('Fim do Programa!')