from random import randint
import playsound
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número você pensou? '))
print('PROCESSANDO... ')
sleep(3)
computador = randint(0, 5)
if jogador == computador:
    print('PARABÉNS! Você acertou! Eu escolhi {} e você escolheu {} também! '.format(computador, jogador))
    playsound.playsound('ex028.mp3')
else:
    print('VOCÊ ERRROU! Eu escolhi {} e você escolheu {}'.format(computador, jogador))
    playsound.playsound('errou.mp3')
print('Foi muito bom jogar com você!')
