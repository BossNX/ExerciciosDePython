nome = str(input('Digite um nome: ')).strip()
if nome == 'Marcelo José' or nome == 'José':
    print('É um prazer te conhecer {}ZeroX{}!!!'.format('\033[4;31m', '\033[m'))

elif nome == 'André Luis' or nome == 'André':
    print('É um prazer te conhecer {}BossNX{}!!!'.format('\033[4;34m', '\033[m'))

elif nome == 'João Victor' or nome == 'João':
    print('É um prazer te conhecer {}CheesperNX{}!!!'.format('\033[4;34m', '\033[m'))

elif nome == 'Leopoldino Felippe' or nome == 'Felippe':
    print('É um prazer te conhecer {}Chrona{}!!!'.format('\033[4;36m', '\033[m'))

elif nome == 'Letícia Vieira' or nome == 'Letícia':
    print('É um prazer te conhecer {}LetVieira{}!!!'.format('\033[4;7;30m', '\033[m'))

elif nome == 'Daniela Arcangela' or nome == 'Daniela':
    print('É um prazer te conhecer {}{}{}!!!'.format('\033[4;7;30m', nome, '\033[m'))
