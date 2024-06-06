import datetime
ano = int(input('Digite o ano para saber se é bissexto ou não. 0 para o ano atual: '))
if ano == 0:
     ano = datetime.date.today().year
     print(f'{ano}')
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
     print(f'Bissexto')
else:
     print('Não é bissexto')