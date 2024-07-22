#Exercicio 2 - Treinamento Python 2024

altura = float(input('Qual a altura da parede em metros?'))
largura = float(input('Qual a largura da parede em metros?'))

area = largura*altura

print('\n----- Resultado -----\nA area eh de %.2f m2' % area)
print('A quantidade de tinta necessaria eh de {:.2f}\n' .format(area/2))