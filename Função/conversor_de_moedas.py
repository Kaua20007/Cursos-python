import os 

def exibir_menu(): #função que exibe o menu
    print('\n === COONVERSOR DE MOEDASD ===')
    print('[1] Converter DOLAR - > REAL')
    print('[2] Converter REAL - > DOLAR')
    print('[0] Sair')

def converter_dolar_para_real(qtd_dolar, taxa):
    return qtd_dolar / taxa

def converter_real_para_dolar(qtd_real, taxa):
    return qtd_real * taxa


def main(): #Principal função do programa
    os.system('cls')
    taxa_cambio = float(input('Informe a taxa de câmbio'
    '(1 USD = Quantos BRL?): '))

    resposta = 'sim'

    while resposta == 'sim':
        exibir_menu() #chamando a principal função
        opcao = input('escolha uma opção: ') #Solicitando a opção do usúario

        if opcao == '1':
            quantidade_dolar = float(input('Digite o valor em DOLAR: '))
            total_convertido_em_dolar = converter_dolar_para_real(quantidade_dolar, taxa_cambio)
            print(f'USD {quantidade_dolar: .2f} = R${total_convertido_em_dolar: .2f}')
        elif opcao == '2':
            quantidade_real = float(input('Digite o valor em REAL: '))
            total_convertido_em_real = converter_real_para_dolar(quantidade_real, taxa_cambio)
            print(f'R${quantidade_real: .2f} = USD {total_convertido_em_real: .2f}')
        elif opcao == '0':
            print('encerrando o programa, até a proxima')
        else:
            print('Essa opção não existe, por favor faça da forma correta!')


        

main()