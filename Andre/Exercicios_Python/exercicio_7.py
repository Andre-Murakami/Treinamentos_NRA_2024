#Exercicio 7 - Treinamento Python 2024

cont_mais_18 = 0
cont_homens = 0
cont_mulheres_menos_20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    if idade > 18:
        cont_mais_18 += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres_menos_20 += 1

    continuar = input("Você quer continuar? (S/N): ").strip().upper()
    if continuar == 'N':
        break

print('---- Resultado ------')
print(f"A) Quantas pessoas tem mais de 18 anos: {cont_mais_18}")
print(f"B) Quantos homens foram cadastrados: {cont_homens}")
print(f"C) Quantas mulheres tem menos de 20 anos: {cont_mulheres_menos_20}")
