def ficha(player='<unknown>', goals=0):
    player = input('Digite o nome do jogador:')
    goals = input('Digite o número de gols:')
    if goals.isnumeric():
        goals = int(goals)
    else:
        goals = 0
    if player.strip() == '':
        player = '<unknown>'
    print(f'O jogador {player} fez {goals} gols(s) no campeonato')


ficha()
