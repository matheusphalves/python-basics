valorA = float(input('Inserir valor A: '))
valorB = float(input('Inserir valor B: '))


#Declaração da função
def calcularMedia(a,b):
    return (a+b)/2

#Invocando nossa função
resultado = calcularMedia(valorA, valorB)
resultado2 = calcularMedia(valorA + 0.5, valorB + 2)
print(resultado + resultado2)