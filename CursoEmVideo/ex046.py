from time import sleep
import playsound
import emoji
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!!!!')
print(emoji.emojize('Bum!!! \033[31m:fireworks:\033[m', use_aliases=True))
playsound.playsound('ex046.mp3')
