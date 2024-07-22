import random

num_aleatorios = [random.randint(1, 100) for _ in range(5)]

print("Números gerados:", num_aleatorios)

menor_valor = min(num_aleatorios)
maior_valor = max(num_aleatorios)
posicao_menor = num_aleatorios.index(menor_valor)
posicao_maior = num_aleatorios.index(maior_valor)

print(f"Menor valor: {menor_valor} está na posição {posicao_menor}")
print(f"Maior valor: {maior_valor} está na posição {posicao_maior}")
