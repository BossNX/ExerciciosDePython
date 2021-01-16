print('\033[31;1m=\033[m' * 20, '\033[34;4;1mLOJINHA\033[m', '\033[31;1m=\033[m' * 20)
preço = float(input('\033[36;1mPreço das compras: R$\033[m'))
print('\033[32;4;1mFORMAS DE PAGAMENTO\033[m')
print('[ 1 ] à vistas dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 4:
    parc = int(input('Quantas parcelas? '))
    if parc == 2 or parc == 1:
       print('\033[31;1mEscolha Inválida!\033[m \033[31mNOT STONKS!\033[m \033[36;1mTente novamente.\033[m')
    else:
        total = preço + (preço * 20 / 100)
        parcela = total / parc
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parc, parcela))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção != 1 and opção != 2 and opção != 3 and opção != 4:
    print('\033[31;1mOPÇÃO INVÁLIDA\033[m de pagamento. Tente novamente!')
