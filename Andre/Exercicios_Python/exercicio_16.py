#Exercicio 16 - Treinamento Python 2024

def leiaInt(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Erro! Digite um número inteiro válido.")

# Exemplo de uso
n = leiaInt('Digite um numero: ')
print(f'Você digitou o numero {n}.')
