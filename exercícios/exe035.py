print('=' * 25)
print('ANALISADOR DE TRIÂNGULOS')
print('=' * 25)
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima PODEM formar um triângulo.')
else:
    print('As retas acima NÃO podem formar um triângulo.')
