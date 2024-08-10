from time import sleep
s = 1
masc = 0
fem = 0

print('--------------CONTADOR--------------')
print('Digite "0" para finalizar o programa\nDigite M para registrar um homem\nDigite F para registrar uma mulher')
print('------------------------------------')

while s != 0:
    resp = str(input('Qual o sexo da pessoa? [M/F] ')).strip().upper()[0]
    if resp == "0":
        s = 0
    elif resp == "M":
        masc += 1
        print('Sexo M registrado!')
    elif resp == "F":
        fem += 1
        print('Sexo F registrado!')
    else:
        print('Resposta inválida, tente novamente!')

print('Carregando...')
sleep(1.5)
print('Você apresentou {} pessoas do sexo masculino e {} do sexo feminino.'.format(masc, fem))
