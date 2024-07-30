stringo = str(input('Digite uma frase: ')).strip().upper()
palavras = stringo.split()
junto = ''.join(palavras)
inverso = ''
for l in range(len(junto) -1, -1, -1):
    inverso += junto[l]
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase não é um palíndromo')
