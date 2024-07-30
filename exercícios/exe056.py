t = 0
maidade = 0
nmaidade = ''
idf = 0

for c in range(1, 5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c)))
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('Qual o sexo da {}° pessoa ? [M / F] '.format(c)))
    print('=' * 40)
    t = idade + idade
    if maidade < idade and sexo == 'M':
        maidade = idade
        nmaidade = nome
    if sexo == 'F' and idade < 20:
        idf = idf + 1

média = t / 4

print('A média de idade do grupo foi {}.'.format(média))
print('O homem mais velho do grupo é o {} com {} anos.'.format(nmaidade, maidade))
print('No grupo {} mulheres tem menos de 20 anos.'.format(idf))
