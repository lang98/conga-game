from typing import List, Tuple

from board import Board
from player import Player


class Agent(Player):
    def __init__(self, c: str, ab_pruning: bool = True):
        Player.__init__(self, c)
        self.ab_pruning = ab_pruning

    def make_next_move(self, board: Board) -> Board:
        if self.ab_pruning:
            evaluation, next_board = self.__mini_max(board, depth=3, is_max=True, states=[])
        else:
            evaluation, next_board = \
                self.__mini_max_ab(board, depth=3, is_max=True, alpha=-9999, beta=9999, states=[])
        return next_board

    def __mini_max(self, board: Board, depth: int, is_max: bool, states: List[Board]) -> Tuple[int, Board]:
        """
        Use the 'minimax' algorithm to find the best next move. Also directly return the best move if
        the next move can directly win the game.

        :param board: to perform the 'minimax' algorithm on
        :param depth: recursively decrement
        :param is_max: recursively inverse
        :param states: recursively keep track of the path
        :return: (utility, next_move)
        """
        if depth == 0:
            return self.__moves_available(board), states[0]
        all_moves = self.get_all_moves(board, self.player_color)

        if self.get_num_of_moves(board, self.opponent_color) == 0:
            return 9999, states[0]

        func = max if is_max else min
        return func([self.__mini_max(m, depth - 1, not is_max, states + [m]) for m in all_moves], key=lambda x: x[0])

    def __mini_max_ab(self,
                      board: Board,
                      depth: int,
                      is_max: bool,
                      alpha: int,
                      beta: int,
                      states: List[Board]
                      ) -> Tuple[int, Board]:
        """
        Use alpha-beta pruning to speed up minimax

        :param board: to perform the 'minimax' algorithm on
        :param depth: recursively decrement
        :param is_max: recursively inverse
        :param alpha: a
        :param beta: b
        :param states: recursively keep track of the path
        :return: (utility, next_move)
        """
        if depth == 0:
            return self.__moves_available(board), states[0]
        if self.get_num_of_moves(board, self.opponent_color) == 0:
            return 9999, states[0]
        all_moves = self.get_all_moves(board, self.player_color)

        if is_max:
            best = (-9999, board)
            for move in all_moves:
                next_state = self.__mini_max_ab(move, depth - 1, False, alpha, beta, states + [move])
                best = max(best, next_state, key=lambda x: x[0])
                alpha = max(alpha, best[0])
                if beta <= alpha:
                    break
            return best
        else:
            best = (9999, board)
            for move in all_moves:
                next_state = self.__mini_max_ab(move, depth - 1, True, alpha, beta, states + [move])
                best = min(best, next_state, key=lambda x: x[0])
                beta = min(beta, best[0])
                if beta <= alpha:
                    break
            return best

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
