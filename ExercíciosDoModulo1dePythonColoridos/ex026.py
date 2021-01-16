frase = str(input('\033[36mDigite uma frase:\033[m ')).strip().upper()
print('\033[36mA letra\033[m \033[31mA\033[m '
      '\033[36maparece\033[m \033[34m{}\033[m \033[36mvezes na\033[m \033[32mfrase\033[m'.format(frase.count('A')))
print('\033[36mEla aparece pela primeira vez na posição\033[m \033[32m{}\033[m'.format(frase.find('A') + 1))
print('\033[36mEla aparece pela última vez na posição\033[m \033[32m{}\033[m'.format(frase.rfind('A') + 1))
