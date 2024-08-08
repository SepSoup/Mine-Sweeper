# Game Mechanics and Logic of my version of Minesweeper

Welcome to **My Minesweeper**, a Python-based implementation of the classic Minesweeper game using Tkinter for the GUI Written based on the principals of object oriented programming.

## Table of Contents

- [Gameplay Overview](#gameplay-overview)
- [Game Components](#game-components)
  - [Grid and Cells](#grid-and-cells)
  - [Mines and Safe Cells](#mines-and-safe-cells)
  - [Lives System](#lives-system)
  - [Cell Revealing Logic](#cell-revealing-logic)
  - [Marking Cells](#marking-cells)
- [Game Logic](#game-logic)
  - [Initializing the Game](#initializing-the-game)
  - [Placing Mines](#placing-mines)
  - [Handling Clicks](#handling-clicks)
  - [Recursive Reveal](#recursive-reveal)
  - [Winning and Losing Conditions](#winning-and-losing-conditions)
- [Code Structure and Flow](#code-structure-and-flow)

## Gameplay Overview

this is a strategy puzzle game where the player aims to clear a grid of cells without triggering hidden mines. The game presents a rectangular grid with a mixture of safe cells and mines. The player interacts with the grid by left-clicking to reveal cells and right-clicking to mark potential mines. The goal is to reveal all safe cells while avoiding mines.


<img src="https://github.com/SepSoup/Mine-Sweeper/blob/master/static/Maingame.png" alt="Game Logic" width="400"/>


## Game Components

### Grid and Cells

- **Grid:** The grid is the main playing field, consisting of a rectangular array of cells. The size of the grid (number of rows and columns) can be adjusted in the `settings.py` file.
- **Cells:** Each cell on the grid can either be a safe cell or a mine. The state of a cell can be hidden, revealed, or marked by the player.

### Mines and Safe Cells

- **Mines:** These are the hidden dangers within the grid. If a player clicks on a mine, they lose a life.
- **Safe Cells:** These cells do not contain mines. When revealed, they either show a number indicating how many adjacent cells contain mines, or they automatically reveal surrounding cells if no adjacent mines are present.


<img src="https://github.com/SepSoup/Mine-Sweeper/blob/master/static/cells.png" alt="Game Logic" width="400"/>


### Lives System

- The game features a **lives system** where players start with a set number of lives, defined in `settings.py`.
- **Losing a life:** When the player clicks on a cell containing a mine, they lose one life.
- **Game Over:** The game ends if the player runs out of lives and clicks on a mine.

### Cell Revealing Logic

- When a player clicks on a safe cell, the game reveals that cell and shows a number representing how many adjacent cells (horizontally, vertically, and diagonally) contain mines.
- If the revealed cell is surrounded by zero mines, the game automatically reveals all adjacent safe cells recursively.

### Marking Cells

- **Right-clicking** on a cell allows the player to mark it as a potential mine. This helps in strategizing and avoiding mines while clearing the grid.
- **Unmarking:** Right-clicking again on a marked cell removes the mark, returning the cell to its hidden state.

## Game Logic

### Initializing the Game

When the game starts, the following steps occur:

1. **Grid Setup:** The grid is initialized with a set number of cells, defined in `settings.py`.
2. **Mine Placement:** Mines are randomly placed within the grid. The number of mines is also configurable.
3. **UI Setup:** The user interface, including frames and labels, is created to display the grid, lives, and remaining cells.

### Placing Mines

The mines are placed randomly across the grid using the `random.sample()` function. This function selects a unique set of cells to contain mines without overlap.

### Handling Clicks

- **Left Click:** When the player left-clicks a cell:
  - If it's a mine, the player loses a life, and the mine is revealed.
  - If it's a safe cell, the number of surrounding mines is displayed, or the cell is revealed along with adjacent safe cells if no surrounding mines exist.

- **Right Click:** This marks the cell as a potential mine. Marked cells help players avoid clicking on mines accidentally.

### Recursive Reveal

- If a safe cell with zero surrounding mines is revealed, the game automatically reveals all surrounding cells. This process is recursive, meaning it continues until all cells adjacent to cells with mines are revealed.
- This logic is handled in the `show_cell()` method within the `Cell` class.

### Winning and Losing Conditions

- **Winning:** The player wins when all non-mine cells are revealed.
- **Losing:** The game is lost if the player clicks on a mine when they have no remaining lives.

## Code Structure and Flow

1. **`main.py`:** This is the entry point of the game. It sets up the Tkinter window, frames, and initializes the game grid.
2. **`cell.py`:** Contains the `Cell` class, which handles the logic for each individual cell in the grid. This includes revealing cells, checking for surrounding mines, handling clicks, and more.
3. **`settings.py`:** Holds configurable settings such as grid dimensions, number of mines, cell size, and initial lives.
4. **`utility.py`:** Contains utility functions such as calculating percentages for UI element placement and other helper functions.
5. **Game Loop:** The game loop is managed by Tkinter's `mainloop()` method, which keeps the window responsive and processes user input (clicks) in real-time.

---

This explanation should provide a clear understanding of how the game operates both from a player's perspective and from the perspective of the underlying code logic. The combination of a user-friendly interface and robust logic ensures a challenging and enjoyable gameplay experience.
