algo = str(input('Digite algo: '))
print('Seu tipo \033[36;4mprimitivo\033[m é: \033[4;34m{}\033[m'.format(type(algo)))

Limpa = '\033[m'
Verdadeiro = '\033[4;32mTrue\033[m'
Falso = '\033[4;31mFalse\033[m'

if algo.isnumeric() == True:
    print('É \033[4;33mnumérico{}? {}'.format(Limpa, Verdadeiro))
else:
    print('É \033[4;33mnumérico{}? {}'.format(Limpa, Falso))

if algo.isalpha() == True:
     print('É \033[4;34malfabético{}? {}'.format(Limpa, Verdadeiro))
else:
    print('É \033[4;34malfabético{}? {}'.format(Limpa, Falso))

if algo.isalnum() == True:
    print('É \033[4;35malfanumérico{}? {}'.format(Limpa, Verdadeiro))
else:
    print('É \033[4;35malfanumérico{}? {}'.format(Limpa, Falso))

if algo.isupper() == True:
    print('Está em \033[4;36mMaiúsculas{}? {}'.format(Limpa, Verdadeiro))
else:
    print('Está em \033[4;36mMaiúsculas{}? {}'.format(Limpa, Falso))

if algo.islower() == True:
    print('Está em \033[4;37mMinúsculas{}? {}'.format(Limpa, Verdadeiro))
else:
    print('Está em \033[4;37mMinúsculas{}? {}'.format(Limpa, Falso))

if algo.istitle() == True:
    print('Está \033[1;4;7;30mCapitalizada{}? {}'.format(Limpa, Verdadeiro))
else:
    print('Está \033[1;4;7;30mCapitalizada{}? {}'.format(Limpa, Falso))
