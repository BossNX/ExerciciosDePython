n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
if n1 > n2:
    print('O \033[33mprimeiro valor\033[m é \033[34mmaior\033[m. ')
elif n2 > n1:
    print('O \033[33msegundo valor\033[m é \033[34mmaior\033[m. ')
else:
    print('\033[33mNão existe\033[m valor \033[31mMAIOR\033[m, os dois são \033[34mIGUAIS\033[m. ')
