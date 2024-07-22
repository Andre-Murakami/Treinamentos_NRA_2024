class Produto:
    def __init__(self, nome):
        self._nome = None
        self.nome = nome  # Utiliza o setter para garantir que o nome seja armazenado em maiúsculas

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str):
            self._nome = valor.upper()
        else:
            raise ValueError("O nome deve ser uma string.")

# Exemplo de uso:
produto = Produto("laptop")
print(produto.nome)  # Output: LAPTOP
produto.nome = "mouse"
print(produto.nome)  # Output: MOUSE
