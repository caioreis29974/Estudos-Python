n = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das opções abaixo:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
resp = int(input('Sua opção é: '))

if resp == 1:
    print('O número {} convertido para BINÁRIO é igual a {}.'.format(n, bin(n) [2:]))
elif resp == 2:
    print('O número {} convertido para OCTAL é igual a {}.'.format(n, oct(n) [2:]))
elif resp == 3:
    print('O número {} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n) [2:]))
else:
    print('Opção inválida. Tente novamente.')
