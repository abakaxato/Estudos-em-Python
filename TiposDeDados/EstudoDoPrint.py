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
