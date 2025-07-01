import random
from abc import ABC, abstractmethod
from azc4.game import ConnectFour

class Player(ABC):

    @abstractmethod
    def pick_move(self, board):
        pass


## -------------------- ##
##     Random Player    ##
## -------------------- ##

class RandomPlayer(Player):
    
    def pick_move(self, game: ConnectFour) -> int:
        return random.choice(game.legal_moves())


## -------------------- ##
##     Greedy Player    ##
## -------------------- ##

class GreedyPlayer(Player):

    def pick_move(self, game: ConnectFour) -> int:
        me, opp = game.current_player, -game.current_player
        for move in game.legal_moves():
            cloned_game = game.clone()
            cloned_game.make_move(move)
            if cloned_game.get_winner() == me or cloned_game.get_winner() == opp:
                return move

        if 3 in game.legal_moves():
            return 3

        else:
            return game.legal_moves()[0]
