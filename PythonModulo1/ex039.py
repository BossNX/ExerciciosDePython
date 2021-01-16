from datetime import date
gênero = str(input('Qual é o gênero? ')).strip().upper()
if gênero == 'MASCULINO':
    nascimento = int(input('Digite o ano de nascimento: '))
    anoatual = date.today().year
    idade = anoatual - nascimento
    falta1 = 18 - idade
    falta2 = idade - 18
    if idade == 1:
        print('Quem nasceu em {} tem {} ano em {}.'.format(nascimento, idade, anoatual))
    else:
        print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoatual))
    if falta1 != 1 and idade < 18:
        print('Ainda faltam {} anos para o alistamento'.format(falta1))
        print('Seu alistamento será em {}.'.format(anoatual + (falta1)))
    elif falta1 == 1:
        print('Ainda falta {} ano para o alistamento'.format(falta1))
        print('Seu alistamento será em {}.'.format(anoatual + (falta1)))
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif falta2 != 1 and idade > 18:
        print('Você já deveria ter se alistado há {} anos'.format(falta2))
        print('Seu alistamento foi em {}.'.format(anoatual - (falta2)))
    elif falta2 == 1:
        print('Você já deveria ter se alistado há {} ano'.format(falta2))
        print('Seu alistamento foi em {}.'.format(anoatual - (falta2)))
elif gênero == 'FEMININO':
    print('Você não precisa fazer o alistamento obrigatório.')
else:
    print('Gênero inválido! Tente novamente!')
