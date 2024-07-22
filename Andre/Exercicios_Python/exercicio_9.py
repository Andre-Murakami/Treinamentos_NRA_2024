#Exercicio 9 - Treinamento Python 2024

soma = 0
num = 0

for _ in range (6):

    num = int(input('Digite um nume inteiro: '))

    if num % 2 == 0: 
        soma += num

print (f'A soma dos numeros pares digitados é {soma}')