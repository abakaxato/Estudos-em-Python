#Em suma de que a String tem muias particuliaridades, decidi criar um modulo especifico para estudar apenas esse tipo de dado em python

nome = str ("Cauã Ricardo")
peso = float (44.00)
idade = int (22)
vivo = True


#exemplo de acesso ao indice da String para acessar o primeiro valor
#O indice ignora os espaços
print(nome[0])
print(nome[-12])

#formatação de Strings

"""
1° forma - usando {} oara utilizar variaveis no lugar no texto da String, tem que colocar o "f" antes das aspas
isso também serve para limitar as casas decimais de um float, isso é chamado de f-string, 'f' de format
"""
variavel_Sting = f"meu nome é {nome} e minha idade é {peso:.1f}"
print(variavel_Sting)

"""
2° forma - usando o metodo .format() para formatar a String
ele serve para utilizar parametros dentro de uma String, substituindo os {}
é possivel também limitar as casas decimais de um float, colocando a limitação dentro das chaves correspondentes
"""

"""
colocando numeros dentro das chaves, podemos definir a ordem dos parametros, senão eles seguem da esquerda para direita
"""
variavel_String2 = "tenho {0:.2f} anos, estou vivo ? = {vida}, meu vulgo é {vulgo}"
"""
também é possivel nomear os parametros dentro das chaves exemplo 'vida'
todos os parametros depois que um foi nomeado, devem ser nomeados também
"""
saida =variavel_String2.format(idade, vida=vivo, vulgo = nome)

print(saida)

"""
Interpolação básica de Strings

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

É utilizada para referenciar dados utilizando o '%' junto de um desses caracters acima
tem que informar os argumentos da função podendo ser variavel ou um valor estatico
"""
interpolacao = "%s é o seu nome, e %.1f é o seu peso" %(nome,peso)
print(interpolacao)

"""Testando o hexadecimal"""
print("O hexadecimal de %i é %X"%(2490,2490))
