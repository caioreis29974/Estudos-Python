from datetime import date

ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('E a sua categoria é MIRIM.')
elif idade <= 14:
    print('E a sua categoria é INFANTIL.')
elif idade <= 19:
    print('E a sua categoria é JUNIOR.')
elif idade <= 25:
    print('E a sua categoria é SÊNIOR')
else:
    print('E a sua categoria é MASTER.')
