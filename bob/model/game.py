from dataclasses import dataclass

from bob.model.player import Player


@dataclass
class Game:
    timestep: int = 0
    player: Player = None