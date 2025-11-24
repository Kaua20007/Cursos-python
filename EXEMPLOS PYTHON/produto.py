import os
os.system('cls')
nome_produto =  input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor do desconto:(%) '))
valor_desconto = preco *desconto / 100
preco_final = preco - valor_desconto
print(f'Produto: {nome_produto} - preço final: ${preco_final}')