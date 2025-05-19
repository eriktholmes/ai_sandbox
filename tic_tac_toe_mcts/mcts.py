import numpy as np
import random



''' 
-------------------------------------
Node class for Monte Carlo Tree setup 
-------------------------------------
'''
class Node():
    def __init__(self, game_state, parent=None, move=None):
        self.state = game_state
        self.parent = parent
        self.move = move
        self.children = {}
        self.visits = 0
        self.wins = 0


'''
---------------------------------------------------
Upper confidence bound function 
  - for informed next node selection
---------------------------------------------------
'''
def UCB(parent, child, c=np.sqrt(2)):
    if child.visits == 0:
        return float('inf')
    exploitation = child.wins / child.visits
    exploration = c * np.sqrt(np.log(parent.visits) / child.visits)
    return exploitation + exploration







"""
----------------------------------
Full Monte Carlo Tree Search class
----------------------------------
"""

class MCTS:
    def __init__(self, simulations=20, c=np.sqrt(2)):
        self.simulations = simulations
        self.c = c

    
    def select(self, node, max_depth=9):
        depth = 0
        
        while len(node.children) == len(node.state.legal_moves()) and not node.state.is_over():
            best_score = float('-inf')
            best_move = None
            if depth > max_depth:
                break
            for move, child in node.children.items():
                score = UCB(node, child, self.c)
                if score > best_score:
                    best_score = score
                    best_move = child
            if best_move == None:
                break
            node = best_move
            depth += 1
        return node


    def expand(self, node):
        moves = node.state.legal_moves()
        for move in moves:
            if move not in node.children:
                new_game = node.state.clone()
                new_game.make_move(move)
                new_node = Node(new_game, parent=node, move=move)
                node.children[move] = new_node
                return new_node 
        return node
        

    def simulate(self, node):
        game = node.state.clone()
        moves = 0
        while not game.is_over():
            move = random.choice(game.legal_moves())
            game.make_move(move)
            moves += 1
        return game.get_winner(), moves

    
    def backpropagate(self, node, result):
        while node is not None:
            node.visits += 1
            last_player = -node.state.current_player
            if result == last_player:
                node.wins += 1
            node = node.parent


    def choose_move(self, game):
        root = Node(game.clone())
    
        for _ in range(self.simulations):
            leaf = self.select(root)
            child = self.expand(leaf)
            result, _ = self.simulate(child)
            self.backpropagate(child, result)
    
        best_child = max(root.children.values(), key=lambda child: child.visits)
        return best_child.move
