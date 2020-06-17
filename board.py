import copy
from typing import Tuple


class Board:
    def __init__(self):
        self.colors: list = [['' for x in range(4)] for y in range(4)]
        self.amounts = [[0 for x in range(4)] for y in range(4)]

        self.colors[0][0] = 'B'
        self.amounts[0][0] = 10
        self.colors[3][3] = 'W'
        self.amounts[3][3] = 10

    def update(self, x: int, y: int, c: str, v: int):
        """
        Update the game board given x, y, color and value
        """
        if 0 <= x < 4 and 0 <= y < 4:
            self.colors[x][y] = c
            self.amounts[x][y] = v

    def put_cell(self, x: int, y: int, c: str, v: int):
        """
        Update the game board given x, y, color and value

        :param x: x
        :param y: y
        :param c: color 'B' or 'W'
        :param v: value v > 0
        """
        if 0 <= x < 4 and 0 <= y < 4 and self.colors[x][y] in [c, ''] and v > 0:
            self.amounts[x][y] += v
            self.colors[x][y] = c

    def get_cell(self, x, y) -> Tuple[str, int]:
        """
        Return the color and amount (c, a)
        """
        if 0 <= x < 4 and 0 <= y < 4:
            return self.colors[x][y], self.amounts[x][y]

    def is_friendly(self, x: int, y: int, c: str):
        """
        Return if the cell is either empty or owned
        """
        return 0 <= x < 4 and 0 <= y < 4 and self.colors[x][y] in [c, '']

    def is_taken_by(self, x: int, y: int, c: str):
        """
        Return if the cell is taken by a color specified
        """
        return 0 <= x < 4 and 0 <= y < 4 and self.colors[x][y] == c

    def clone(self):
        """
        Return a new board that is a deep copy
        """
        return copy.deepcopy(self)

    def show(self):
        """
        Print the game board
        """
        print('------- ------- ------- -------')
        for y in range(4):
            row = ''
            for x in range(4):
                row += '{0} ({1})\t'.format(
                    self.amounts[x][y], self.colors[x][y])
            print(row)
            print('------- ------- ------- -------')
