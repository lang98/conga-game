from abc import abstractmethod, ABC
from typing import List, Tuple, Optional

from board import Board


class Player(ABC):
    def __init__(self, c: str):
        self.player_color = c
        self.opponent_color = 'B' if c == 'W' else 'W'
        self.moves = [
            (1, 0), (-1, 0), (0, -1), (0, 1),
            (1, -1), (1, 1), (-1, -1), (-1, 1)
        ]

    @abstractmethod
    def make_next_move(self, board: Board) -> Board:
        """
        A generic method for the player to make a move, to be implemented by subclasses

        :param board: given a board
        :return: a new board after the move has been made
        """
        pass

    def get_all_moves(self, board: Board, for_player: str) -> List[Board]:
        """
        Generate all the moves available for the current player in the current level

        :return: a list of boards each representing the next game state
        """
        boards: List[Board] = []
        for y in range(4):
            for x in range(4):
                if board.is_taken_by(x, y, for_player):
                    for (dx, dy) in self.moves:
                        move = self.make_move(board, x, y, (dx, dy))
                        if move:
                            boards.append(move)
        return boards

    def get_num_of_moves(self, board: Board, for_player: str) -> int:
        """
        Get number of moves available to a player in a given board. It is faster than 'get_all_moves'

        :return: a list of boards each representing the next game state
        """
        count = 0
        for y in range(4):
            for x in range(4):
                if board.is_taken_by(x, y, for_player):
                    for (dx, dy) in self.moves:
                        if board.is_friendly(x + dx, y + dy, for_player):
                            count += 1
        return count

    def make_move(self, board: Board, x: int, y: int, direction: Tuple[int, int]) -> Optional[Board]:
        """
        Generate a new board object given the x, y and direction. This also ensures that the game rule of having
        1, 2, ... stones in the target direction is enforced even if there is only 1 or 2 cells in the direction.
        If that direction cannot be moved to, None will be returned.

        :param board: current board
        :param x: x of the cell to move
        :param y: y of the cell to move
        :param direction: (dx, dy) -1 <= dx, dy <= 1
        :return: A new Board object which shows the next move, None if cannot be moved to
        """
        new_board = board.clone()
        dx, dy = direction
        start_color, start_amount = new_board.get_cell(x, y)

        x_cur, y_cur = x + dx, y + dy
        amount, amount_count = start_amount, 1
        has_moved = False
        while new_board.is_friendly(x_cur, y_cur, self.player_color) and amount > 0:
            new_board.put_cell(x_cur, y_cur, self.player_color, min(amount_count, amount))
            amount -= amount_count
            if amount_count == 1:
                amount_count = 2
            else:
                amount_count = amount
            x_cur += dx
            y_cur += dy
            has_moved = True
        else:
            if x_cur == x + dx and y_cur == y + dy:  # can't move
                return None
            if amount > 0:  # 1, remaining
                new_board.put_cell(x_cur - dx, y_cur - dy, self.player_color, amount)

        if has_moved:  # movable
            new_board.update(x, y, '', 0)

        return new_board
