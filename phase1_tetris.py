"""
Phase 1 Tetris Demo (text-based)

This script is intentionally simple so non-technical readers can follow the logic.
It demonstrates the core Tetris loop:
1) Create a grid
2) Spawn a piece
3) Let it fall one step at a time
4) Lock it when it lands
5) Repeat until no new piece can spawn

What this version does NOT include (by design for Phase 1):
- no scoring
- no rotation
- no line clearing
- no graphical UI
"""

import random
from typing import List, Tuple

# Grid size suggested in Phase 1 requirements.
GRID_WIDTH = 10
GRID_HEIGHT = 20

# A cell is represented as (row_offset, col_offset) from the piece's top-left origin.
Cell = Tuple[int, int]

# Basic Tetromino layouts in fixed orientation (no rotation in Phase 1).
# Each list of cells describes where blocks exist for that shape.
SHAPES = {
    "I": [(0, 0), (0, 1), (0, 2), (0, 3)],
    "O": [(0, 0), (0, 1), (1, 0), (1, 1)],
    "T": [(0, 1), (1, 0), (1, 1), (1, 2)],
    "L": [(0, 0), (1, 0), (1, 1), (1, 2)],
    "J": [(0, 2), (1, 0), (1, 1), (1, 2)],
    "S": [(0, 1), (0, 2), (1, 0), (1, 1)],
    "Z": [(0, 0), (0, 1), (1, 1), (1, 2)],
}


def create_empty_grid(height: int, width: int) -> List[List[str]]:
    """Build a blank grid filled with '.' characters."""
    return [["." for _ in range(width)] for _ in range(height)]


def can_place(grid: List[List[str]], cells: List[Cell], row: int, col: int) -> bool:
    """Check whether a piece can be placed at (row, col) without collisions."""
    for r_offset, c_offset in cells:
        r = row + r_offset
        c = col + c_offset

        # Piece is not valid if it goes outside the board.
        if r < 0 or r >= GRID_HEIGHT or c < 0 or c >= GRID_WIDTH:
            return False

        # Piece is not valid if it hits a previously locked block.
        if grid[r][c] == "#":
            return False

    return True


def lock_piece(grid: List[List[str]], cells: List[Cell], row: int, col: int) -> None:
    """Convert the active piece into locked blocks on the grid."""
    for r_offset, c_offset in cells:
        r = row + r_offset
        c = col + c_offset
        grid[r][c] = "#"


def draw_grid(grid: List[List[str]], cells: List[Cell], row: int, col: int, shape_name: str) -> None:
    """Print the grid, overlaying the current falling piece as '@'."""
    # Copy so we can draw the active piece without changing the real grid.
    view = [line[:] for line in grid]

    for r_offset, c_offset in cells:
        r = row + r_offset
        c = col + c_offset
        if 0 <= r < GRID_HEIGHT and 0 <= c < GRID_WIDTH:
            view[r][c] = "@"

    print("\n" + "=" * 28)
    print(f"Current piece: {shape_name}")
    print("Commands: [Enter]=fall, a=left, d=right, s=down, q=quit")
    print("." " = empty, @ = falling piece, # = stacked block")
    print("=" * 28)
    for line in view:
        print(" ".join(line))


def shape_width(cells: List[Cell]) -> int:
    """Return the width of a shape, used for centering spawn position."""
    min_col = min(c for _, c in cells)
    max_col = max(c for _, c in cells)
    return max_col - min_col + 1


def choose_random_shape() -> Tuple[str, List[Cell]]:
    """Pick one random shape and return its name and cells."""
    name = random.choice(list(SHAPES.keys()))
    return name, SHAPES[name]


def run_game() -> None:
    """Run the main text-based Tetris loop for Phase 1."""
    grid = create_empty_grid(GRID_HEIGHT, GRID_WIDTH)

    print("Welcome to Phase 1 Tetris (text mode)!\n")

    while True:
        shape_name, cells = choose_random_shape()
        piece_row = 0
        piece_col = (GRID_WIDTH - shape_width(cells)) // 2

        # If a new piece cannot appear, the stack reached the top.
        if not can_place(grid, cells, piece_row, piece_col):
            print("\nGame over: no space to spawn a new piece.")
            break

        while True:
            draw_grid(grid, cells, piece_row, piece_col, shape_name)
            command = input("Next move: ").strip().lower()

            if command == "q":
                print("\nGame ended by player.")
                return

            # Horizontal movement is optional before each fall step.
            if command == "a" and can_place(grid, cells, piece_row, piece_col - 1):
                piece_col -= 1
            elif command == "d" and can_place(grid, cells, piece_row, piece_col + 1):
                piece_col += 1

            # 's' means manually nudge down by one row (still no real-time movement).
            if command == "s" and can_place(grid, cells, piece_row + 1, piece_col):
                piece_row += 1

            # Every loop, the piece attempts to fall by one step.
            if can_place(grid, cells, piece_row + 1, piece_col):
                piece_row += 1
            else:
                lock_piece(grid, cells, piece_row, piece_col)
                break

    print("\nFinal stacked grid:")
    for line in grid:
        print(" ".join(line))


if __name__ == "__main__":
    run_game()
