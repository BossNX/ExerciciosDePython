num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
dem = num // 10000 % 10
cem = num // 100000 % 10
mi = num // 1000000 % 10
print('Analisando o número {} '.format(num))
print('Unidade: {} '.format(u))
print('Dezena: {} '.format(d))
print('Centena: {} '.format(c))
print('Milhar: {} '.format(m))
print('Dezena de Milhar: {} '.format(dem))
print('Centena de Milhar: {} '.format(cem))
print('Milhão: {} '.format(mi))
