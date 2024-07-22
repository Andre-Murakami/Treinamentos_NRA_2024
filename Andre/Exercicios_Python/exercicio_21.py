import numpy as np

# 1. Crie duas matrizes NumPy 3x3, A e B, preenchidas com valores aleatórios de 0 a 9.
A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 3))

# 2. Imprima as duas matrizes.
print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)

# 3. Calcule a soma das duas matrizes e armazene o resultado em uma terceira matriz C.
C = A + B

# 4. Imprima a matriz resultante C.
print("\nMatriz C (A + B):")
print(C)

# 5. Calcule o produto elemento a elemento das duas matrizes A e B e armazene o resultado em uma quarta matriz D.
D = A * B

# 6. Imprima a matriz resultante D.
print("\nMatriz D (A * B elemento a elemento):")
print(D)

# 7. Calcule o produto das matrizes A e B e armazene o resultado em uma quinta matriz E. (não é o produto elemento a elemento, queremos E = AB)
E = A @ B

# 8. Imprima a matriz E.
print("\nMatriz E (A * B):")
print(E)
