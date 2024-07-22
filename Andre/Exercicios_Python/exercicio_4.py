#Exercicio 4 - Treinamento Python 2024

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'Abaixo do Peso'
elif imc < 25:
    status = 'Peso Ideal'
elif imc < 30:
    status = 'Sobrepeso'
elif imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

print('\n----- Resultado -----')
print('Seu IMC é: {:.2f}' .format(imc))
print(f'Status: {status}\n')
