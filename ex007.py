nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))
média = (nota1 + nota2) / 2
print(f'A média é: {média}')
if média >= 6:
     print('Meus parabéns! Você passou')
else:
     print('Reprovado! Média menor que 6')