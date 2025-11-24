import os
os.system('cls')
print('''

🅗🅔🅛🅛🅞 🅦🅞🅡🅓 ☭

''')
nome = input('Digite seu nome: ')
nota_1 = float(input('Digite a sua primeira nota: '))
nota_2 = float(input('Digite a sua segunda nota: '))
nota_3 =  float(input('Digite a sua terceira nota: '))

resultado = (nota_1 + nota_2 + nota_3) /3
print(round(resultado, 2))

if resultado >= 5:
    print(f'{nome}, vc passouuuu!, sua nota final foi: {resultado} ')
elif resultado >= 4:
    print(f'{nome}, vc está de recuperação, melhora seu vacilão!, sua nota foi só isso: {resultado} ')
else:
    print(f'{nome}, vc reprovouuuuuuuuuuu!, vc conseguiu tira essa nota: {resultado} ') 

input('Pressione a tecla enter para fechar o programa.')

