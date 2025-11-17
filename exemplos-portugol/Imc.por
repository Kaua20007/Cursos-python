programa {
  
  inclua biblioteca Matematica --> mat 
  // BIBLIOTECA QUE FAZ COM QUE TENHA SOMENTE 2 CASAS APÓS A VIRGULA

  funcao inicio() {
    cadeia nome
    //declrando o nome da variavel
    real altura, peso,imc
    //declarando o nome das variavel
    
    
    escreva("Digite seu nome: ")
    //Pegando nome do user
    leia(nome)
    //utilizando a variavel nome 
    escreva("Digite sua altura: ")
    //Pegando altura do user
    leia(altura)
    //utilizando a variavel altura
    escreva("Digite seu peso: ")
    //Pegando peso do user
    leia(peso)
    //utilizando a variavel peso
    imc = peso / (altura * altura)
    //calculo do imc
   escreva(nome," o seu imc é : ", mat.arredondar(imc,2))
    se( imc <= 18.4) {
      escreva("\nAbaixo do peso")
  }

  senao se( imc <= 24.9)
    escreva("\npeso normal")
  }



   
  
    
   


  }
}
