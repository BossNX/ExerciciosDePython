num = int(input('Digite um número: '))
Limpa = '\033[m'
ant = num - 1
suc = num + 1
print('O \033[34;4mnúmero{} é \033[32;4m{}{}, o seu \033[33;4mantecessor{} é \033[31;4m{}{} e o seu \033[35;4msucessor{} é \033[36;4m{}{}'.format(Limpa, num, Limpa, Limpa, ant, Limpa, Limpa, suc, Limpa))
