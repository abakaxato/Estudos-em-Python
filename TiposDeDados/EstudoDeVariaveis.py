# A principal diferenca da declaração de variavel em python para o JAVA e que podemos não dizemos o tipo
# a outra diferença que existe é a ordem, java = "tipo variavel = valor", Python = "variavel = tipo (valor)"
# é possivel declarar um valor de um tipo diferente para a variavel e ela vai alocar o valor automaticamente
#Outra particuliariedade é o snake case no Python. java = nomeComposto, Python = nome_composto

#declaracao de interiro
# não precisa especificar o tipo da variavel
idade = int (22);
#declaracao de String
nome = "Cauã Ricardo";
#Declaracao de float
peso = 44.44;
#declaracao de boolean
esta_vivo = True;

#formatação de Strings

#1° forma - usando {} oara utilizar variaveis no lugar no texto da String, tem que colocar o "f" antes das aspas
# isso também serve para limitar as casas decimais de um float, isso é chamado de f-string, 'f' de format
variavel_Sting = f"meu nome é {nome} e minha idade é {peso:.1f}"
print(variavel_Sting)
#2° forma - usando o metodo .format() para formatar a String
#ele serve para utilizar parametros dentro de uma String, substituindo os {}
#é possivel também limitar as casas decimais de um float, colocando a limitação dentro das chaves correspondentes

# colocando numeros dentro das chaves, podemos definir a ordem dos parametros, senão eles seguem da esquerda para direita
variavel_String2 = "tenho {0:.2f} anos, estou vivo ? = {vida}, meu vulgo é {vulgo}"
#também é possivel nomear os parametros dentro das chaves exemplo 'vida'
#todos os parametros depois que um foi nomeado, devem ser nomeados também
saida =variavel_String2.format(idade, vida=esta_vivo, vulgo = nome)

print(saida)