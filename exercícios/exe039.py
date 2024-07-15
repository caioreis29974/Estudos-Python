from datetime import date

ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano

print('Quem nasceu no ano {} tem {} anos no ano de {}.'.format(ano, idade, atual))

if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade < 18:
    x = 18 - idade
    print('Você ainda não tem 18 anos. Faltam {} anos para seu alistamento.'.format(x))
else:
    x = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(x))
