#!/usr/bin/python3
"""This module contains a program that solves the N queens problem."""


import sys


def is_integer(value):
    """Check if a value can be converted to an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def print_usage_and_exit():
    """Print usage information and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_error_and_exit(message):
    """Print an error message and exit with status 1."""
    print(message)
    sys.exit(1)


def generate_board_with_column(board=[]):
    """Add a column of zeroes to the right of the board."""
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def place_queen(board, row, col):
    """Place a queen at the specified coordinates in the board."""
    board[row][col] = 1


def is_queen_placement_safe(board, row, col):
    """Check if placing a new queen at given coordinates is safe."""
    x, y = row, col

    for i in range(1, N):
        if (y - i) >= 0:
            # Check up-left diagonal
            if (x - i) >= 0 and board[x - i][y - i]:
                return False
            # Check left
            if board[x][y - i]:
                return False
            # Check down-left diagonal
            if (x + i) < N and board[x + i][y - i]:
                return False
    return True


def format_queen_coordinates(candidate_boards):
    """Convert board into a series of row/column indices for each queen."""
    formatted_queens = []
    for x, candidate in enumerate(candidate_boards):
        formatted_queens.append([])
        for i, row in enumerate(candidate):
            formatted_queens[x].append([])
            for j, col in enumerate(row):
                if col:
                    formatted_queens[x][i].extend([i, j])
    return formatted_queens


# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print_usage_and_exit()

# Extract and validate the input N from the command-line argument
input_n = sys.argv[1]
if not is_integer(input_n):
    print_error_and_exit("N must be a number")
N = int(input_n)
if N < 4:
    print_error_and_exit("N must be at least 4")

# Initialize candidate_boards list with the first column of 0s
candidate_boards = [generate_board_with_column()]

# Proceed column by column, testing the rightmost
for col in range(N):
    """Start a new generation of the candidate_boards
    list for every round of testing"""
    new_candidates = []
    # Test each candidate from the previous round at the current column
    for current_board in candidate_boards:
        # For every row in that candidate's rightmost column
        for row in range(N):
            # Check if placing a queen at those coordinates is safe
            if is_queen_placement_safe(current_board, row, col):
                # Create a "child" (copy) of that candidate
                new_board = [line[:] for line in current_board]
                # Place a queen in that position
                place_queen(new_board, row, col)
                # Add a new column of 0s on the right for the next round
                if col < N - 1:
                    generate_board_with_column(new_board)
                # Add that new candidate to this round's list of successes
                new_candidates.append(new_board)
    # Discard the "parent" candidates when finished with the round
    candidate_boards = new_candidates

# Format results to match assignment output
for queen_coordinates in format_queen_coordinates(candidate_boards):
    print(queen_coordinates)
