from typing import List

from bob.model.game import Game


class Action:
    def __repr__(self):
        return self.__class__.__name__ + "(" + str(self.__dict__) + ")"

    @staticmethod
    def get_actions(game: Game) -> List["Action"]:
        """Given a game state, return a list of actions of this type that are valid."""
        raise NotImplemented("get_actions must be implemented!")
