import os
os.system('cls')
#criando uma variavel
numero = int(input('Digite seu número: ')) # pedindo o número para o usuruario
#outra variavel 
i = 1 # começo da tabuada 

while i <= 10: # declarando o começo e o fin
    print(f' {i} x {numero} = {i * numero}') #calculo da tabuada 
    i += 1 # almenta o valor da variavel em 1 a cada repetição
