from typing import List

from bob.model.game import Game
from bob.simulation.actions.action import Action
from bob.simulation.actions.build import Build
from bob.simulation.actions.train import Train


def get_actions(game: Game) -> List[Action]:
    actions = []
    actions += Build.get_actions(game)
    actions += Train.get_actions(game)

    return actions


def choose_action(game: Game, actions: List[Action]):
    # TODO: NYI
    return actions[0]


def simulate_game(game: Game, time_delta: float):
    """Modifies game so that the game time is now game.time + time_delta"""
    # TODO: NYI
    return game


def find_milestone(game: Game, action: Action) -> Game:
    # NYI. Steps:
    # - Are we already at a milestone? If so, return the game state
    # - Otherwise, generate all possible milestones that are reachable from the current game state
    #   - You need a function that can e.g. generate milestones defined by how long it will be until
    #     a certain building is available to train units again, and measure how temporally distant
    #     that milestone is
    # - Take the milestone that is temporally closest
    #
    # Some milestone criteria:
    # - A building is not training anything and we have the resources to train sth from it
    # - A villager is idle (this needs a new subclass of Action too)
    # - We reach a resource amount that unlocks a certain tech or unit training
    # - We can age up
    #
    # Code organization: probably best to write a bunch of function-pairs, where one function
    # tests whether a game-state is a milestone according to a single criterion (e.g. "can train villager"),
    # and another function modifies a game-state so that the same kind of milestone is reached (e.g. by
    # letting the game clock tick until the town center, which can train villagers, is idle again).
    pass


# TODO: arguments for criteria? probably want some kind of config object
def search_loop(game: Game):
    for i in range(2):
        # Consider all possible actions
        actions = get_actions(game)

        # Choose one to execute
        best_action = choose_action(game, actions)

        # See next reachable milestones for this action
        game = find_milestone(game, best_action)

    print(game)
