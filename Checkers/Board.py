import numpy as np

class Board:
    def __init__(self):
        self.board = np.array(
        [[0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0 ,1],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [2, 0, 2, 0, 2, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2],
         [2, 0, 2, 0, 2, 0, 2, 0]])

        self.board_size = 8

    def make_a_move(self, from_tile, to_tile, player):


    def check_if_legal(self, from_tile, to_tile, player):
        from_tile = np.asarray(from_tile)
        to_tile = np.asarray(to_tile)
        legal = True

        if player == 1:
            player_dir = 1
        elif player == 2:
            player_dir = -1
        else:
            legal = False
            print("Invalid player %d" player)

        if self.board[from_tile] != player:
            legal = False
            print("Illegal move by player %d. No legal piece at" % player, from_tile)
        if (0 < to_tile < self.board_size).any() or (to_tile > self.board_size).any():
            legal = False
            print("Illegal move by player %d. Moved out of board." % player)
        if self.board[to_tile] != 0:
            legal = False
            print("Illegal move by player %d. Moved onto other piece." % player)
        #if (from_tile - to_tile)



if __name__ == "__main__":
    TestBoard = Board()
    print(TestBoard.board)
