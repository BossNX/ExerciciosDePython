print('\033[36;4m-=\033[m'*20)
casa = float(input('Digite o valor da casa: R$'))
salário = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser \033[32mCONCEDIDO!\033[m')
else:
    print('Empréstimo \033[31mNEGADO!\033[m')
print('\033[36;4m-=\033[m'*20)
