from listas import lista_nomes_times_zoeiros, lista_nomes_pessoais
from scratch import team_choosen

user_team = []
for c in range(10):
    player = lista_nomes_pessoais()
    user_team.append(player)
    player = lista_nomes_times_zoeiros()
    user_team.append(player)

print(f'{team_choosen} Roster')
for player in user_team:
    print(player)


# class Jogador(self):
