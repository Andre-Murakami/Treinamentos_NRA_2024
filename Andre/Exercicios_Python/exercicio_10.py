#Exercicio 10 - Treinamento Python 2024

while True:
    num = int(input("Digite um número para ver sua tabuada (negativo para sair): "))
    
    if num < 0:
        print("Programa encerrado.")
        break
    
    print(f"--- Tabuada de {num} ---")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 20) 
