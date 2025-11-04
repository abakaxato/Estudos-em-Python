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
1° forma - usando {} para utilizar variaveis no lugar no texto da String, tem que colocar o "f" antes das aspas
isso também serve para limitar as casas decimais de um float, isso é chamado de f-string, 'f' de format
"""
variavel_Sting = f"meu nome é {nome} e minha idade é {peso:.1f}"
print(variavel_Sting)

"""
2° forma - usando o metodo .format() para formatar a String
ele serve para utilizar parametros dentro de uma String, substituindo os {}
é possivel também limitar as casas decimais de um float, colocando a limitação dentro das chaves correspondentes.
colocando numeros dentro das chaves, podemos definir a ordem dos parametros, senão eles seguem da esquerda para direita
"""
variavel_String2 = "tenho {0:.2f} anos, estou vivo ? : {vida}, meu vulgo é {vulgo}"
"""
também é possivel nomear os parametros dentro das chaves exemplo 'vida'
todos os parametros depois que um foi nomeado, devem ser nomeados também
"""
saida = variavel_String2.format(idade, vida=vivo, vulgo = nome)

print(saida)

#Interpolação básica de Strings
"""
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

#aprofundando a formatação de Strings com f-Strings
variavel_f_string = str = "ABCD"
variavel_f_float = float(12.23)
variavel_f_int = int(298)
print(f'{variavel_f_string}')

    #Chamados de pede = são as repetições de caracteres ao redor da sua string
""" '>' serve pra preencher para a esquerda o caracter que você escolher"""
print(f'{variavel_f_string:7>10}')
""" '<' serve pra preencher para a direita o caracter que você escolher"""
print(f'{variavel_f_string:7<10}')
""" '^' serve pra preencher a sua string no centro do caracter que você escolher"""
print(f'{variavel_f_string:7^10}')

    #Formatação de numeros
""" '.f' serve pra delimitar o numero de casas decimais, tendo que inserir o numero entre o '.' e o 'f' """
print(f"{variavel_f_float:.1f}")
""" '+' serve pra expresar que eu desejo ver o "+" quando o numero for positivo """
print(f"{variavel_f_float:+.1f}")
""" 'x ou X' serve pra exibir o exadecimal do valor """
print(f"{variavel_f_int:2X}")

#Aprofundando o conhecimento no acesso de indices das string sem python
variavel_i_string = "caua ricardo"

    #Usando o fatiamento de strings
"""colocando o indice e um ':' a direita ele vai trazer o valor apos aquele indice"""
print(variavel_i_string[4:])
"""colocando o indice e um ':' a esquerda ele vai trazer o valor antes aquele indice"""
print(variavel_i_string[:4])
"""colocando o indice e um ':' entre outro indice ele vai trazer o valor entre aqueles indices"""
print(variavel_i_string[2:4])
"""colocando mais um ':' depois do intervalo que voce quer se seja exibido, é especificado o pulo de caracteres"""
print(variavel_i_string[0:11:2])
"""colocando um valor negativo no pulo, ele vira a string ao contrario"""
print(variavel_i_string[::-1])


#verificando quantos caracteres tem dentro de uma string
"""A função 'len' pode verificar quantos caracteres tem dentro de uma String"""
variavel_l_string = "joao do pé de feijão"
print( len(variavel_l_string))