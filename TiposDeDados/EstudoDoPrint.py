#o python por padrao quebra linha(pula) de um print para outro colocando um "\n" oculto no final
#para mudar esse padrão no final voce pode usar o argumento "end"

# o python também coloca espaco entreas variaveis por padrão, de forma oculta
#para mudar o separador que esta ficando no lugar da virgula, usamos a funcao sep

# o "\n" é o pulo de linha aqui do windows, isso pode mudar de OS pra OS
# colocando um "\" ou um "r" o compilador do python ignora o proximo caracter como uma possivel funcao

#print sem mudanca
print(1,2,"tres quatro\n\n")

#print mudando o final para nao quebrar a linha e adicionar um "**"
print(1,2,"tres quatro",end="")
print(1,2,"tres quatro",end="**")

#print mudando o tipo de separador para "-"
print('\n')
print(1,2,"tres quatro\n",sep="-")

#print mudando o separador para "+"
print(1,2,"tres quatro\n",sep='+')

#print ignorando a "(aspa) em questao do "\" (possivel também usar ' dentro de " ou vise versa)
print(1,2,"tres \"quatro\"\n",sep='+')
print(1,2,"tres 'quatro'\n",sep='+')

#formatação de Strings
#declaração de variaveis para formatação
idade = int (22);
nome = "Cauã Ricardo";
peso = 44.44;
esta_vivo = True;


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

#também é possivel mostrar qual é o nome da variavel e o valor dela usando o "=" dentro das chaves
variavel_String3 = "nome={n}, idade={i}, peso={p:.2f}, vivo={v}".format(n=nome, i=idade, p=peso, v=esta_vivo)
print(variavel_String3)
