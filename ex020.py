import random
p1 = str(input('Primeira pessoa: '))
p2 = str(input('Segunda pessoa: '))
p3 = str(input('Terceira pessoa: '))
p4 = str(input('Quarta pessoa: '))
list = [p1, p2, p3, p4]
random.shuffle(list)
print(f'A sequência da prova é: {list}')