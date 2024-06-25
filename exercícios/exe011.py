larg = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
area = larg * alt
tinta = area / 2
print('A parede que você citou tem {}x{} e sua área é de {}m2.'.format(larg, alt, area))
print('Para pintar a parede, é preciso de {}L de tinta.'.format(tinta))
