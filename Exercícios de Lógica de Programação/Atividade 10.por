programa {
  funcao inicio() 
  {
    inteiro numero, contador = 0

    para(inteiro i = 1; i <= 5; i++)

    { 
      escreva ("Digite o n�mero ", i, ": ")
      leia(numero)

      se (numero > 0)
      { 
        contador++
      }
    }
    escreva("Voc� digitou ", contador, " numeros positivos.")
  } 
}
