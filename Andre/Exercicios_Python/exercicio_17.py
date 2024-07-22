#Treinamento Python 2024 - SEMEAR

import random

num_aleatorios = tuple(random.randint(1, 100) for _ in range(5))

print("Números gerados:", num_aleatorios)

print("Menor valor:", min(num_aleatorios))
print("Maior valor:", max(num_aleatorios))
