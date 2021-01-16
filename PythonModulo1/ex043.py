peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[31mABAIXO DO PESO\033[m.')
elif 18.5 <= imc < 25:
    print('Você está com \033[32mPESO IDEAL\033[m.')
elif 25 <= imc < 30:
    print('Você está com \033[33mSOBREPESO\033[m.')
elif 30 <= imc < 40:
    print('Você está com \033[35mOBESIDADE\033[m.')
elif imc >= 40:
    print('Você está com \033[31mOBESIDADE MÓRBIDA!!\033[m.')
