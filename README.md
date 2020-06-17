# Conga
Used the `minimax` algorithm with `alpha-beta pruning` to play the game of Conga against a random computer

## Game Rule
The game of Conga was developed by Matin Franke, and published by “Das Spiel 
Hamburg” in 1998. It is a two-player game played on a square 4X4 board, as shown below:

                         _______ _______ _______ _______
                        |       |       |       |       |
                        | (1,4) | (2,4) | (3,4) | (4,4) |
                        |_______|_______|_______|_______|
                        |       |       |       |       |
                        | (1,3) | (2,4) | (3,3) | (4,3) |
                        |_______|_______|_______|_______|
                        |       |       |       |       |
                        | (1,2) | (2,4) | (3,2) | (4,2) |
                        |_______|_______|_______|_______|
                        |       |       |       |       |
                        | (1,1) | (2,1) | (3,1) | (4,1) |
                        |_______|_______|_______|_______|


Initially, Player 1 has ten black stones in (1,4) and Player 2 has ten white stones in (4,1).

The players alternate turns. On each turn, a player chooses a square with some of his 
stones in it, and picks a direction to move them, either horizontally, vertically or 
diagonally. The move is done by removing the stones from the square and placing one 
stone in the following square, two in the next one, and the others into the last one. The 
stones can only be moved in consecutive squares that are not occupied by the opponent; 
if a direction has less than three squares not occupied by the opponent in a row, then all 
remaining stones are placed in the last empty square. If a square has no neighbouring 
squares that are not occupied by the opponent, then the stones in that square cannot be 
moved.

You can move stones from a square to a (series of) neighbouring square(s), provided the 
squares you are moving to are not occupied by the opponent. It makes no difference if the 
squares are free or occupied by yourself. You do not need any of the squares you are 
moving to be free; they could all already be occupied by your other stones. The only 
distinction is between squares that are occupied by the opponent (which block you) and squares that are not occupied by the opponent (which you can move to). 

The goal of the game is to block the opponent, so that they have no legal moves. In other 
words, all of the opponents’ stones must be trapped in squares that are all surrounded by 
the player’s stones.
