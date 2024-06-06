nome = str(input('Digite o seu nome inteiro: ')).strip().lower()
lis = nome.split()
print(f'O seu primeiro nome é {lis[0]}')
print(f'E seu último nome é {lis[-1]}')
