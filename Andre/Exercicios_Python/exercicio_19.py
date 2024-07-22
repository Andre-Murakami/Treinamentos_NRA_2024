lista = []
lista_par = []
lista_impar = []

while True:
    num = input("Digite um numero ou 'e' para sair: ")
    if num.isdigit() or num.startswith('-') and num[1:].isdigit(): # verifica postivos e negativos
        num = int(num)
        lista.append(num)
        if num%2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)

    elif num == "e":
        break
    else:
        print("Você não digitou um numero!")

print("A lista de todos os numeros digitados: ", lista)
print("A lista dos numeros impares : ", lista_impar)
print("A lista dos numeros pares: ", lista_par)
