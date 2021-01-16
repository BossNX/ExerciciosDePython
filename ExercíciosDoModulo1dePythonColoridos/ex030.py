n = int(input('\033[32mDigite um número para verificar se é\033[m \033[34mPAR\033[m \033[32m'
              'ou\033[m \033[31mÍMPAR\033[m: '))
if n % 2 == 0:
    print('\033[32mO número\033[m \033[34m{}\033[m \033[32mé\033[m \033[31mPAR\033[m'.format(n))
else:
    print('\033[32mO número\033[m \033[34m{}\033[m \033[32mé\033[m \033[31mÍMPAR\033[m'.format(n))
