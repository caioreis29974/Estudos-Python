nome = str(input('Digite seu nome: ')).strip()
separado = nome.split()
print('=' * 45)
print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('Quantas letras o seu nome completo tem: {}'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e ele tem {} letras'.format(separado[0], len(separado[0])))
print('=' * 45)