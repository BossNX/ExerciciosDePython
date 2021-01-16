from time import sleep
import random
print('\033[31;1m-=\033[m'*12)
print('\033[34;1m{:^24}\033[m'.format('JOKENPÔ'))
print('\033[31;1m-=\033[m'*12)
print('\033[32;1;4mSuas opções:\033[m ')
print('\033[33;1m[ 1 ] PEDRA\033[m')
print('\033[35;1m[ 2 ] PAPEL\033[m')
print('\033[36;1m[ 3 ] TESOURA\033[m')
jogador = int(input('\033[31mQual é a sua jogada?\033[m '))
pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'
jokenpo = [pedra, papel, tesoura]
computador = random.choice(jokenpo)
if jogador == 1 or jogador == 2 or jogador == 3:
    print('\033[32;1mJO\033[m')
    sleep(1)
    print('\033[34;1mKEN\033[m')
    sleep(1)
    print('\033[31;1mPÔ!!!\033[m')
    if jogador == 1:
        jogador = pedra
    elif jogador == 2:
        jogador = papel
    elif jogador == 3:
        jogador = tesoura
    print('\033[36;1m-=\033[m'*12)
    print('\033[31;1mComputador jogou\033[m \033[35m{}\033[m'.format(computador))
    print('\033[32;1mJogador jogou\033[m \033[35m{}\033[m'.format(jogador))
    print('\033[36;1m-=\033[m'*12)
    if jogador == pedra and computador == papel:
        print('\033[31;1mCOMPUTADOR VENCE\033[m')
    elif jogador == papel and computador == tesoura:
        print('\033[31;1mCOMPUTADOR VENCE\033[m')
    elif jogador == tesoura and computador == pedra:
        print('\033[31;1mCOMPUTADOR VENCE\033[m')
    elif jogador == computador:
        print('\033[34;1mEMPATE\033[m')
    else:
        print('\033[32;1mJOGADOR VENCE\033[m')
else:
    print('\033[31;1mOPÇÃO INVÁLIDA!\033[m Tente novamente.')
