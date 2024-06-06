distância = int(input('Qual é a distância: '))
if distância > 200:
     preço = 0.45
     print(f'Sua passagem ficou no valor de R${(preço) * distância:.2f}')
else:
     preço = 0.50
     print(f'Sua passagem ficou no valor de R${(preço) * distância:.2f}')
