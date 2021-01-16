numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('\033[4;32mUnidade:\033[m \033[31m{}\033[m \n\033[31;4mDezena:\033[m \033[32m{}\033[m '
      '\n\033[34;4mCentena:\033[m \033[33m{}\033[m \n\033[4;33mMilhar:\033[m \033[34m{}\033[m'.format(u, d, c, m))
