c = float(input('Qual é a temperatura atual em °C? '))
f = c * 9 / 5 + 32
print('A temperatura \033[34;4m{:.1f}°C\033[m é equivalente à \033[31;4m{:.1f}°F\033[m'.format(c, f))
