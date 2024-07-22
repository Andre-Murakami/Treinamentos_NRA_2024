#Exercicio 13 - Treinamento Python 2024

frase = input('Digite uma frase: ')

frase_upper = frase.upper()

numA = frase_upper.count('A')

primeiroA = frase_upper.find('A') + 1 

ultimoA = frase_upper.rfind('A') + 1 

print('--- Resultado ---')
print(f'A letra "A" aparece {numA} vezes na frase.')
print(f'A primeira ocorrência da letra "A" está na posição {primeiroA}.')
print(f'A última ocorrência da letra "A" está na posição {ultimoA}.')
