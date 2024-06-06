dia = int(input('Quantos dia você ficou com o carro? '))
km = float(input('Quantos Km você rodou com o carro? '))
valorPago = (dia * 110) + (km * 0.50)
print(f'Tudo ficou R${valorPago:.2f}')