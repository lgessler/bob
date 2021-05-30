from typing import List

from bob.model.game import Game
from bob.model.player import Player
import bob.model.entities as E


def init_dutch_player_state() -> Player:
    # unit types
    villager_type = E.UnitType(
        "villager",
        build_time=25.0,
        coin_cost=100.0,
        xp_on_completion=10.0,
        population_occupied=1,
        max_training_batch_size=1,
        limit=50
    )
    envoy_type = E.UnitType(
        "envoy",
        build_time=15.0,
        food_cost=50.0,
        xp_on_completion=5.0,
        population_occupied=1,
        limit=5
    )

    # building types
    tc_type = E.BuildingType(
        "town_center",
        build_time=120.0,
        wood_cost=500.0,
        xp_on_completion=100.0,
        trainable_units=[villager_type, envoy_type],
        population_supplied=10,
        limit=1
    )
    bank_type = E.BuildingType(
        "bank",
        build_time=30.0,
        wood_cost=350.0,
        food_cost=350.0,
        xp_on_completion=140.0,
        coin_trickle=2.75,
        limit=5
    )
    house_type = E.BuildingType(
        "house",
        build_time=10.0,
        wood_cost=100.0,
        xp_on_completion=20.0,
    )
    building_types = [tc_type, bank_type, house_type]

    # units and buildings
    tc = E.Building(type=tc_type)
    units: List[E.Unit] = [E.Villager(villager_type) for _ in range(6)]
    units.append(E.Unit(envoy_type))

    player_state = Player(
        food_in_crates=100.0,
        wood_in_crates=200.0,
        coin_in_crates=300.0,
        building_types=building_types,
        buildings=[tc],
        units=units
    )
    # dutch have 20% coin gather bonus
    player_state.bonus_gather_coin_rate += 0.2 * player_state.base_gather_coin_rate

    return player_state


def init_player_state(civ_name: str) -> Player:
    if civ_name == 'dutch':
        return init_dutch_player_state()
    else:
        raise Exception(f"Unsupported civ: {civ_name}")


def init_game_state(civ_name: str) -> Game:
    game_state = Game(
        player=init_player_state(civ_name)
    )
    return game_state
