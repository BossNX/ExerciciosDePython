from math import hypot
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa vale \033[35;4m{:.2f}\033[m!'.format(hipotenusa))
