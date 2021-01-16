largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m². \nPara pintar essa parede, você precisará de {:.2f}L de tinta.'.format(largura, altura, área, (área/2)))
