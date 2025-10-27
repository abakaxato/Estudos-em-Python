#os operadores aritmetricos são basicamente os mesmos

adicao = 10 + 9
print("adição",adicao)

subtracao = 10 - 9
print("subtração",subtracao)

multiplicacao = 10 * 9
print("multiplicação",multiplicacao)
#multiplicacao entre flout e int

multiplicacao2 = 10 * 0.7
print("multiplicação com float",multiplicacao2)

# o retorno de qualquer divisao sempre vai dar float
divisao = 10 / 10
print("divisão",divisao)

#divisao entre flout e int
divisao2 = 10 / 1.5
print("divisão com float",divisao2)

#divisao com duas barras corta as casas decimais, fica apenas o numero inteiro
divisao3 = 10 // 1.5
print("divisão com 2 barras",divisao3)

#basicamente um numero elevado a outro
exponeciacao = 2 ** 10 
print("Exponeciação",exponeciacao)

#Resto da divisao
resto_da_divisao = 10 % 3
print("Resto da divisão", resto_da_divisao)

#colocando '+' no lugar no ',' ele junta os valores sem colocar um divisor entre eles se forem strings
print("concatenação usando '+'","um"+"dois"+"tres"+"quatro")

#colocando o sinal de multiplicação com uma string ele vai fazer a repetição
a_muitas_vezes = "A" * 8
print("letra vezes numero", a_muitas_vezes)

#ordem dos operadores = os que estiverem entre parenteses, exponencias, divisões e multiplicações e no final soma e subtração
# 1° (n + n)
# 2° **
# 3° */ // %
# 4° + -
# se estiverem no mesmo nível e estiverem na mesma conta, serão executados da esquerda para a direita

conta = 1 + 1 ** 5 + 5 #valor desejado 1024
conta_certa = (1 + 1) ** (5 + 5)
print("Ordem das operações",conta)
print("Ordem das operações certa",conta_certa)