#Exercicio 3 - Treinamento Python 2024

valor_casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o salario do comprador?'))
anos = int(input('Quantos anos de financiamento?'))

prestacao = valor_casa/(anos*12)

print('\n----- Resultado -----')
if prestacao > (0.3 * salario):
    print('Emprestimo negado. Valor excede o valor da prestacao {:.2f} excede o limite de {:.2f}.' .format(prestacao,0.3 * salario))
else:
    print('Emprestimo concedido. A parcela sera de {:.2f}\n' .format(prestacao))
