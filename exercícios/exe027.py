nome = str(input('Digite o seu nome: ')).strip()
nome1 = nome.split()
print('O seu primeiro nome é {}.'.format(nome1[0]))
print('O seu último nome é {}.'.format(nome1[len(nome1)-1]))
