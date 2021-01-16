import playsound
velocidade = float(input('\033[32mQual a velocidade do seu carro?\033[m '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('\033[31;4mMULTADO!\033[m Você \033[35mexcedeu\033[m o limite de \033[36m80km/h\033[m e terá que '
          'pagar uma \033[31mmulta\033[m de \033[31mR${:.2f}\033[m'.format(multa))
    playsound.playsound('ex029.mp3')

print('\033[32mTenha um bom dia!\033[m \033[34mDirija com segurança!\033[m')
