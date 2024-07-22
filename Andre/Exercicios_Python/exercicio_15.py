#Exercicio 15 - Treinamento Python 2024

def maior(*numeros):
    if numeros:
        maior_numero = max(numeros)
        print(f"O maior número entre {numeros} é {maior_numero}.")
    else:
        print("Nenhum número foi fornecido.")

maior(10, 33, 51, 67, 91)
maior(10, 20, 30, 40)
maior(-1, -5, -3, -4)
