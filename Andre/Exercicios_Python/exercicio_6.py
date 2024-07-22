primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

contador = 0
termosPA = []

print('Os 10 primeiros termos da PA são:')
while contador < 10:
    termo_atual = primeiro_termo + contador * razao
    termosPA.append(str(termo_atual))
    contador += 1

print(', '.join(termosPA))

while True:
    resposta = input('\nVocê deseja ver mais alguns termos? (s/n): ').strip().lower()
    if resposta == 'n':
        break
    elif resposta == 's':
        mais = int(input('Quantos termos a mais você deseja ver? '))
        for _ in range(mais):
            termo_atual = primeiro_termo + contador * razao
            print(termo_atual, end=' ,')
            contador += 1
    else:
        print('Resposta inválida. Por favor, digite "s" para sim ou "n" para não.')

print('\nPrograma encerrado.')
