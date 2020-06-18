
while(True):
    tabuada = int(input("Digite um número"))
    if(tabuada < 0):
        continue
        print("Olá")
    else:
        for valor in range(0,11):
            print(f"{tabuada}x{valor} = {tabuada*valor}")
    #fazer algo
print("Programa encerrado!")