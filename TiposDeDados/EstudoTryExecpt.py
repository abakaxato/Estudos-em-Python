#Try exception serve para tratar as exceções e mostrar um caminho quando elas ocorrerem

#exemplo de tratamento de exceção quando tetamos calcular um texto quando deveria ser um numéro
valor = input ("Digite um valor numero pra eu lhe mostrar ele duplicado : ")

try:
    valor_numerico = int (valor)
    print(f"O valor que você digitou foi {valor_numerico} e esse valor duplicado é {valor_numerico * 2}")
except ValueError:
    print("você não digitou um numero")