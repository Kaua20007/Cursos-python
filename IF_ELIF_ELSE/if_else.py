import os 

os.system('cls')

# Cores ANSI
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura) 
imc_arredondado = round(imc, 2)

print(f'\nOlá {nome}, seu IMC é de: {imc_arredondado}\n')

if imc < 16:
    print(RED + f' {nome}, você está com MAGREZA GRAVE.' + RESET)
elif imc <= 16.9:
    print(RED + f' {nome}, você está com MAGREZA MODERADA.' + RESET)
elif imc <= 18.4:
    print(BLUE + f' {nome}, você está com MAGREZA LEVE.' + RESET)
elif imc <= 24.9:
    print(GREEN + f' {nome}, você está SAUDÁVEL.' + RESET)
elif imc <= 29.9:
    print(YELLOW + f' {nome}, você está com PRÉ-OBESIDADE.' + RESET)
elif imc <= 34.9:
    print(RED + f' {nome}, você está com OBESIDADE MODERADA (Grau I).' + RESET)
elif imc <= 39.9:
    print(RED + f' {nome}, você está com OBESIDADE SEVERA (Grau II).' + RESET)
else:
    print(RED + f' {nome}, você está com OBESIDADE MÓRBIDA (Grau III).' + RESET)
