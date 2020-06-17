from typing import List, Tuple

from board import Board
from player import Player


class Agent(Player):
    def __init__(self, c: str, eval: int):
        Player.__init__(self, c)
        self.prev = ([0, 0], [0, 0])
        self.eval = eval

    def make_next_move(self, board: Board) -> Board:
        evaluation, next_board = self.__mini_max(board, depth=3, is_max=True, states=[])
        return next_board

    def __mini_max(self, board: Board, depth: int, is_max: bool, states: List[Board]) -> Tuple[int, Board]:
        if depth == 0:
            return self.__moves_available(board), states[0]
        all_moves = self.get_all_moves(board, self.player_color)

        if self.get_num_of_moves(board, self.opponent_color) == 0:
            return 9999, states[0]

        func = max if is_max else min
        return func([self.__mini_max(m, depth - 1, not is_max, states + [m]) for m in all_moves], key=lambda x: x[0])

    def __moves_available(self, board: Board):
        """
        Evaluation function 1
        Evaluate the current board with number of moves

        :param board: for a given board
        :return: number of moves of player - number of moves of opponent
        """
        player_moves = self.get_num_of_moves(board, self.player_color)
        opponent_moves = self.get_num_of_moves(board, self.opponent_color)
        # print(len(player_moves), len(opponent_moves))

        return player_moves - opponent_moves * 3
