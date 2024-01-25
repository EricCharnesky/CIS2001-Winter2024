from MazeSolver import MazeSolver
from NQueens import NQueens


# helper private function
def _fib(nth, current_nth, previous, current):
    if current_nth == nth:
        return current
    return _fib(nth, current_nth+1, current, previous+current)

def fib(nth):
    if nth <= 2:
        return 1
    return _fib(nth, 2, 1, 1)

def fib_iterative(nth):
    if nth <= 2:
        return 1
    current_nth = 2
    previous = 1
    current = 1
    while current_nth < nth:
        next = previous + current
        previous = current
        current = next
        current_nth += 1
    return current

def fib_slow(nth):
    if nth <= 2:
        return 1
    return fib_slow(nth-1) + fib_slow(nth-2)

for n in range(1, 51):
    print(f'fib nth: {n}: {fib(n)}')
    print(f'fib nth: {n}: {fib_iterative(n)}')

def count_down(n):
    if n <= 0:
        print("blastoff!")
    else:
        print(n)
        count_down(n-1)

#count_down(10)

maze = [
    ['S', 'X', ' ', ' ', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', ' ', ' ', 'X', ' '],
    [' ', 'X', ' ', 'X', ' '],
    [' ', 'X', ' ', ' ', 'E']
]

solver = MazeSolver(maze)
print(solver.solve())

eightQueens = NQueens(8)
eightQueens.solve()

