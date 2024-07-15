nome = str(input('Qual é o seu nome? '))
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)

print('{}, seu IMC é de {:.1f}.'.format(nome, imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    ('Você está em SOBREPESO!')
elif imc >= 30 and imc < 40:
    ('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
