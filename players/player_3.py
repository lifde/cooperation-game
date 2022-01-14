from defs import Action, Turn

class Player:
    gain: int = 0
    turn_gain: int = 0
    cooperate_count: int = 0
    cheat_count: int = 0
    name: str = "Landry et William"

    def play(turn_index: int, history: list[Turn]) -> Action:
        if len(history) == 0:
            return Action.COOPERATE
        else:
            return history[-1]["opponent_action"]
        
