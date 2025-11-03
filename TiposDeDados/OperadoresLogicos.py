#Os operadores Logicos do Python são os mesmos das outras linguagens "and", "or" e "not"
# também temos algums operadores especias como é o caso do "none" que serve para representar o vazio

#variaveis utilizadas para os testes
nome_usuario = "caua"
senha_usuario = "senha123"

#começo do programa
parar = "1"
while(parar != "0"):
    entrada_nome_usuario = input("Digite o nome do usuario para iniciar a sessão :")
    entrada_senha_usuario = input("\n Agora digite a senha do usuario correspondente :")
    teste = input("quer testar o AND, OR ou o NOT ? :")

    #exemplo de utilização do AND
    if (nome_usuario == entrada_nome_usuario and senha_usuario == entrada_senha_usuario):
        print("Acesso concedido com sucesso")
    elif(nome_usuario == entrada_nome_usuario and senha_usuario != entrada_senha_usuario):
        print("Senha incorreta")
    else: 
        print("Usuario não identificado")

    #exemplo de utilização do OR


















    parar = input("\nDeseja encerrar o programa ? :")
