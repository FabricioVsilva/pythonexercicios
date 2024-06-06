larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
área = larg * alt
print(f'Seu quarto tem: {área:.2f} m²')
pintura = área / 2
print(f'Para pintar o seu quarto vamos precisar de {pintura:.2f} litros de tinta')