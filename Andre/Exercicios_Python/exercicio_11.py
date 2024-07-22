#Exercicio 11 - Treinamento Python 2024

valor = int(input("Digite o valor a ser sacado: R$ "))

cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0

if valor >= 50:
    cedulas_50 = valor // 50
    valor = valor % 50

if valor >= 20:
    cedulas_20 = valor // 20
    valor = valor % 20

if valor >= 10:
    cedulas_10 = valor // 10
    valor = valor % 10

if valor >= 1:
    cedulas_1 = valor

print(f"Serão entregues:")
print(f"{cedulas_50} cédulas de R$50")
print(f"{cedulas_20} cédulas de R$20")
print(f"{cedulas_10} cédulas de R$10")
print(f"{cedulas_1} cédulas de R$1")
