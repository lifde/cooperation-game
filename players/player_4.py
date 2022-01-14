from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Lucalixte"

    def play(turn_index: int, history: list[Turn]) -> Action:
        print("history", history)
        if turn_index % 2:
            return Action.COOPERATE
        else
            return Action.CHEAT
