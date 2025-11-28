import os
os.system('cls')

def escreva(): #declarando a função
     print('hello word') # o print está dentro da função

def exibir_idade(idade, seunome ): #exemplo diferende de uma função com parametro 
     print(f'{seunome}, vc tem {idade} anos! ')

def multiplicacao(n1, n2): #exemplo diferende de uma função com parametro 
     resultado = n1 * n2
     print(f'o resultado da soma é: {resultado}  ') 

def divisao(Valor, Valor2): #exemplo diferende de uma função com parametro. Porém nessa função utilizamos o return 
     resultado =  Valor / Valor2
     return resultado

escreva() #Chamando a função sem paramatro, nada dentro disso: ()

exibir_idade(18,'Kauã') #Chamando a função com paramatro,com coisa dentro disso: ()

multiplicacao(50,100) #Chamando a função com paramatro,com coisa dentro disso: ()

print (f'A função é: {divisao (30, 2)}')
