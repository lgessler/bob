import click

from bob.simulation.initialize import init_game_state


click.command(help="")
def main():
    game_state = init_game_state('dutch')
    player_state = game_state.player
    from pprint import pprint
    pprint(player_state.__dict__)


if __name__ == '__main__':
    main()