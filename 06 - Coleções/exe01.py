def highAndLow(string: str):
    listaNumeros = string.split(" ")
    high = int(listaNumeros[0]) 
    low =  int(listaNumeros[0])

    for numeroAtual in listaNumeros[1:]:
        if(int(numeroAtual) > high):
            high = int(numeroAtual)

        if(int(numeroAtual) < low):
            low = int(numeroAtual)
    
    return (low, high)


print(highAndLow('14 2 3 4 5'))