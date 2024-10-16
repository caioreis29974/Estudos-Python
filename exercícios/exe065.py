soma = media = cont = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Vc digitou {} numeros.\nA soma foi {}\nA media foi {}'.format(cont, soma, media))
print('O maior numero foi {} e o menor foi {}.'.format(maior, menor))
print('Fim do Codiigo')