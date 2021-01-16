import random
import pygame
from time import sleep
print('\033[31m-=\033[m'*30)
print('\033[34mVou pensar em um número entre 0 e 5\033[m! \033[34mConsegue adivinhar\033[m? ')
print('\033[31m-=\033[m'*30)
jogador = int(input('\033[32mEm qual número pensei\033[m? '))
print('PROCESSANDO... ')
sleep(3)
computador = random.randint(0, 5)

if jogador == computador:
    print('\033[32;4mPARABÉNS!\033[m Você me venceu! Eu escolhi o número \033[34m{}\033[m '
          'e você escolheu o número \033[35m{}\033[m!'.format(computador, jogador))
    pygame.mixer.init()
    pygame.mixer_music.load('ex028c.mp3')
    pygame.mixer_music.play()
    input()

else:
    print('\033[31;4mGANHEI\033[m! Você \033[31;4mperdeu\033[m! Eu escolhi o número \033[34m{}\033[m '
          'e você escolheu o número \033[35m{}\033[m!'.format(computador, jogador))
    pygame.mixer.init()
    pygame.mixer_music.load('ex028e.mp3')
    pygame.mixer_music.play()
    input()
