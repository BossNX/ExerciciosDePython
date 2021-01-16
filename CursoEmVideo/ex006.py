n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de \033[4;31m{}\033[m vale \033[34m{}\033[m. '.format(n, d))
print('O triplo de \033[4;33m{}\033[m vale \033[36m{}\033[m. '.format(n, t))
print('A raíz quadrada de \033[4;35m{}\033[m é igual a \033[32m{:.2f}\033[m. '.format(n, r))
