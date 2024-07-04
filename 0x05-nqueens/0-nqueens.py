#!/usr/bin/env python3
import sys

"nqueens algorithm"


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]. This function
    is called when "col" queens are already placed in columns from 0 to col -1.
    So we need to check only left side for attacking queens"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    """Utilize backtracking to find all solutions"""
    if col >= len(board):
        solutions.append(board_to_positions(board))
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0


def board_to_positions(board):
    """Convert board to a list of positions"""
    positions = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                positions.append([i, j])
    return positions


def solve_nqueens(n):
    """Solve the N queens problem and return all solutions"""
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
