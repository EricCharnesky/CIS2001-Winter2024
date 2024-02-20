class Checkers:

    WHITE_CHECKER = 'W'
    BLACK_CHECKER = 'B'
    BLANK = ' '

    def __init__(self, board):
        self.board = board
        self.max_jumps = 0
        self._current_jumps = 0

    def _try_jump(self, current_row_index, current_column_index, black_row_index, black_column_index, destination_row_index, destination_column_index):
        if 0 <= destination_row_index < len(self.board) \
                and 0 <= destination_column_index < len(self.board[destination_row_index]) \
                and self.board[destination_row_index][destination_column_index] == ' ' \
                and self.board[black_row_index][black_column_index] == self.BLACK_CHECKER:

            self.board[current_row_index][current_column_index] = self.BLANK
            self.board[black_row_index][black_column_index] = self.BLANK
            self.board[destination_row_index][destination_column_index] = self.WHITE_CHECKER
            self._current_jumps += 1
            if self._current_jumps > self.max_jumps:
                self.max_jumps = self._current_jumps
            self._get_max_jumps(destination_row_index, destination_column_index)
            self._current_jumps -= 1
            self.board[destination_row_index][destination_column_index] = self.BLANK
            self.board[black_row_index][black_column_index] = self.BLACK_CHECKER
            self.board[current_row_index][current_column_index] = self.WHITE_CHECKER

    def _get_max_jumps(self, row_index, column_index):
        jumps = ((-2, -2), (-2, 2), (2, 2), (2, -2))
        for jump in jumps:
            self._try_jump(row_index, column_index, row_index + ( jump[0]//2), column_index + (jump[1]//2), row_index+jump[0], column_index+jump[1] )

    def get_max_jumps(self):
        for row_index in range(len(self.board)):
            for column_index in range(len(self.board[row_index])):
                if self.board[row_index][column_index] == self.WHITE_CHECKER:
                    self._get_max_jumps(row_index, column_index)
        return self.max_jumps

board = [
    ['W', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'B', ' ', 'B', ' ', 'B', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' '],
    [' ', ' ', 'W', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

checkers = Checkers(board)
print(checkers.get_max_jumps())
