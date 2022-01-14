import random
from defs import Action, Turn
from random import randint

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Player 2"

    def play(turn_index: int, history: list[Turn]) -> Action:
        random_num = randint(1,3)
        if (random_num == 1):
            return Action.CHEAT
        return Action.COOPERATE
