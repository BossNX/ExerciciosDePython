dia = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km percorridos? '))
preço = (dia * 60) + (km * 0.15)
print('O preço a ser pago será de \033[31;4mR${:.2f}\033[m!'.format(preço))
