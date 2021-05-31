from copy import deepcopy, copy
from dataclasses import dataclass
from typing import List

from bob.model.entities import EntityType, BuildingType, UnitType
from bob.model.game import Game
from bob.model.player import Player


@dataclass
class Action:
    pass


def cost_satisfied(player: Player, entity_type: EntityType):
    return (
        entity_type.food_cost <= player.food
        and entity_type.wood_cost <= player.wood
        and entity_type.coin_cost <= player.coin
    )


def not_at_limit(player: Player, entity_type: EntityType):
    if isinstance(entity_type, UnitType):
        ents = [u for u in player.units if u.type == entity_type]
    else:
        ents = [b for b in player.buildings if b.type == entity_type]
    return len(ents) < entity_type.limit


def can_build_building(player: Player, building_type: BuildingType):
    return len([u for u in player.units if u.type.name == "villager"]) > 0


def can_build_unit(player: Player, unit_type: UnitType):
    potential_trainers = [b for b in player.buildings if unit_type in b.type.trainable_units]
    for building in potential_trainers:
        if building.production_status is None:
            return True
        else:
            ps = building.production_status
            if ps.unit_type == unit_type and ps.batch_size < unit_type.max_training_batch_size:
                return True
    return False


def can_build(player: Player, entity_type: EntityType):
    return (
        # we must be able to pay for the unit
        cost_satisfied(player, entity_type)
        and not_at_limit(player, entity_type)
        and (
            (isinstance(entity_type, BuildingType) and can_build_building(player, entity_type))
            or (isinstance(entity_type, UnitType) and can_build_unit(player, entity_type))
        )
    )


def get_actions(game: Game) -> List[Action]:
    actions = []
    player = game.player

    for building_type in player.building_types:
        if can_build(player, building_type):
            actions.append(("build", building_type))
        for unit_type in building_type.trainable_units:
            if can_build(player, unit_type):
                actions.append(("train", unit_type))

    return actions
