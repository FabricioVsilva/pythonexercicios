a = float(input('Segmento um: '))
b = float(input('Segmento dois: '))
c = float(input('Segmento três: '))
if a < b + c and b < a + c and c < a + b:
     print(f'Forma um triangulo!')
else:
     print(f'Não forma um triangulo!')