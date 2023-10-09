# Maze Solver

This Python program generates and solves mazes using the Turtle graphics library. It creates random mazes and provides two solving algorithms: A* and Backtracking.

## Features

- Random maze generation with customizable size.
- Maze solving using two different algorithms: A* and Backtracking.
- Visual representation of the maze and solving process.

## How to Use

 **Clone this repository** to your local machine:

   ```bash
   git clone <repository_url>
   pip install turtle
   python maze_solver.py
```
Use the GUI to select the solving algorithm (A* or Backtracking) and click the "Solve" button.  
Watch as the program generates a random maze and solves it.

## Solving Algorithms
**A\* Algorithm**  
The A* algorithm uses the Manhattan distance heuristic to find the shortest path from the start to the exit of the maze. It explores the maze by considering the tiles with the lowest heuristic values first.

**Backtracking Algorithm**  
The Backtracking algorithm explores the maze by recursively searching for a path from the start to the exit. If it reaches a dead-end, it backtracks to the previous tile and continues exploring until it finds a path to the exit.

