valor = float(input('Qual o valor do produto? '))
desconto = valor - (valor / 100 * 10)
print(f'O produto com desconto de 10% está saindo de R${valor:.2f} por R${desconto:.2f} ')
