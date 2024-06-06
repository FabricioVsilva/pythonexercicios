velocidade = int(input('Qual é a sua velocidade? '))
if velocidade > 80:
    print('Multado! Você excedeu a velocidade de 80km/h')
    multa = (velocidade - 80) * 7
    print(f'R${multa:.2f} em multa')
print(f'Boa viagem!')