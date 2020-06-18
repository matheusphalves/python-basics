ativo = True
while(ativo):
    tabuada = int(input("Digite um número"))
    if(tabuada < 0):
        ativo = False
    else:
        for valor in range(0,11):
            print(f"{tabuada}x{valor} = {tabuada*valor}")
    #fazer algo
print("Programa encerrado!")

