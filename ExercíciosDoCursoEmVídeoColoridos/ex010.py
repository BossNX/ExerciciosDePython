real = float(input('Quanto você possui na carteira? R$'))
dolar = real / 4.05  # Valor em janeiro de 2020
print('Com \033[4;32mR${:.2f}\033[m, você pode comprar \033[4;34mUS${:.2f}\033[m'.format(real, dolar))
