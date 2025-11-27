#Para esse exercicio eu devo criar uma calculadora simples (provavelmente eu vou querer colocar algumas coisas a maiskkk).

#Declaração de variaveis
number1 = float(0)
number2 = float(0)
type_calc = str (None)
reply = str (None)
end_prog = 1
name = str (None)
val = 0
val2 = ""

# Inicio do programa
while end_prog != 0:
    name = input("Olá !\n por favor digite seu nome : ")
    
    print(f"Ok, {name.capitalize()} ! Vamos iniciar...\n")

    #validação das entradas do usuário
    while val == 0:
        try :
            number1 = float(input("Por favor digite o primeiro número : "))
            val = 1
        except ValueError:
            print("\n DIGITE APENAS NUMEROS... \n")
    while val == 1:
        try :
            number2 = float(input("\nPor favor digite o segundo número : "))
            val = 0
        except ValueError:
            print("\n DIGITE APENAS NUMEROS... \n")
    
    while val != 1:
        print(f"Esses são os números que você digitou {number1} e {number2}.\n Qual tipo de operação você quer fazer ?")
        val2 = input("\n digite '+' para Adição\ndigite '-' para subtração\ndigite 'x' para multiplicação\ndigite '/' para Divisão\n")
        if val2 == "+":
            print("O resultado da sua adição é " + (number1 + number2))
            val = 1
        elif val2 == "-":
            print("O resultado da sua subtração é " + (number1 - number2))
            val = 1
        elif val2 == "x":
            print("O resultado da sua multiplicação é " + (number1 * number2))
            val = 1
        elif val2 == "+":
            print("O resultado da sua divisão é " + (number1 / number2))
            val = 1
        else:
            print("Você não digitou um operador desconhecido")
            val = 0
















 #Final do programa(Loop de confirmação)
    while reply.lower() != "sim" and reply.lower() != "não"  or end_prog == 1:
        reply = input("Você deseja finalizar o programa ? Responda com sim ou não : ")
        print(reply.lower())
        if reply.lower() == "sim":
            print("OK ! O programa foi encerrado...")
            end_prog = 0
        elif reply.lower() == "não":
            print("OK ! O programa foi reiniciado...\n")
            end_prog = 1
        else : print("Responda com sim ou não")
