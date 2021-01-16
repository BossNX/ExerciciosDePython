import emoji
dis = float(input('Qual é a distância da sua viagem? '))
if dis <= 200:
    print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dis))
    print('E o preço da sua passagem vai será de R${:.2f}'.format(dis * 0.50))
else:
    print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dis))
    print('E o preço da sua passagem será de R${:.2f}'.format(dis * 0.45))
print(emoji.emojize('Tenha uma boa viagem! :airplane:', use_aliases=True))
