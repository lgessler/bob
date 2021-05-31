from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List


# Entity types--these are used to keep track of available entities and shared info about them
@dataclass(repr=False)
class EntityType:
    name: str
    build_time: float
    food_cost: float = 0.0
    wood_cost: float = 0.0
    coin_cost: float = 0.0
    xp_on_completion: float = 0.0
    limit: int = 10000

    def __repr__(self):
        s = self.name
        s += "("
        for k, v in sorted(self.__dict__.items(), key=lambda x: x[0]):
            if k in ["name", "trainable_units"]:
                continue
            if not v or v == getattr(self.__class__, k, None):
                continue
            s += f"{k}={v}"
            s += ", "
        if s[-1] != "(":
            s = s[:-2]
        s += ")"
        return s


@dataclass(repr=False)
class UnitType(EntityType):
    population_occupied: int = 0
    max_training_batch_size: int = 5


@dataclass(repr=False)
class BuildingType(EntityType):
    trainable_units: List[UnitType] = field(default_factory=list)
    population_supplied: int = 0
    xp_trickle: float = 0.0
    food_trickle: float = 0.0
    coin_trickle: float = 0.0
    wood_trickle: float = 0.0


# Entities--these are used to track the individual states of buildings
@dataclass(repr=False)
class Entity:
    type: EntityType

    def __repr__(self):
        s = self.type.name
        s += "("
        for k, v in sorted(self.__dict__.items(), key=lambda x: x[0]):
            if k in ["type"]:
                continue
            if not v or v == getattr(self.__class__, k, None):
                continue
            s += f"{k}={v}"
            s += ", "
        if s[-1] != "(":
            s = s[:-2]
        s += ")"
        return s


@dataclass(repr=False)
class Unit(Entity):
    type: UnitType


@dataclass
class ProductionStatus:
    unit_type: UnitType
    batch_size: int = 1
    elapsed: float = 0.0


@dataclass(repr=False)
class Building(Entity):
    type: BuildingType
    # between 0.0 and 1.0, 1.0 = fully constructed
    construction_status: float = 0.0
    production_status: ProductionStatus = None


# some special handling for villagers
class VillagerTask(Enum):
    IDLE = auto()
    HUNT = auto()
    COIN_MINE = auto()
    BERRIES = auto()
    WOOD = auto()
    FOOD_CRATE = auto()
    WOOD_CRATE = auto()
    COIN_CRATE = auto()
    BUILDING = auto()


@dataclass(repr=False)
class Villager(Unit):
    task: VillagerTask = VillagerTask.IDLE
    target_building: Building = None
