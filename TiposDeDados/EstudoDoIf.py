# Não tem muita diferença do IF em JAVA para o IF em Python
# Basicamente temos o "if" que seria o "SE", o "else" que seria o "SENÃO" e o "else" que seria o "SENÃO SE"
# a declaração dos IFs que serem escritos em letras minusculas
# não é recomendado usar chaves para delimitar o bloco de execução do IF em Python, o correto é usar dois pontos (:) e indentação
# também não precisa do () mas eu gosto de delimitar as coisas o maximo possivel

entrada = input("Digite 's' ou 'n' : ")

if(entrada == "s"):
    print("você digitou 's'")
elif(entrada == "n"):
    print("Você digitou 'n'")
else:
    print("você digitou algo diferente de 's' ou 'n' ")
