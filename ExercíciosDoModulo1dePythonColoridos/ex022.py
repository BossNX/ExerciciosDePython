nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome em \033[31;4mMaiúsculas\033[m é \033[32m{}\033[m'.format(nome.upper()))
print('O seu nome em \033[4;32mMinúsculas\033[m é \033[33m{}\033[m'.format(nome.lower()))
print('O seu nome possui \033[34m{}\033[m letras ao todo'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é \033[35m{}\033[m e possui \033[36m{}\033[m letras'.format(separa[0], len(separa[0])))
