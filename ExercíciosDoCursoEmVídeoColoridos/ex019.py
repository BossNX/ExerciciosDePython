import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
print('Dos quatro \033[34malunos sorteados\033[m, aquele que '
      'vai \033[35mapagar\033[m o quadro será \033[31;4m{}\033[m!'.format(random.choice(alunos)))
