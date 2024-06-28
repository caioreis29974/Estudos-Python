from math import sin, cos, tan, radians
an = float(input('Digite o ângulo: '))
seno = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('O ângulo de {} tem o seno de {:.2f}.'.format(an, seno))
print('O ângulo de {} tem o cosseno de {:.2f}.'.format(an, cos))
print('A ângunlo de {} tem a tangente de {:.2f}.'.format(an, tan))
