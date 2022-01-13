from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Player 7"

    def play(turn_index: int, history: list[Turn]) -> Action:
        return Action.COOPERATE
