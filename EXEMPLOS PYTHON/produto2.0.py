import os
os.system('cls')

nome_produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor do desconto (%): '))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print('\n=== RESUMO DO PRODUTO ===')
print(f'Produto: {nome_produto}')
print(f'Preço original: R${preco:.2f}')
print(f'Desconto aplicado: {desconto}%')
print(f'Valor do desconto: R${valor_desconto:.2f}')
print(f'Preço final: R${preco_final:.2f}')
