preço = float(input('Qual o preço do produto? R$'))
desconto = preço - (preço*5/100)
print('O produto custava \033[31mR${:.2f}\033[m, com \033[34m5%\033[m de '
      '\033[36mdesconto\033[m passou a custar \033[32mR${:.2f}\033[m agora'.format(preço, desconto))
