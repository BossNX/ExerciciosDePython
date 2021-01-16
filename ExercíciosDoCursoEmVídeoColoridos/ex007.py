n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
if media >= 7.0:
    print('\033[4;32mParabéns\033[m! Você foi \033[4;34mAprovado\033[m! '
    'Sua \033[4mmédia\033[m foi \033[32m{:.1f}\033[m! '
    'Continue assim!'.format(media))
else:
    print('\033[4;31mReprovado\033[m! Sua média foi \033[31m{:.1f}\033[m! Estude mais na próxima!'.format(media))
