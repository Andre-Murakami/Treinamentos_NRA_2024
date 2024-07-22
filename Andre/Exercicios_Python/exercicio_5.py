#Exercicio 5 - Treinamento Python 2024

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

print('\n----- Resultado -----')
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    if reta1 == reta2 == reta3:
        tipo_triangulo = 'Equilátero'
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        tipo_triangulo = 'Isósceles'
    else:
        tipo_triangulo = 'Escaleno'
    
    print(f'As retas podem formar um triângulo {tipo_triangulo}.')

else:
    print('As retas não podem formar um triângulo.')
