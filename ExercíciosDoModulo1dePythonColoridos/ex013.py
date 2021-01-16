salário = float(input('Qual o salário do trabalhador? R$'))
aumento = salário + (salário*15/100)
print('O trabalhador recebia normalmente \033[31;4mR${:.2f}\033[m, mas com o \033[34;4maumento\033[m de \033[36;4m15%\033[m '
      'ele passou a receber \033[4;32mR${:.2f}\033[m'.format(salário, aumento))
