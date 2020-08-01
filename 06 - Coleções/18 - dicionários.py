#Declaração
dicionario = { "João" : 27, "Geovana": 24, "Jéssica" : 21}
#print(type(dicionario))
#print(dicionario)

#Adicionar elementos
#Modo 01
#dicionario.update({"Alfredo" : 12})
#Modo 02 chave e valor
dicionario["Maria"] = 12
#dicionario["Maria"] = 300

print(dicionario)

#Removendo elementos
#dicionario.pop("João")
#print(dicionario)
#dicionario.clear()
#print(dicionario)

#Elemenos pelo índice
#print(f'O conteúdo é: {dicionario["Geovana"]}')

#print(dicionario.items())

#Tamanho
#print(len(dicionario))


#Iterando sobre dicionários

#chaves
#for i in dicionario:
    #print(i)

#valores
for i in dicionario.values():
    print(i)