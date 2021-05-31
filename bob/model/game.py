from dataclasses import dataclass

from bob.model.player import Player


@dataclass
class Game:
    time: float = 0.0
    player: Player = None
