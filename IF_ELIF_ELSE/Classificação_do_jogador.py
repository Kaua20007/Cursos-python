import os
os.system('cls')

idade = int(input('Digite idade do jogador: '))

if idade >=5 and idade <=7:
    print('Jogador é um infatil A')
elif idade >=8 and idade <=11:
    print('Jogador é um infatil B ')
elif idade >=12 and idade <=13:
    print('Jogador é um juvenil A')
elif idade >=14 and idade <=17:
    print('Jogador é um juvenil B')
elif idade >=18>:
    print(" Jogador profissional ")
else:
    print('Com essa idade o jogador não pode praticar o esporte no momento')
