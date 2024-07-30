from datetime import date
atual = date.today().year
mai = 0
men = 0
for c in range(1, 11):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 18:
        mai = mai + 1
    else:
        men = men + 1
print('Entre essas 10 pessoas {} são de maior idade e {} menores de idade.'.format(mai, men))