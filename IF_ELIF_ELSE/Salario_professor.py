import os

os.system('cls')

print('Qual é o seu level? 1 - level 1|\n 2 - level 2|\n 3 - level 3 ' )
level = input('Informe o seu level: ')

qtd_aulas = int(input("Qual a quantidade de aulas que vc passa ao decorrer das semanas: "))

if level == '1':
    cash = (qtd_aulas * 12) * 4
elif level == '2':
    cash = (qtd_aulas * 17) * 4
elif level == '3':
    cash =(qtd_aulas * 25) * 4
else:
    print('O level descrito está invalido! ')

print(f'O seu salário será: {cash}')