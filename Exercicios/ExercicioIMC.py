#Declaração de variaveis
preco1 = float; produto1=str;
preco2 = float; produto2=str;
preco3 = float; produto3=str;
preco4 = float; produto4=str;
preco5 = float; produto5=str;
role = bool; cr = int (0);
soma = float(0); sys = str(1);

#Inicio do programa
print("Olá, seja bem vindo a loja\n");
print("Antes de começarmos, gostaria de saber se voce é cliente ou colaborador...\n");
print("por favor, se voce é cliente digite '1' senão, se for colaborador, digite '2'\n");

while(sys != str(0)):

    while(cr != str(3) and role != True and role != False):
        cr = input("Digite 1 para cliente, 2 para colaborador ou 3 para sair: ");
        if (cr == str(1)):
            role = True;
            print("\nLegal !!!\n Seja bem vindo a nossa loja");
        elif (cr ==str(2)):
            role = False;
            print("\nOpa !!!\n Seja bem vindo de volta colaborador");
        elif (cr ==str(3)):
            role = False;
            print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
        else:
            print("\nValor inválido, digite 1 ou 2 para selecionar entre cliente ou colaborador, ou digite 3 para sair da sessão\n");
        

    if (role == True):
        if(not produto1 or produto2 or produto3 or produto4 or produto5):
            print("\nNossa loja está sem produtos no momento, por favor volte mais tarde\n");
            break
        else: 
            print("\nAgora que sabemos que voce é cliente, vamos começar as compras\n");
            
            print("Esses são os produtos disponiveis no momento\n");
            print("Produto 1: ", produto1, " Preço: R$", preco1);
            print("Produto 2: ", produto2, " Preço: R$", preco2);
            print("Produto 3: ", produto3, " Preço: R$", preco3);
            print("Produto 4: ", produto4, " Preço: R$", preco4);
            print("Produto 5: ", produto5, " Preço: R$", preco5 );
            
            print("Esta interessado em comprar algum produto desses ?")
            print("Se sim, digite o numero do produto que deseja comprar, se não, digite 0 para sair\n");
            
            while(soma != 0):
                cat = input("Numero do produto desejado (1 a 5) ou 0 para sair: ")
                if (cat == 1):
                    soma = soma + preco1;
                    print("\nvalor atual de compra R$"+ str(soma) + " : ");
                    input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                    if (input == 's'):
                        print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
                    else:
                        continue;
                elif (cat == 2):
                    soma = soma + preco2;
                    print("\nvalor atual de compra R$"+ str(soma) + " : ");
                    input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                    if (input == 's'):
                        print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
                    else:
                        continue;
                elif (cat == 3):
                    soma = soma + preco3;
                    print("\nvalor atual de compra R$"+ str(soma) + " : ");
                    input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                    if (input == 's'):
                        print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
                    else:
                        continue;
                elif (cat == 4):
                    soma = soma + preco4;
                    print("\nvalor atual de compra R$"+ str(soma) + " : ");
                    input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                    if (input == 's'):
                        print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
                    else:
                        continue;
                elif (cat == 5):
                    soma = soma + preco5;
                    print("\nvalor atual de compra R$"+ str(soma) + " : ");
                    input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                    if (input == 's'):
                        print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
                    else:
                        continue;
                elif (cat == 0):
                    print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
                else:
                    print("\nValor inválido, por favor digite um valor entre 0 e 5\n");
    else:
        print("\nAgora que sabemos que voce é colaborador, vamos cadastrar produtos\n");
        
        produto1 = input("Digite o nome do produto 1: ");
        preco1 = float(input("Digite o preço do produto 1: R$"));
        
        produto2 = input("Digite o nome do produto 2: ");
        preco2 = float(input("Digite o preço do produto 2: R$"));
        
        produto3 = input("Digite o nome do produto 3: ");
        preco3 = float(input("Digite o preço do produto 3: R$"));
        
        produto4 = input("Digite o nome do produto 4: ");
        preco4 = float(input("Digite o preço do produto 4: R$"));
        
        produto5 = input("Digite o nome do produto 5: ");
        preco5 = float(input("Digite o preço do produto 5: R$"));
        
        print("\nProdutos cadastrados com sucesso !!!\n");
sys = input("Deseja reiniciar o sistema ? (digite 's' para sim ou 'n' para não) : ");
    if (sys == 's'):
        sys = str(1);
        cr = str(0);
    else:
        sys = str(0);
else:
    print("\nSistema finalizado, obrigado por usar nosso sistema !!!\n");
        


        








