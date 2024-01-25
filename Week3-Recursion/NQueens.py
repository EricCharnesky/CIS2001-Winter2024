class NQueens:

    OPEN = ' '
    QUEEN = 'Q'

    def __init__(self, n):
        self.board = []
        for row in range(n):
            self.board.append([])
            for column in range(n):
                self.board[row].append(' ')
        self._current_row = 0
        self._numer_of_solutions = 0

    def __str__(self):
        return "\n".join(str(row) for row in self.board)

    def _is_open_column(self, column_index):
        for row_index in range(self._current_row):
            if self.board[row_index][column_index] == NQueens.QUEEN:
                return False
        return True

    def _is_open_diagonal_back(self, column_index):
        current_row_index = self._current_row - 1
        current_column_index = column_index - 1

        while current_column_index >= 0 and current_row_index >= 0:
            if self.board[current_row_index][current_column_index] == NQueens.QUEEN:
                return False
            current_column_index -= 1
            current_row_index -= 1
        return True

    def _is_open_diagonal_forward(self, column_index):
        current_row_index = self._current_row - 1
        current_column_index = column_index + 1

        while current_column_index < len(self.board) and current_row_index >= 0:
            if self.board[current_row_index][current_column_index] == NQueens.QUEEN:
                return False
            current_column_index += 1
            current_row_index -= 1
        return True

    def _can_place(self, column_index):
        return self._is_open_column(column_index) \
            and self._is_open_diagonal_back(column_index) \
            and self._is_open_diagonal_forward(column_index)

    def solve(self):
        while self._current_row < len(self.board):
            for column_index in range(len(self.board)):
                if self._can_place(column_index):
                    self.board[self._current_row][column_index] = NQueens.QUEEN
                    self._current_row += 1
                    self.solve()
                    self._current_row -= 1
                    self.board[self._current_row][column_index] = NQueens.OPEN
            else:
                # after all n columns were tried, go back and undo
                return

        else:
            print(self)
            self._numer_of_solutions += 1
            print(f'solution # {self._numer_of_solutions}')
            print()