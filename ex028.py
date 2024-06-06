import random
print('Vou pensar em um número, tente adivinhar...')
pergunta = int(input('Qual número eu pensei: '))
numerocomputador = random.randint(0, 5)
print(f'Pensei em {numerocomputador}')
if numerocomputador == pergunta:
     print(f'Acertouuu!')
else:
    print('Errou!')


