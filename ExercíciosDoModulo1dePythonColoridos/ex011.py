largura = float(input('Digite o valor da largura da parede: '))
altura = float(input('Digite o valor da altura da parede: '))
area = largura * altura
tinta = area/2
print('A \033[4márea\033[m é \033[31m{:.1f}m²\033[m então é necessário \033[34m{:.1f}L\033[m de \033[4mtinta\033[m. '.format(area, tinta))
