salário = float(input('Digite o seu salário: '))
aumento = salário + (salário / 100 * 12)
print(f'Meus parabéns! Você recebeu um aumento de 12% de R${salário:.2f} agora é R${aumento:.2f}')