from math import radians, sin, cos, tan
angulo_radianos = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo_radianos))
cosseno = cos(radians(angulo_radianos))
tangente = tan(radians(angulo_radianos))
print(f'O ângulo de {angulo_radianos} tem o SENO de: {seno:.2f}')
print(f'O ângulo de {angulo_radianos} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo_radianos} tem o TANGENTE de {tangente:.2f}')