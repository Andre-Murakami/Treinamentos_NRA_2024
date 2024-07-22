class Caneta:
    def __init__(self, marca, cor):
        self._marca = marca  
        self._cor = cor  

    def escrever(self):
        print(f"Caneta {self._marca} está escrevendo na cor {self._cor}.")

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.caneta = None  

    def escrevendo(self):
        if self.caneta:
            self.caneta.escrever()
        else:
            print(f"{self.nome} não tem uma caneta para escrever.")

caneta = Caneta("BIC", "azul")

escritor = Escritor("João")

escritor.caneta = caneta

escritor.escrevendo()  
