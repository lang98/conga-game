import random

from board import Board
from player import Player


class RandPlayer(Player):
    def __init__(self, c: str):
        Player.__init__(self, c)

    def make_next_move(self, board: Board) -> Board:
        all_moves = self.get_all_moves(board, self.player_color)
        return random.choice(all_moves)
