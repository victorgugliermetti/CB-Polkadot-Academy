programa {
  funcao inicio()
  {
    // Declara uma vari�vel inteira para armazenar o ano
    inteiro ano
    
    // Solicita ao usu�rio para digitar um ano
    escreva("Digite um ano: ")

    // L� o valor inserido pelo usu�rio e armazena na vari�vel 'ano'
    leia(ano)

    // Verifica se o ano � bissexto usando a l�gica correta
    se(ano % 4 == 0)
    { 
      se (ano % 100 == 0)
      { 
        se (ano % 400 == 0)
        { 
          escreva("O ano � bissexto")
        }
        senao
        { 
          escreva("O ano n�o � bissexto")
        }
      }
      senao
      { 
        escreva ("O ano � bissexto")
      }
    }
    senao 
    { 
      escreva ("O ano n�o � bissexto")
    }
    }
  }
