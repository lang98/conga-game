from agent import Agent
from board import Board
from randplayer import RandPlayer


class Game:
    def __init__(self):
        pass

    def play(self):
        turn = 0
        b = Board()
        agent = Agent('B', False)
        rand_player = RandPlayer('W')
        rounds = 0

        while agent.get_num_of_moves(b, 'B'):
            rounds += 1
            print(rounds)
            b = agent.make_next_move(b)
            print('agent moves')
            b.show()
            if not rand_player.get_num_of_moves(b, 'W'):
                break
            b = rand_player.make_next_move(b)
            print('rand moves')
            b.show()
        b.show()


game = Game()
game.play()
