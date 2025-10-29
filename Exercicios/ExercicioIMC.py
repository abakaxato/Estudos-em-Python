#Declaração de variaveis
preco1 = None; produto1=None;
preco2 = None; produto2=None;
preco3 = None; produto3=None;
preco4 = None; produto4=None;
preco5 = None; produto5=None;
role = bool(None); entrada = str (0);
soma = float(0); sys = str(1);
compras = int(1); comprando = str();
cliente1 = str(); cliente2 = str();
cliente3 = str(); cliente_atual = str();

#Inicio do programa
while(sys != str(0)):
    print("\n\n\n\nOlá, seja bem vindo a loja\n");
    print("Antes de começarmos, gostaria de saber se voce é cliente ou colaborador...\n");
    print("por favor, se voce é cliente digite '1' senão, se for colaborador, digite '2'\n");

    while(entrada != str(2) and entrada != str(1)):
        entrada = input("\nDigite 1 para cliente, 2 para colaborador ou digite qualquer coisa para sair: ");
        if (entrada == str(1)):
            role = True;
            print("\nLegal !!!\n Seja bem vindo a nossa loja");
            while(cliente_atual != cliente1 and cliente_atual != cliente2 and cliente_atual !=cliente3):
                print("\nPor favor, selecione qual cliente voce é\n");
                print("1 - ", cliente1);
                print("2 - ", cliente2);
                print("3 - ", cliente3);
                cliente_atual = input("\nDigite o numero do cliente que voce é (1 a 3): ");
                if (cliente_atual == str(1)):
                    cliente_atual = cliente1;
                elif (cliente_atual == str(2)):
                    cliente_atual = cliente2;
                elif (cliente_atual == str(3)):
                    cliente_atual = cliente3;
                else:
                    print("\nValor inválido, por favor digite um valor entre 1 e 3\n");
        elif (entrada ==str(2)):
            role = False;
            print("\n\n\n\nOpa !!!\n Seja bem vindo de volta colaborador");
        elif (entrada ==str(3)):
            role = False;
            print("\nObrigado por visitar nossa loja, volte sempre !!!\n");
        else:
            print("\nValor inválido, digite 1 ou 2 para selecionar entre cliente ou colaborador, ou digite 3 para sair da sessão\n");
        

        if (role == True):
            if(not produto1 or not produto2 or not produto3 or not produto4 or not produto5):
                print("\n Desculpe", cliente_atual,":(")
                print("\nNossa loja está sem produtos no momento, por favor volte mais tarde\n");
            else: 
                print("\n Muito bem", cliente_atual,":)")
                print("Agora que sabemos que voce é cliente, vamos começar as compras\n");
            
                print("Esses são os produtos disponiveis no momento\n");
                print("Produto 1: ", produto1, " Preço: R$", preco1);
                print("Produto 2: ", produto2, " Preço: R$", preco2);
                print("Produto 3: ", produto3, " Preço: R$", preco3);
                print("Produto 4: ", produto4, " Preço: R$", preco4);
                print("Produto 5: ", produto5, " Preço: R$", preco5 );
            
                print("Esta interessado em comprar algum produto desses ?")
                print("Se sim, digite o numero do produto que deseja comprar, se não, digite 0 para sair\n");
            
                while(compras != 0):
                    try:
                        cat = int(input("\nNumero do produto desejado (1 a 5) ou 0 para sair: "))
                    except ValueError:
                        print("\nValor inválido, por favor digite um valor entre 0 e 5\n");
                        continue;
                    if (cat == 1):
                        soma = soma + preco1;
                        print("\nVocê adicionou", produto1, "ao carrinho.");
                        print("\nvalor atual de compra R$"+ str(soma) + " : ");
                        comprando = input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                        if (comprando == 's'):
                            compras = 0;
                            print("\nObrigado por visitar nossa loja",cliente_atual,"!, volte sempre !!!\n");
                            print("\n voce fechou uma compra de no valor de R$"+ str(soma) + " : ");
                        else:
                            continue;
                    elif (cat == 2):
                        soma = soma + preco2;
                        print("\nVocê adicionou", produto2, "ao carrinho.");
                        print("\nvalor atual de compra R$"+ str(soma) + " : ");
                        comprando = input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                        if (comprando == 's'):
                            compras = 0;
                            print("\nObrigado por visitar nossa loja",cliente_atual,"!, volte sempre !!!\n");
                            print("\n voce fechou uma compra de no valor de R$"+ str(soma) + " : ");
                        else:
                            continue;
                    elif (cat == 3):
                        soma = soma + preco3;
                        print("\nVocê adicionou", produto3, "ao carrinho.");
                        print("\nvalor atual de compra R$"+ str(soma) + " : ");
                        comprando = input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                        if (comprando == 's'):
                            compras = 0;
                            print("\nObrigado por visitar nossa loja",cliente_atual,"!, volte sempre !!!\n");
                            print("\n voce fechou uma compra de no valor de R$"+ str(soma) + " : ");
                        else:
                            continue;
                    elif (cat == 4):
                        soma = soma + preco4;
                        print("\nVocê adicionou", produto4, "ao carrinho.");
                        print("\nvalor atual de compra R$"+ str(soma) + " : ");
                        comprando = input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                        if (comprando == 's'):
                            compras = 0;
                            print("\nObrigado por visitar nossa loja",cliente_atual,"!, volte sempre !!!\n");
                            print("\n voce fechou uma compra de no valor de R$"+ str(soma) + " : ");
                        else:
                            continue;
                    elif (cat == 5):
                        soma = soma + preco5;
                        print("\nVocê adicionou", produto5, "ao carrinho.");
                        print("\nvalor atual de compra R$"+ str(soma) + " : ");
                        comprando = input("quer fechar a compra ? (digite 's' para sim ou 'n' para não) : ");
                        if (comprando == 's'):
                            compras = 0;
                            print("\nObrigado por visitar nossa loja",cliente_atual,"!, volte sempre !!!\n");
                            print("\n voce fechou uma compra de no valor de R$"+ str(soma) + " : ");
                        else:
                            continue;
                    elif (cat == 0):
                        print("\nObrigado por visitar nossa loja",cliente_atual,"!, volte sempre !!!\n");
                    else:
                        print("\nValor inválido, por favor digite um valor entre 0 e 5\n");
        elif (role == False):
            print("\nAgora que sabemos que voce é colaborador, vamos cadastrar produtos\n");
        
            produto1 = input("Digite o nome do produto 1: ");
            while True:
                try:
                    preco1 = float(input("Digite o preço do produto 1: R$"));
                    break
                except ValueError:
                    print("\nValor inválido, por favor digite um valor numérico para o preço\n");
        
            produto2 = input("Digite o nome do produto 2: ");
            while True:
                try:
                    preco2 = float(input("Digite o preço do produto 2: R$"));
                    break
                except ValueError:
                    print("\nValor inválido, por favor digite um valor numérico para o preço\n");
        
            produto3 = input("Digite o nome do produto 3: ");
            while True:
                try:
                    preco3 = float(input("Digite o preço do produto 3: R$"));
                    break
                except ValueError:
                    print("\nValor inválido, por favor digite um valor numérico para o preço\n");
        
            produto4 = input("Digite o nome do produto 4: ");
            while True:
                try:
                    preco4 = float(input("Digite o preço do produto 4: R$"));
                    break
                except ValueError:
                    print("\nValor inválido, por favor digite um valor numérico para o preço\n");
        
            produto5 = input("Digite o nome do produto 5: ");
            while (True):
                try:
                    preco5 = float(input("Digite o preço do produto 5: R$"));
                    break
                except ValueError:
                    print("\nValor inválido, por favor digite um valor numérico para o preço\n");
        
            print("\n\nAgora, cadastre os clientes da loja\n");
            cliente1 = input("Digite o nome do cliente 1: ")
            print("cliente",cliente1,"cadastrado com sucesso !!!\n");
            cliente2 = input("Digite o nome do cliente 2: ")
            print("cliente",cliente2,"cadastrado com sucesso !!!\n");
            cliente3 = input("Digite o nome do cliente 3: ")
            print("cliente",cliente3,"cadastrado com sucesso !!!\n");   
                
            print("\nProdutos e clientes cadastrados com sucesso !!!\n");
    while(sys != str(0)):
        sys = input("Deseja reiniciar o sistema ? (digite 's' para sim ou 'n' para não) : ");
        if (sys == 's'):
            sys = str(1);
            entrada = str(0);
            soma = float(0);
            compras = int(1);
        elif(sys == 'n'):
            sys = str(0);
            print("\nSistema finalizado, obrigado por usar nosso sistema !!!\n");
        else:
            print("\nEntrada inválida, Digite um valor valido e tente novamente !!!\n");


    
        


        








