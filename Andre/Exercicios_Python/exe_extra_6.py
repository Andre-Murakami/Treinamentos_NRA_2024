class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cidade}"

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def adicionar_endereco(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        return "\n".join(str(endereco) for endereco in self.enderecos)

    def __str__(self):
        return f"Cliente: {self.nome}\nEndereços:\n{self.listar_enderecos()}"

    def __del__(self):
        print(f"Cliente {self.nome} foi deletado. Todos os endereços foram apagados.")
        self.enderecos = []

# aplicativo
if __name__ == "__main__":
    endereco1 = Endereco("Rua A", 123, "Cidade X")
    endereco2 = Endereco("Rua B", 456, "Cidade Y")

    cliente1 = Cliente("João")
    cliente1.adicionar_endereco(endereco1)
    cliente1.adicionar_endereco(endereco2)

    # Imprimindo a lista de endereços de cada cliente1
    print(cliente1)

    del cliente1

    # Tentar acessar o cliente após a deleção 
    try:
        print(cliente1)
    except NameError:
        print("O cliente foi deletado e não pode ser acessado.")
