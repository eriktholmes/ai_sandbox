import random
from connect_four import ConnectFour


def greedy_move(game):
    """Greedy gameplay: aka player looks only for winning moves or blocks, otherwise proceeds with random play"""
    
    # Look for winning move
    for col in game.legal_moves():
        sim = game.clone()
        player_one = sim.current_player
        sim.make_move(col)
        if sim.get_winner() == player_one:
            return col

    # Try to block
    for col in game.legal_moves():
        sim = game.clone()
        player_two = -1*sim.current_player
        sim.current_player *= -1 
        sim.make_move(col)
        if sim.get_winner() == player_two:
            return col

    # Otherwise, return a random choice
    return random.choice(game.legal_moves())
        




def greedy_vs_random(num_simulations):
    """ Simulate a batch of games between the 'Greedy' player (Player 1) and Random player (Player 2)"""
    results = {0:0, 1:0, -1:0}
    for _ in range(num_simulations):
        game = ConnectFour()
        while not game.is_over():
            if game.current_player == 1:
                game.make_move(greedy_move(game))
            else:
                game.make_move(random.choice(game.legal_moves()))
        results[game.get_result()] += 1
        
    print(f"Greedy wins: {results[1]}")
    print(f"Random wins: {results[-1]}")
    print(f"Draws: {results[0]}")
    return results
