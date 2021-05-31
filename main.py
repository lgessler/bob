import click

from bob.simulation.actions import get_actions
from bob.simulation.initialize import init_game_state


click.command(help="")


def main():
    game_state = init_game_state("dutch")
    player_state = game_state.player
    player_state.food = 100.0
    player_state.coin = 100.0
    from pprint import pprint

    pprint(player_state.__dict__)

    print(get_actions(game_state))


if __name__ == "__main__":
    main()

