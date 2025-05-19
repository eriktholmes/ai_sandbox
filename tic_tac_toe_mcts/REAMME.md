# Tic Tac Toe

## Game environment ('tictactoe.py')
Fully functional tic tac toe game environment (though not overly pleasing (visually) to actually play) 


---

## Monte Carlo Tree Search 
We are using MCTS and UCB to simulate (informed) gameplay on the fly. We simulate games with two random players as well as one random and one MCTS informed player. The results illustrate the power of MCTS on small games. 
[Here is a nice introduction to MCTS](https://www.cs.swarthmore.edu/~mitchell/classes/cs63/f20/reading/mcts.html#:~:text=The%20basic%20MCTS%20algorithm%20is,down%20into%20the%20following%20steps.&text=Starting%20at%20root%20node%20R,leaf%20node%20L%20is%20reached.') is a description of the algorithm. We will use Monte Carlo Tree Search (MCTS) and Upper Confidence Bound (UCB) to help us select the optimal next move. 

---

### Part 1: node class
Each node in the MCTS stores:
- 'state': the current TicTacToe game (typically a cloned version for MCTS)
- 'move': the last move that resulted in this game state.
- 'parent': the previous node (i.e. the game state prior to move)
- 'child': a dictionary that stores a move that results in the child node
- 'visit count' and a 'win count': for UCB scores

---

### Part 2: Upper Confidence Bound
- First, visit **unvisted** nodes!
- Next, we define the **exploitation** (ratio of the child nodes wins/visits: like the weight assigned to a given child node)
- Finally, we define **exploration** (we set c = sqrt(2), but this can be tuned/altered)... **Try this!**
- Lastly, we return the result of UCB which assigns a value to a given child node, we loop over this during node selection to see which node to visit next in the MCTS.

------

### Part 3: Monte Carlo Tree Search! See the algorithm above for more details but here is a rough breakdown:
** We can specify number of simiulations at each step and the tunable UCB constant *c*. Then, the algorithm does the following steps:


#### 1: ```select```
Starting at the root node (i.e. the current game state) 'select()' will return the next node in the tree for simulation. 
- If not all children nodes have been explored then we return the current node, which will then be expanded
- If all children nodes have been visited and the game is not over
  - we calculate the UCB score for each child node
  - return the child node that has the highest UCB


#### 2: ```expand```
  - generate all legal moves given the current state of the game
  - if any unexplored moves exist we push the game one step forward to this new child node
  - otherwise we return the current node



#### 3: ```simulate``` 
Simulate gameplay from the expanded state:
- clone the game
- simulate a random game from this last move
- return the winner (and the number of moves played... we don't use this now but thought it might be useful)


 
#### 4: ```backpropogate```
we travel back up the tree from our simulated game node with the result of the simulation. 
- starting at our *siulation* node we travel back to the *root*. As we go we
  - increase node.visit by 1
  - increase node.win by 1 IF the player to move to this node won the simulation (i.e. -node.state.current_player)



#### 5: ```choose_move```
Here we choose the actual move that the MCTS 'agent' will play
- Create a root node, i.e. clone of the current game state
- for each simulation (parameter set in MCTS) we:
  - select the next move via UCB 
  - expland the tree from the resulting game state
  - simulate a full game from this node
  - back propogate the result
- After all simulations we return the child node that saw highest number of visits

---

## What comes next?

- Add simulation results for MCTS player vs random and random vs random
- Experiment with different values of 'c'
- Apply MCTS to connect four (also, build connect four game)

---

## Why?

This project was suggested to me as a learning tool. Well, this is a baby step towards the actual project and ultimately, my broader goal of learning AI/ML through projects... next is connect four and maybe more complex turn based games where this brute force search for moves is not efficient. As the reader can likely deduce, we are starting with the basics and building towards 'alphazero'-style systems. 
