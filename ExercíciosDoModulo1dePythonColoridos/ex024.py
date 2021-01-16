cid = str(input('\033[34;4mQual a cidade que você mora\033[m? ')).strip()
sim = '\033[32;4mSIM\033[m'
não = '\033[31;4mNÃO\033[m'
if cid[:5].upper() == 'SANTO':
    print('A cidade começa com \033[35;4mSANTO\033[m? {}'.format(sim))
else:
    print('A cidade começa com \033[35;4mSANTO\033[m? {}'.format(não))
