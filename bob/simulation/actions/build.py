from typing import List

from bob.model.entities import BuildingType, Villager
from bob.model.game import Game
from bob.simulation.actions.action import Action
from bob.simulation.actions.common import find_producer_for_entity


class Build(Action):
    def __init__(self, villager: Villager, building_type: BuildingType):
        self.villager = villager
        self.building_type = building_type

    @staticmethod
    def get_actions(game: Game) -> List[Action]:
        player = game.player
        actions = []
        for building_type in player.building_types:
            producer = find_producer_for_entity(player, building_type)
            if producer is not None:
                actions.append(Build(producer, building_type))
        return actions

