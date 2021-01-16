distancia = float(input('\033[32mQual a distância da sua viagem?\033[m '))
if distancia <= 200:
    print('\033[34mA viagem de\033[m \033[33m{}km\033[m \033[34mterá '
          'o preço de\033[m \033[31mR${:.2f}\033[m '.format(distancia, (distancia * 0.50)))
else:
    print('\033[34mA viagem de\033[m \033[33m{}km\033[m \033[34mterá o preço '
          'de\033[m \033[31mR${:.2f}\033[m'.format(distancia, (distancia * 0.45)))
print('\033[36mmTenha uma boa viagem!\033[m')
