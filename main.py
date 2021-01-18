import random
from listas import lista_nomes_times_zoeiros, lista_nomes_pessoais, list_teams
import time
from headers import header


# User choose his/her team
while True:
    team_choosen = str(input(f"Select your team: {list_teams()}\n"))
    if team_choosen in list_teams():
        break
    else:
        print('Error!! Choose a valid team.')
        team_choosen = str(input(f"Select your team: {list_teams()}\n"))

# Random choice to teams for the computer
while True:
    comp_1 = random.choice(list_teams())
    if comp_1 != team_choosen:
        break
    else:
        comp_1 = random.choice(list_teams())

while True:
    comp_2 = random.choice(list_teams())
    if comp_2 != team_choosen and comp_2 != comp_1:
        break
    else:
        comp_2 = random.choice(list_teams())

while True:
    comp_3 = random.choice(list_teams())
    if comp_3 != team_choosen and comp_3 != comp_1 and comp_3 != comp_2:
        break
    else:
        comp_3 = random.choice(list_teams())

print(f'\n{header()}')
print('TEAMS IN THE LEAGUE')
time.sleep(0.5)
print(team_choosen)
print(comp_1)
print(comp_2)
print(comp_3)
time.sleep(3)

print(f'\nCONGRATULATIONS! You are the new coach of {team_choosen}, first you need to evaluate the attributes of each player and assign a position to them.')
time.sleep(3)

# Assign players to the teams
user_team_roster = []
for c in range(10):
    player = random.choice(lista_nomes_pessoais())
    while True:
        if player in user_team_roster:
            player = random.choice(lista_nomes_pessoais())
        else:
            break
    user_team_roster.append(player)
    player = random.choice(lista_nomes_times_zoeiros())
    while True:
        if player in user_team_roster:
            player = random.choice(lista_nomes_times_zoeiros())
        else:
            break
    user_team_roster.append(player)

comp1_team_roster = []
for c in range(10):
    player = random.choice(lista_nomes_pessoais())
    while True:
        if player in comp1_team_roster:
            player = random.choice(lista_nomes_pessoais())
        else:
            break
    comp1_team_roster.append(player)
    player = random.choice(lista_nomes_times_zoeiros())
    while True:
        if player in comp1_team_roster:
            player = random.choice(lista_nomes_times_zoeiros())
        else:
            break
    comp1_team_roster.append(player)

comp2_team_roster = []
for c in range(10):
    player = random.choice(lista_nomes_pessoais())
    while True:
        if player in comp2_team_roster:
            player = random.choice(lista_nomes_pessoais())
        else:
            break
    comp2_team_roster.append(player)
    player = random.choice(lista_nomes_times_zoeiros())
    while True:
        if player in comp2_team_roster:
            player = random.choice(lista_nomes_times_zoeiros())
        else:
            break
    comp2_team_roster.append(player)

comp3_team_roster = []
for c in range(10):
    player = random.choice(lista_nomes_pessoais())
    while True:
        if player in comp3_team_roster:
            player = random.choice(lista_nomes_pessoais())
        else:
            break
    comp3_team_roster.append(player)
    player = random.choice(lista_nomes_times_zoeiros())
    while True:
        if player in comp3_team_roster:
            player = random.choice(lista_nomes_times_zoeiros())
        else:
            break
    comp3_team_roster.append(player)

print(f'{team_choosen} Roster')
counter = 1
for player in user_team_roster:
    print(f'{counter} {player}')
    time.sleep(0.5)
    counter += 1
time.sleep(3)

# Assigning values to the players
print(header())
print('Now it is time to evaluate the players...')
print('Loading...')
time.sleep(3)
player_attrib = ['Ball control', 'Passing', 'Dribbling', 'Marking', 'Finishing', 'Physical Condition', 'Endurance']

