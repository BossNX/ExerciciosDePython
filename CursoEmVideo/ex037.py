número = int(input('\033[35mDigite um número inteiro:\033[m '))
print('Escolha uma das bases para conversão: ')
print('\033[33;1m[1]\033[m converter para \033[33;4;1mBINÁRIO\033[m')
print('\033[36;1m[2]\033[m converter para \033[36;4;1mOCTAL\033[m')
print('\033[34;1m[3]\033[m converter para \033[34;4;1mHEXADECIMAL\033[m')
opção = int(input('Sua opção: '))
if opção == 1:
    print('Seu número convertido para \033[33;4;1mBINÁRIO\033[m é igual a \033[32m{}\033[m'.format(bin(número)[2:]))
elif opção == 2:
    print('Seu número convertido para \033[36;4;1mOCTAL\033[m é igual a \033[32m{}\033[m'.format(oct(número)[2:]))
elif opção == 3:
    print('Seu número convertido para \033[34;4;1mHEXADECIMAL\033[m é igual a \033[32m{}\033[m'.format(hex(número)[2:]))
else:
    print('\033[31;4;1mEssa opção é inválida! Tente novamente!\033[m')
