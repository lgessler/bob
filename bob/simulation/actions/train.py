from typing import List

from bob.model.entities import UnitType, Building
from bob.model.game import Game
from bob.simulation.actions.action import Action
from bob.simulation.actions.common import find_trainer_for_unit


class Train(Action):
    def __init__(self, trainer: Building, unit_type: UnitType):
        self.trainer = trainer
        self.unit_type = unit_type

    @staticmethod
    def get_actions(game: Game) -> List[Action]:
        player = game.player
        actions = []
        for building_type in player.building_types:
            for unit_type in building_type.trainable_units:
                trainer = find_trainer_for_unit(player, unit_type)
                if trainer is not None:
                    actions.append(Train(trainer, unit_type))
        return actions
