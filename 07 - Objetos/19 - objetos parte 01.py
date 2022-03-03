class Carro:
    def __init__(self) -> None:
        pass

    def andar(self) -> str:
        return 'Andando!'

    def parar(self) -> str:
        return 'Parado'


carro = Carro()

print(carro.andar())
print(carro.parar())