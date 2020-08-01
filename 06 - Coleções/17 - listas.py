#Declarando
lista = [1,2,3,4]
print(lista2)
#tupla = (1,2,3)

#print(type(lista))
#print(type(tupla))
#Imprimindo
print(lista)

#Inserindo: append() e insert()
lista.append(4)
lista.insert(1, 25)
#print(lista)
#Removendo
lista.remove(25)
#print(lista)

#Acessando pelo indice
print(lista[0])
#for i in range(0,len(lista)):
 #   print(lista[i])


#Fatiando lista
print(lista[1:4])
#Tamanho
print(len(lista))

#Indice do elemento: index(index, start, stop)
print(lista.index(1, 0,4))