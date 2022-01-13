from enum import Enum
from typing import TypedDict

class Action(Enum):
    CHEAT = 0
    COOPERATE = 1

class Turn(TypedDict):
    self_action: Action
    opponent_action: Action