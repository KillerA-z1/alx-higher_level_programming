#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format:
[[row, col], [row, col], [row, col], [row, col]]
where `row` and `col` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    chessboard = []
    for _ in range(n):
        row = [' '] * n
        chessboard.append(row)
    return chessboard


def deepcopy_chessboard(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(deepcopy_chessboard, chessboard))
    return chessboard


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard)):
            if chessboard[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def mark_attacked_positions(chessboard, row, col):
    """Mark attacked positions on the chessboard.

    Mark all spots where non-attacking queens can no
    longer be placed as 'x'.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    n = len(chessboard)

    # Mark all forward positions
    c = col + 1
    while c < n:
        chessboard[row][c] = "x"
        c += 1

    # Mark all backward positions
    c = col - 1
    while c >= 0:
        chessboard[row][c] = "x"
        c -= 1

    # Mark all positions below
    r = row + 1
    while r < n:
        chessboard[r][col] = "x"
        r += 1

    # Mark all positions above
    r = row - 1
    while r >= 0:
        chessboard[r][col] = "x"
        r -= 1

    # Mark all positions diagonally down to the right
    r = row + 1
    c = col + 1
    while r < n and c < n:
        chessboard[r][c] = "x"
        r += 1
        c += 1

    # Mark all positions diagonally up to the left
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        chessboard[r][c] = "x"
        r -= 1
        c -= 1

    # Mark all positions diagonally up to the right
    r = row - 1
    c = col + 1
    while r >= 0 and c < n:
        chessboard[r][c] = "x"
        r -= 1
        c += 1

    # Mark all positions diagonally down to the left
    r = row + 1
    c = col - 1
    while r < n and c >= 0:
        chessboard[r][c] = "x"
        r += 1
        c -= 1


def solve_nqueens(n):
    chessboard = [[' ' for _ in range(n)] for _ in range(n)]
    stack = []
    solutions = []

    row = 0
    col = 0
    while True:
        if col == n:
            if row == 0:
                break
            row, col = stack.pop()
            chessboard[row][col] = ' '
            col += 1
            continue

        if is_valid_placement(chessboard, row, col):
            chessboard[row][col] = 'Q'
            stack.append((row, col))
            if row == n - 1:
                solutions.append(get_solution(chessboard))
                chessboard[row][col] = ' '
                col += 1
                continue
            row += 1
            col = 0
        else:
            col += 1

    return solutions


def is_valid_placement(chessboard, row, col):
    """Check if placing a queen at the given position is valid.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The row to check.
        col (int): The column to check.

    Returns:
        bool: True if the placement is valid, False otherwise.
    """
    n = len(chessboard)

    # Check same row
    for c in range(n):
        if chessboard[row][c] == "Q":
            return False

    # Check same column
    for r in range(n):
        if chessboard[r][col] == "Q":
            return False

    # Check upper-left diagonal
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        if chessboard[r][c] == "Q":
            return False
        r -= 1
        c -= 1

    # Check upper-right diagonal
    r = row - 1
    c = col + 1
    while r >= 0 and c < n:
        if chessboard[r][c] == "Q":
            return False
        r -= 1
        c += 1

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    solutions = solve_nqueens(n)

    for solution in solutions:
        print(solution)

    sys.exit(0)
