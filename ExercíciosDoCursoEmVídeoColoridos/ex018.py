from math import sin, cos, tan, radians
angulo = int(input('Digite o valor de um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de \033[34m{}°\033[m vale \033[31m{:.2f}\033[m, o cosseno de \033[34m{}°\033[m vale \033[32m{:.2f}\033[m '
      'e a tangente de \033[34m{}°\033[m '
      'vale \033[33m{:.2f}\033[m'.format(angulo, seno, angulo, cosseno, angulo, tangente))
