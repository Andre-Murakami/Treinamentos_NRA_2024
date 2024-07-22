class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return f"Eu sou {self.nome}."

class Cliente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def comprar(self):
        return f"{self.nome} está comprando."

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

    def estudar(self):
        return f"{self.nome} está estudando."


# Aplicativo

# Instanciar objetos das três classes
pessoa = Pessoa("Carlos")
cliente = Cliente("Ana")
aluno = Aluno("Sebastiana")

# Verificando que um objeto da classe Aluno de fato é da classe Aluno utilizando o método falar
print(aluno.falar())

# Verificar que não é possível utilizar o método estudar com um objeto da classe Cliente
try:
    print(cliente.estudar())
except AttributeError:
    print("O método estudar não está disponível para a classe Cliente.")

# Verificar que um objeto da classe Pessoa não pode nem estudar nem comprar
try:
    print(pessoa.estudar())
except AttributeError:
    print("O método estudar não está disponível para a classe Pessoa.")

try:
    print(pessoa.comprar())
except AttributeError:
    print("O método comprar não está disponível para a classe Pessoa.")
