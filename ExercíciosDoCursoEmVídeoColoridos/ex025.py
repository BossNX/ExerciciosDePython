nome = str(input('Digite seu nome completo: ')).strip()
sim = '\033[32;4mSIM\033[m'
não = '\033[31;4mNÃO\033[m'
if 'SILVA' in nome.upper():
    print('Tem \033[35;4mSILVA\033[m no nome? {}'.format(sim))
else:
    print('Tem \033[4;35mSILVA\033[m no nome? {}'.format(não))
