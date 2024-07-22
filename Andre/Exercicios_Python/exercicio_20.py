nome = ''
gols = 0
partidas = 0
lista = []


while True:
    nome = input('Digite o nome do jogador: ')
    partidas = int(input(f'Digite o número de partidas jogadas por {nome}: '))
    gols_por_partida = []
    
    for i in range(partidas):
        gols = int(input(f'Quantos gols na partida {i+1}? '))
        gols_por_partida.append(gols)
        
    total_gols = sum(gols_por_partida)
    dicionario = {'nome': nome, 'partidas': partidas, 'gols_por_partida': gols_por_partida, 'total_gols': total_gols}
    lista.append(dicionario)

    if input("Deseja adicionar mais jogadores? (s para sim / n para não): ").lower() == "n":
        break

print("\n--- Informações dos jogadores ---")
for jogador in lista:
    print(f"Nome: {jogador['nome']}, Partidas: {jogador['partidas']}, Gols por partida: {jogador['gols_por_partida']}, Total de gols: {jogador['total_gols']}")

total_gols_time = sum(jogador['total_gols'] for jogador in lista)
print(f"\nTotal de gols do time: {total_gols_time}")
