n1 = int(input('\033[35mPrimeiro valor:\033[m '))
n2 = int(input('\033[33mSegundo valor:\033[m '))
n3 = int(input('\033[32mTerceiro valor:\033[m '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O \033[36mmaior\033[m número digitado foi \033[36m{}\033[m'.format(maior))
print('O \033[31mmenor\033[m número digitado foi \033[31m{}\033[m'.format(menor))
