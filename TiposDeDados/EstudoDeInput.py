# a função que usamos para receber dados do usuario é a função input()

# ela sempre retorna uma String, então se quisermos outro tipo de dado, precisamos converter o valor
# para o tipo desejado

#exemplo de input recebendo uma String

nome = input("Digite seu nome: ");
print(f"Seu nome é {nome}");
#exemplo de input recebendo um inteiro
idade = int(input("Digite sua idade: "));
print(f"Sua idade é {idade}");
#exemplo de input recebendo um float
peso = float(input("Digite seu peso: "));
print(f"Seu peso é {peso}");
#Exemplo de input recebendo um boolean
# o boolean identifica que se o valor for 0, ele é False, se for 1 ou mais, ele é True
esta_vivo = bool(int(input("Digite 1 se você está vivo ou 0 se está morto: ")));
print(f"Você está vivo ? {esta_vivo}");