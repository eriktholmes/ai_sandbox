import random
import torch
from connect_four import ConnectFour


def play_random_game():
  """ A full game of Connect Four where both players select moves at random. """
    game = ConnectFour()
    while not game.is_over():
        game.make_move(random.choice(game.legal_moves()))
    return game.get_result()

def random_batch(num_games=100):
    """ Run a batch of random games and print win/draw statistics """
    results = torch.tensor([play_random_game() for _ in range(num_games)])
    one = (results == 1).sum().item()
    two = (results == -1).sum().item()
    draws = (results == 0).sum().item()
    print(f'Player One wins {one/num_games*100:.2f}% of the games')
    print(f'Player Two wins {two/num_games*100:.2f}% of the games')
    print(f'There were {draws} draws')

if __name__ == "__main__":
    random_batch(1000)
