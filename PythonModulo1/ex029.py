velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h!')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dai! Dirija com segurança')
