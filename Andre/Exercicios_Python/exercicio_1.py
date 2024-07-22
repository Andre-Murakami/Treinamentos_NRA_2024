#Exercicio 1 - Treinamento Python 2024

num_dias = int(input('Quantos dias o veiculo foi alugado?'))
km_rodados = float(input('Quantos Km foi veiculo foi rodado?'))

valor_pagar = (num_dias*60) + (km_rodados*0.15)

print(' O valor a ser pago sera R$ %.2f' % valor_pagar)