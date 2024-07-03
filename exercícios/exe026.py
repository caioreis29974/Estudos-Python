f = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(f.count('A')))
print('A letra "A" aparece na posição {} pela primeira vez na frase.'.format(f.find('A')+1))
print('A letra "A" aparece na posição {} pela última vez na frase.'.format(f.rfind('A')+1))
