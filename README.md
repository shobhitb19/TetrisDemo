# Tetris Demo (Phase 1)

This repository contains a text-based Tetris prototype that demonstrates the core game loop in a simple, readable way.

## What this version includes

- 10x20 game grid
- Random spawning of standard tetromino shapes (`I`, `O`, `T`, `L`, `J`, `S`, `Z`)
- Piece movement (left, right, and manual down)
- Automatic one-step fall each turn
- Piece locking when it can no longer fall
- Game-over detection when a new piece cannot spawn

## What this version intentionally does not include

- Rotation
- Line clearing
- Scoring
- Graphical interface

## Requirements

- Python 3.9+

## Run the game

```bash
python3 phase1_tetris.py
```

## Controls

- `Enter`: continue (piece falls one step)
- `a`: move piece left (if possible)
- `d`: move piece right (if possible)
- `s`: move piece down one extra step (if possible)
- `q`: quit game

## Sample gameplay

```text
$ python3 phase1_tetris.py
Welcome to Phase 1 Tetris (text mode)!

============================
Current piece: T
Commands: [Enter]=fall, a=left, d=right, s=down, q=quit
. = empty, @ = falling piece, # = stacked block
============================
. . . . @ . . . . .
. . . @ @ @ . . . .
. . . . . . . . . .
... (rows omitted) ...

Next move: d

============================
Current piece: T
...piece shifts right and falls one row...

Next move:
...piece falls one row...

Next move: s
...piece nudges down and then falls again...

Next move: q

Game ended by player.
```

## Grid symbols

- `.` empty cell
- `@` currently falling piece
- `#` locked/stacked blocks

## Project file

- `phase1_tetris.py`: full Phase 1 text-mode implementation