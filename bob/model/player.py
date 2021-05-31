from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Dict

from bob.model.entities import BuildingType, Unit, Building


@dataclass
class Player:
    # Current state of food, wood, and coin
    food: float = 0.0
    wood: float = 0.0
    coin: float = 0.0

    # Rates
    base_xp_trickle_rate: float = 2.0
    base_gather_coin_rate: float = 0.60
    base_gather_wood_rate: float = 0.5
    base_gather_hunt_rate: float = 0.84
    base_gather_berry_rate: float = 0.67
    bonus_xp_trickle_rate: float = 0.0
    bonus_gather_coin_rate: float = 0.0
    bonus_gather_wood_rate: float = 0.0
    bonus_gather_hunt_rate: float = 0.0
    bonus_gather_berry_rate: float = 0.0

    # Crate resources lying on the ground
    food_in_crates: float = 0.0
    wood_in_crates: float = 0.0
    coin_in_crates: float = 0.0
    xp_in_crates: float = 0.0

    # Available building types
    building_types: List[BuildingType] = field(default_factory=list)

    # Building and unit states
    buildings: List[Building] = field(default_factory=list)
    units: List[Unit] = field(default_factory=list)

    # techs
    # tech_types: List[TechType] = field(default_factory=list)
    # techs: List[Tech] = field(default_factory=list)

    @property
    def max_pop(self):
        return sum(b.type.population_supplied for b in self.buildings)

    @property
    def pop(self):
        return sum(u.type.population_occupied for u in self.units)
