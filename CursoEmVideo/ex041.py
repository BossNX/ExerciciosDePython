ano = int(input('Qual o ano de nascimento do aluno? '))
from datetime import date
atual = date.today().year
idade = atual - ano
if 1 < idade <= 9:
    print('Esse aluno possui \033[32m{}\033[m anos, então sua categoria é \033[34mMIRIM\033[m'.format(idade))
elif idade == 1:
    print('Esse aluno possui \033[32m{}\033[m ano, então sua categoria é \033[34mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('Esse aluno possui \033[33m{}\033[m anos, então sua categoria é \033[34mINFANTIL\033[m'.format(idade))
elif idade <= 19:
    print('Esse aluno possui \033[35m{}\033[m anos, então sua categoria é \033[34mJUNIOR\033[m'.format(idade))
elif idade <= 25:
    print('Esse aluno possui \033[36m{}\033[m anos, então sua categoria é \033[34mSÊNIOR\033[m'.format(idade))
else:
    print('Esse aluno possui \033[31m{}\033[m anos, então sua categoria é \033[34mMASTER\033[m'.format(idade))
