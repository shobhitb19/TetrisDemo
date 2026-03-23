# Phase 1 & 2 – Unified Instructions

## Goal
Create a simple, playable version of Tetris that demonstrates the core mechanics and essential rules, making the game feel real and trustworthy.

## Scope
- No graphics or animations (text-based logic)
- No real-time input initially; add basic keyboard controls (left, right, rotate, drop) for interaction
- No UI beyond the game grid

## Functional Requirements
- Represent a game grid (e.g. 10x20)
- Generate and support multiple Tetromino shapes
- Allow shapes to "fall" step by step
- Detect when a shape hits the bottom or other blocks
- Stack shapes on the grid
- Allow rotation of shapes
- Detect filled horizontal lines and clear completed lines
- Shift remaining blocks downward after line clear

## System Behaviour
- End game when blocks reach the top
- Maintain a clear game loop

## Constraints
- Keep logic simple and readable
- Avoid performance optimisations

## Non-Goals
- No scoring
- No advanced UI

## Audience
Non-technical users. Code must be explained in plain English.

## Success Criteria
- The concept of Tetris is recognisable
- Logic is readable and commented
- Game loop and rules are clear
- Game behaves as expected with no obvious rule-breaking
- Players trust the system
