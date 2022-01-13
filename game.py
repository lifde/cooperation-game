from players.player_0 import Player as player_0
from players.player_1 import Player as player_1
from players.player_2 import Player as player_2
from players.player_3 import Player as player_3
from players.player_4 import Player as player_4
from players.player_5 import Player as player_5
from players.player_6 import Player as player_6
from players.player_7 import Player as player_7

from defs import Turn, Action

players: list = [
  player_0,
  player_1,
  player_2,
  player_3,
  player_4,
  player_5,
  player_6,
  player_7
]

fights_done = []

def tournament():
    for player in players:
        player.gain = 0
        player.cooperate_count = 0
        player.cheat_count = 0

    for player_i in players:
        for player_j in players:
            if (player_i != player_j):
                fight_id = sorted([player_i.name, player_j.name])
                
                if fight_id not in fights_done:
                    fight(player_i, player_j)
                    fights_done.append(fight_id)

    show_results()
    show_behaviors()

def fight(player_i, player_j):
    print("\n\n==================================================")
    print(player_i.name, "VS", player_j.name)
    print("==================================================")
    player_i_history: list[Turn] = []
    player_j_history: list[Turn] = []
    player_i.turn_gain = 0
    player_j.turn_gain = 0

    for turn in range(10):
        print("\nROUND", turn + 1)
        try:
            player_i_action = player_i.play(turn, player_i_history)
        except:
            player_i_action = Action.COOPERATE

        try:
            player_j_action = player_j.play(turn, player_j_history)
        except:
            player_j_action = Action.COOPERATE

        if player_i_action == Action.COOPERATE:
            player_i.cooperate_count += 1
        else:
            player_i.cheat_count += 1

        if player_j_action == Action.COOPERATE:
            player_j.cooperate_count += 1
        else:
            player_j.cheat_count += 1
        
        if (player_i_action == Action.COOPERATE and player_j_action == Action.COOPERATE):
            print(player_i.name, "et", player_j.name, "coopèrent")
            gain(player_i, 2)
            gain(player_j, 2)
        elif (player_i_action == Action.CHEAT and player_j_action == Action.CHEAT):
            print(player_i.name, "et", player_j.name, "ont triché tous les deux !")
        elif (player_i_action == Action.CHEAT and player_j_action == Action.COOPERATE):
            print(player_i.name, "a trahi", player_j.name, "!")
            gain(player_i, 3)
            gain(player_j, -1)
        elif (player_i_action == Action.COOPERATE and player_j_action == Action.CHEAT):
            print(player_j.name, "a trahi", player_i.name, "!")
            gain(player_i, -1)
            gain(player_j, 3)

        player_i_history.append({
            "self_action": player_i_action,
            "opponent_action": player_j_action
        })

        player_j_history.append({
            "self_action": player_j_action,
            "opponent_action": player_i_action
        })


def gain(player, amount: int):
    player.gain += amount
    player.turn_gain += amount

    if (amount > 0):
        print(player.name, "gagne", amount, "pièces (total", player.turn_gain, ")")
    else:
        print(player.name, "perd", amount, "pièce (total", player.turn_gain, ")")


import matplotlib.pyplot as plt

def show_results():
    print("\n\n==================================================")
    x_axis = []
    y_axis = []

    for player in players:
        x_axis.append(player.name)
        y_axis.append(player.gain)

        print(player.name, ":", player.gain)

    plt.bar(x_axis, y_axis)
    plt.title('Résultats')
    plt.xlabel('Joueur')
    plt.ylabel('Gain')
    plt.savefig('result.png')
    plt.close()

def show_behaviors():
    behavior_x_axis = []
    behavior_y_axis = []

    for player in players:
        behavior_x_axis.append(player.name)
        if player.cooperate_count == 0:
            behavior_y_axis.append(0)
        else:  
            behavior_y_axis.append((player.cooperate_count / (player.cooperate_count + player.cheat_count)) * 100)

    plt.bar(behavior_x_axis, behavior_y_axis)
    plt.title('Pourcentage de coopération')
    plt.xlabel('Joueur')
    plt.ylabel('Coopération')
    plt.savefig('coop.png')
    plt.close()
        
tournament()
