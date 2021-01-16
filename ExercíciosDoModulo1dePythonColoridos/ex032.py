from datetime import date
ano = int(input('\033[36mDigite qualquer ano para dizer '
                'se é bissexto ou não! Digite 0 para dizer sobre o ano atual!\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[34m{}\033[m \033[32mÉ BISSEXTO\033[m'.format(ano))
else:
    print('O ano \033[34m{}\033[m \033[31mNÃO É BISSEXTO\033[m'.format(ano))