## Assigning values to the user team
all_teams_list = [team_choosen, comp_1, comp_2, comp_3]
all_teams_rosters = [user_team_roster, comp1_team_roster, comp2_team_roster, comp3_team_roster]
all_teams = {}

    #user team
player_detailed_rating_dict = {}
players_detailedrating_dict = {}
allteams_player_detailedrating_dict = {}
for t in range(20):
    for c in range(7):
        player_rating = random.randint(0, 100)
        player_detailed_rating_dict.update({player_attrib[c]: player_rating})
    players_detailedrating_dict.update({user_team_roster[t]: player_detailed_rating_dict})
allteams_player_detailedrating_dict.update({team_choosen: players_detailedrating_dict})

    #computer team 1
player_detailed_rating_dict = {}
players_detailedrating_dict = {}
for t in range(20):
    for c in range(7):
        player_rating = random.randint(0, 100)
        player_detailed_rating_dict.update({player_attrib[c]: player_rating})
    players_detailedrating_dict.update({comp1_team_roster[t]: player_detailed_rating_dict})
allteams_player_detailedrating_dict.update({comp_1: players_detailedrating_dict})

    #computer team 2
player_detailed_rating_dict = {}
players_detailedrating_dict = {}
for t in range(20):
    for c in range(7):
        player_rating = random.randint(0, 100)
        player_detailed_rating_dict.update({player_attrib[c]: player_rating})
    players_detailedrating_dict.update({comp2_team_roster[t]: player_detailed_rating_dict})
allteams_player_detailedrating_dict.update({comp_2: players_detailedrating_dict})

    #computer team 3
player_detailed_rating_dict = {}
players_detailedrating_dict = {}
for t in range(20):
    for c in range(7):
        player_rating = random.randint(0, 100)
        player_detailed_rating_dict.update({player_attrib[c]: player_rating})
    players_detailedrating_dict.update({comp3_team_roster[t]: player_detailed_rating_dict})
allteams_player_detailedrating_dict.update({comp_3: players_detailedrating_dict})


# ASSIGNING THE OVERALL RATING OF EACH TEAM
teams_overall_rating = []
overallrating_allteams_dict = {}

#   Assigning overall rating for players
for team, players in allteams_player_detailedrating_dict.items():
    overall_player_dict = {}
    for p, r in players.items():
        overall_rating = 0
        for value in r.values():
            overall_rating += value
        overall_rating = round(overall_rating/7, 1)
        overall_player_dict.update({p: overall_rating})
        overallrating_allteams_dict.update({team: overall_player_dict})

#   Assigning tactics rating for each team
teams_tactics_rating = {}
for i in range(4):
    tactics_rating = random.randint(30, 60)
    teams_tactics_rating.update({all_teams_list[i]: tactics_rating})

#   Assigning the player overall rating
player_overall_rating_byteam = {}
for t, r in overallrating_allteams_dict.items():
    x = 0
    for v in r.values():
        x += v
    x = round(x/20, 1)
    player_overall_rating_byteam.update({t: x})

#   Assigning the overall rating
rating_combined = {}
for team, rating in player_overall_rating_byteam.items():
    rating_calc = 0
    for t, r in teams_tactics_rating.items():
        if team == t:
            rating_calc = r
    rating_calc += rating
    rating_calc = round(rating_calc/2, 1)
    rating_combined.update({team: rating_calc})

for i, z in rating_combined.items():
    print(i, z)

'''print(userteam_dict)
print(userteam_overallrating)
print(f'{team_choosen} Overall Rating: {team_overallrating:.0f}')

print(f'\n{comp1team_dict}')
print(comp1team_overall)
print(f'{comp1_team} Overall Rating: {comp1overall_rate:.0f}')

print(f'\n{comp2team_dict}')
print(comp2team_overall)
print(f'{comp2_team} Overall Rating: {comp2overall_rate:.0f}')

print(f'\n{comp3team_dict}')
print(comp3team_overall)
print(f'{comp3_team} Overall Rating: {comp3overall_rate:.0f}')'''