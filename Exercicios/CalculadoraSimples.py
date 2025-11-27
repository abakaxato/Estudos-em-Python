#Para esse exercicio eu devo criar uma calculadora simples (provavelmente eu vou querer colocar algumas coisas a maiskkk).

#Declaração de variaveis
number1 = float(0)
number2 = float(0)
type_calc = str (None)
reply = str (None)
end_prog = 1

while end_prog != 0:


















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
