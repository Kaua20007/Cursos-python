programa {
  funcao inicio() {
    cadeia nome 
    real valor_inteiro , porcentagem , valor_a_parte
     escreva("Digite seu nome: ")
     leia(nome)
     escreva( nome,  ",seja muito bem vindo ao programa de descontos!\n")

    //delcarando os nomes das variavel
    escreva("Digite o valor inteiro: R$" )
    leia(valor_inteiro)
    escreva("Digite a porcentagem: ")
    leia(porcentagem)

    valor_a_parte = valor_inteiro * (porcentagem/100)

    escreva(nome, ",o valor de seu  desconto que é correspondente a " , porcentagem,"% de ","R$",valor_inteiro," é :  R$",valor_a_parte)

  }
}
