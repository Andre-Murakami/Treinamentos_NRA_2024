class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.falando = False
        self.comendo = False

    def comer (self, comida):
        if self.falando:
            print(f"{self.nome} esta falando e nao pode comer!")
        else:
            self.comendo = True
        print(f"{self.nome} esta comendo {comida}")

    def interromper_comer (self):
        if self.comendo:
            self.comendo = False
            print(f"{self.nome} parou de comer.")

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar enquanto está comendo.")
            return
        self.falando = True
        print(f"{self.nome} está falando sobre {assunto}.")

    def interromper_falar(self):
        if self.falando:
            self.falando = False
            print(f"{self.nome} parou de falar.")


pessoa = Pessoa("Sebastiana")

pessoa.comer("jaca")
pessoa.falar("Amostra de cinema iraniano")
pessoa.interromper_comer()
pessoa.falar("A morte da bezerra")
pessoa.comer("Acai com banana e paçoca")