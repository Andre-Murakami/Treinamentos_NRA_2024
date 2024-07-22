class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)

    def esta_vazio(self):
        return len(self.produtos) == 0

    def __str__(self):
        if self.esta_vazio():
            return "O carrinho está vazio."
        else:
            produtos_str = "\n".join(str(produto) for produto in self.produtos)
            return f"Produtos no carrinho:\n{produtos_str}\nTotal: R${self.calcular_total():.2f}"


# Exemplo de uso
if __name__ == "__main__":
    p1 = Produto("Maçã", 1.50)
    p2 = Produto("Banana", 2.00)
    p3 = Produto("Laranja", 3.00)

    carrinho = CarrinhoDeCompras()
    print(carrinho)  # Ainda vazio aqui

    carrinho.adicionar_produto(p1)
    carrinho.adicionar_produto(p2)
    carrinho.adicionar_produto(p3)

    print(carrinho)  # Aqui o carrinho esta com p1, p2 e p3
