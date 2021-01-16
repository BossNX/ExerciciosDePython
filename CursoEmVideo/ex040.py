nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5:
    print('\033[31mREPROVADO!\033[m Sua média é \033[31m{:.1f}\033[m. '.format(média))
elif 5 <= média < 7:
    print('\033[33mRECUPERAÇÃO!\033[m Sua média é \033[33m{:.1f}\033[m. '.format(média))
elif média >= 7:
    print('\033[32mAPROVADO!\033[m Sua média é \033[32m{:.1f}\033[m. '.format(média))
