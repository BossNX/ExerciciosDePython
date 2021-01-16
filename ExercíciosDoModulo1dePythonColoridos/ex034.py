salario = float(input('\033[36;4mQual é o seu salário?\033[m \033[32mR$\033[m'))
if salario <= 1250.00:
    aumento = salario + (salario*15/100)
else:
    aumento = salario + (salario*10/100)
print('\033[34;4mQuem recebia\033[m \033[31mR${:.2f}\033[m \033[34;4mpassou '
      'a receber\033[m \033[32mR${:.2f}\033[m \033[34;4magora\033[m'.format(salario, aumento))
