# 348. Design Tic-Tac-Toe
# Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
#
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves are allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
# Implement the TicTacToe class:
#
# TicTacToe(int n) Initializes the object the size of the board n.
# int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move.
# Follow up:
# Could you do better than O(n2) per move() operation?
#
#
#
# Example 1:
#
# Input
# ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
# [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
# Output
# [null, 0, 0, 0, 0, 0, 0, 1]
#
# Explanation
# TicTacToe ticTacToe = new TicTacToe(3);
# Assume that player 1 is "X" and player 2 is "O" in the board.
# ticTacToe.move(0, 0, 1); // return 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
#
# ticTacToe.move(0, 2, 2); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
#
# ticTacToe.move(2, 2, 1); // return 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
#
# ticTacToe.move(1, 1, 2); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
#
# ticTacToe.move(2, 0, 1); // return 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
#
# ticTacToe.move(1, 0, 2); // return 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
#
# ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
#
#
# Constraints:
#
# 2 <= n <= 100
# player is 1 or 2.
# 1 <= row, col <= n
# (row, col) are unique for each different call to move.
# At most n2 calls will be made to move.

# 00  01  02
# 10  11  12
# 20  21  22

# 00  01
# 10  11


# Logic
# Create a n x n matrix using lists and initialize all values to 0
# Update value of location by player
# Create checker function which counts player val in 4 ways checker = [vertical, horizontal, diag1, diag2]
# If any of the checker list element is equal to n
# Given player is the winner
# Else return 0

class TicTacToe:
    def __init__(self, n):
        self.board = [[0 for i in range(0, n)] for i in range(0, n)]
        self.dimension = n

    def move(self, row, col, player):
        """
            Player {player} makes a move at ({row}, {col}).
            @param row The row of the board.
            @param col The column of the board.
            @param player The player, can be either 1 or 2.
            @return The current winning condition, can be either:
                    0: No one wins.
                    1: Player 1 wins.
                    2: Player 2 wins.
        """
        # Playing the move
        if self.board[row][col] == 0:
            self.board[row][col] = player

        # Approach 1 -- Works
        # [vertical, horizontal, diag1, diag2]
        self.checker = [0]*4

        for i, j in zip(range(0, self.dimension), range(self.dimension-1, -1, -1)):
            if self.board[row][i] == player:
                self.checker[0] += 1
            if self.board[i][col] == player:
                self.checker[1] += 1
            if self.board[i][i] == player:
                self.checker[2] += 1
            if self.board[i][j] == player:
                self.checker[3] += 1

        if any(elem == self.dimension for elem in self.checker):
            return player
        else:
            return 0

        # Approach 2 -- Time limit exceeded
        # # Check if won
        # # Vertical
        # if all(self.board[row][i] == player for i in range(0, self.dimension)):
        #     print("Player {} Won".format(player))
        #     return player
        #
        # # Horizontal
        # elif all(self.board[i][col] == player for i in range(0, self.dimension)):
        #     print("Player {} Won".format(player))
        #     return player
        #
        # # Diagonal 1
        # elif all(self.board[i][i] == player for i in range(0, self.dimension)):
        #     print("Player {} Won".format(player))
        #     return player
        #
        # # Diagonal 2
        # elif all(self.board[i][j] == player for i, j in zip( range(0, self.dimension), range(self.dimension-1, -1, -1) )):
        #     print("Player {} Won".format(player))
        #     return player
        #
        # else:
        #     return 0


if __name__ == "__main__":
    # Approach 1 Set
    ttt_obj = TicTacToe(n=2)
    ttt_obj.move(0, 0, 2)
    ttt_obj.move(0, 1, 1)
    ttt_obj.move(1, 1, 2)

    # Approach 2 Set
    # ttt_obj = TicTacToe(n=3)
    # ttt_obj.move(0, 0, 1)
    # ttt_obj.move(0, 2, 2)
    # ttt_obj.move(2, 2, 1)
    # ttt_obj.move(1, 1, 2)
    # ttt_obj.move(2, 0, 1)
    # ttt_obj.move(1, 0, 2)
    # ttt_obj.move(2, 1, 1)
