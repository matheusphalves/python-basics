def solucao1(listaParadas):
    totalPessoas = 0
    for parada in listaParadas:
        totalPessoas += parada[0]
        totalPessoas -= parada[1]
        print(f'Total passageiros: {totalPessoas}')
    return totalPessoas

def solucao2(listaParadas):
    totalEntrada = 0
    totalSaida = 0
    for parada in listaParadas:
        totalEntrada += parada[0]
        totalSaida += parada[1]

    return totalEntrada - totalSaida



#print(solucao1([[10,0],[3,5],[5,8]]))
#print(solucao2([[10,0],[3,5],[5,8]]))
print(solucao1([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))
print(solucao2([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))


