
from math import hypot
opos = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(opos, ad)
print(f'{hipotenusa:.2f}')

#ou

opos = float(input('Comprimento do cateto oposto: '))
ad = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (opos ** 2 + ad ** 2) ** (1/2)
print(f'{hipotenusa:.2f}')


