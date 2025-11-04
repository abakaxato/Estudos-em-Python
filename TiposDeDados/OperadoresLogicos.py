#Os operadores Logicos do Python são os mesmos das outras linguagens "and", "or" e "not".
# também temos algums operadores especias como é o caso do "none" que serve para representar um "não valor".

# Uma curiosidade sobre a avaliação das condições é que quando o compilador teste as condições que vão ser comparadas
#  No AND ele para no valor que der FALSE e mostra o output do valor que originou o FALSE
#  No OR ele para no valor que der TRUE e mostra o output do valor que originou o TRUE.

#variaveis utilizadas para os testes
nome_usuario = "caua"
senha_usuario = "senha123"

#começo do programa
parar = "1"
while(parar != "0"):
    entrada_nome_usuario = input("Digite o nome do usuario para iniciar a sessão :")
    entrada_senha_usuario = input("\n Agora digite a senha do usuario correspondente :")
    teste = input("quer testar o AND, OR ou o NOT ? :")
    print(f"Usuario digitado {entrada_nome_usuario}\n Senha digitada {entrada_senha_usuario}\n\n")

    #exemplo de utilização do AND
    if(teste == "and"):
        if (nome_usuario == entrada_nome_usuario and senha_usuario == entrada_senha_usuario):
            print("nome de usuario e senha reconhecidos\nAcesso concedido com sucesso")
        elif(nome_usuario == entrada_nome_usuario and senha_usuario != entrada_senha_usuario):
            print("Senha incorreta")
        else: 
            print("Usuario não identificado")

    #exemplo de utilização do OR
    elif(teste == "or"):
        if(nome_usuario != entrada_nome_usuario or senha_usuario != entrada_senha_usuario):
            print("Sua senha ou o seu nome de usuario estão incorretos")
        else:
            print("Senha e nome do usuario reconhecidos\nAcesso concedido com sucesso")

    #exemplo de utização do NOT
    #Utilizado para inverter a expressão FALSE vira TRUE e TRUE vira FALSE
    elif(teste == "not"):
        if(not nome_usuario != entrada_nome_usuario): 
            print("\n nome correto")
    else:
        parar = input("\nDeseja encerrar o programa ? :")
