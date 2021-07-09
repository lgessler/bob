from bob.model.entities import EntityType, UnitType, BuildingType, VillagerTask, Villager
from bob.model.player import Player


def cost_satisfied(player: Player, entity_type: EntityType):
    return (
            entity_type.food_cost <= player.food
            and entity_type.wood_cost <= player.wood
            and entity_type.coin_cost <= player.coin
    )


def not_at_limit(player: Player, entity_type: EntityType):
    """Have we already maxed out on a certain entity type?"""
    if isinstance(entity_type, UnitType):
        ents = [u for u in player.units if u.type == entity_type]
    else:
        ents = [b for b in player.buildings if b.type == entity_type]
    return len(ents) < entity_type.limit


def find_builder_for_building(player: Player, building_type: BuildingType):
    """Does a player have a villager available to build a building?"""
    for u in player.units:
        if isinstance(u, Villager) and u.task is not VillagerTask.BUILDING:
            return u
    return None


def find_trainer_for_unit(player: Player, unit_type: UnitType):
    """Can a unit be trained?"""
    potential_trainers = [b for b in player.buildings if unit_type in b.type.trainable_units]
    for building in potential_trainers:
        if building.production_status is None:
            return building
        else:
            ps = building.production_status
            if ps.unit_type == unit_type and ps.batch_size < unit_type.max_training_batch_size:
                return building
    return None


def find_producer_for_entity(player: Player, entity_type: EntityType):
    """Are there enough resources and are we not at the limit for building a new unit or building?"""
    if not cost_satisfied(player, entity_type):
        return None
    if not not_at_limit(player, entity_type):
        return None
    if isinstance(entity_type, BuildingType):
        return find_builder_for_building(player, entity_type)
    elif isinstance(entity_type, UnitType):
        return find_trainer_for_unit(player, entity_type)
    return None
