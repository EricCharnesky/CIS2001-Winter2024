class Knights_Tour:

    def __init__(self):
        self.current_move = 1
        self.board = []
        for row in range(8):
            self.board.append([])
            for column in range(8):
                self.board[row].append(' ')

    def solve(self, row, column):
        # mark
        self.board[row][column] = str(self.current_move)

        if self.current_move == 64:
            return True

        self.current_move += 1

        current_position = Position(self.board, row, column)
        next_moves = []
        for move in Position.POSSIBLE_MOVES:
            if current_position.can_move_to(row+move[0], column+move[1]):
                next_moves.append(Position(self.board, row+move[0], column+move[1]))
        next_moves.sort()
        for move in next_moves:
            if self.solve(move.row, move.column):
                return True

        self.current_move -= 1
        self.board[row][column] = ' '
        return False

    def __str__(self):
        return "\n".join(str(row) for row in self.board)



class Position:

    POSSIBLE_MOVES = ((2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1))

    def __init__(self, knights_tour_board, row, column):
        self.knights_tour_board = knights_tour_board
        self.row = row
        self.column = column


    def valid_moves(self):
        moves = 0
        for move in self.POSSIBLE_MOVES:
            if self.can_move_to(self.row + move[0], self.column + move[1]):
                moves += 1
        return moves

    def can_move_to(self, row, column):
        return 0 <= row < len(self.knights_tour_board) and \
            0 <= column < len(self.knights_tour_board) and \
            self.knights_tour_board[row][column] == ' '

    def __lt__(self, other):
        return self.valid_moves() < other.valid_moves()

    def __gt__(self, other):
        return self.valid_moves() > other.valid_moves()

    def __eq__(self, other):
        return self.valid_moves() == other.valid_moves()


tour = Knights_Tour()
tour.solve(3,3)
print(tour)
