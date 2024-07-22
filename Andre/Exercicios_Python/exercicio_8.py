#Exercicio 8 - Treinamento Python 2024

total_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
mulheres_menos_20 = 0

for i in range(4):
    print(f"Digite os dados da {i+1} pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()
    
    total_idade += idade #p/ calacular a media de idade
    
    if sexo == 'M' and (idade > idade_homem_mais_velho or idade_homem_mais_velho == 0):
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

media_idade = total_idade / 4

print("\n--- Resultados ---")
print(f"Média de idade do grupo: {media_idade:.2f} anos")
if nome_homem_mais_velho:
    print(f"Nome do homem mais velho: {nome_homem_mais_velho}")
else:
    print("Nenhum homem foi incluído")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
