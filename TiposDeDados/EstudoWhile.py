#O while funciona igual a maioria das linguagens

contador = 0

while contador < 100:
    print(contador)
    contador +=1

 #Reiniciando o Loop usando o continue
    if contador == 40:
        print(contador)
        continue

 #Quebrando o while usando o braak para parar o loop
    if contador == 60:
        print (f"{contador}")
        break
