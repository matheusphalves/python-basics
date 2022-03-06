#A conversão se dá pela seguinte forma. Por exemplo, para a sequência 1011, temos 
#decimal = 1 X 2^(3) + 0 X 2^(2) + 1 X 2^(1) + 1 X 2^(0)
# = 8 + 0 + 1 = 11

#00 2^n = 4

#230 = 200 + 30 + 0 = 2*10^2 + 3*10^1 + 0*10^0

#00 = 0*2^(1) + 0*2^(0) = 0 + 0 = 0
#01 = 0*2^(1) + 1*2^(0) = 0 + 1 = 1
#10 = 1*2^(1) + 0*2^(0) = 2 + 0 = 2
#11 = 1*2^(1) + 1*2^(0) = 2 + 1 = 3


def toDecimal(bitList):
    valorTotal = 0
    contador = 1

    for bitAtual in bitList:
        valorTotal += bitAtual*2**(len(bitList) - contador)
        contador += 1

    return valorTotal

print(toDecimal([1, 1, 1, 1, 1]))