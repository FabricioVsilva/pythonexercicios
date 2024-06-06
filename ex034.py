salario = float(input('Digite o seu salário R$'))
if salario > 1250:
    print(f'Você teve um aumento de 10% agora seu salário passa a ser R${(salario / 100 * 10) + salario:.2f}')
elif salario <= 1250:
    print(f'Você teve um aumento de 15% agora seu salário passa a ser R${(salario / 100 * 15) + salario:.2f}')
