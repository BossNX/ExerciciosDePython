from math import sqrt
num = float(input('Digite um número: '))
dob = num * 2
tri = num * 3
rq = sqrt(num)
print('O \033[4mdobro\033[m de \033[31m{}\033[m vale \033[32m{:.2f}\033[m, o \033[4mtriplo\033[m de \033[31m{}\033[m '
      'vale \033[33m{:.2f}\033[m e a \033[4mraíz quadrada\033[m de \033[31m{}\033[m '
      'vale \033[34m{:.2f}\033[m'.format(num, dob, num, tri, num, rq))
