Maze Solver
This is a Python program for generating and solving mazes using the Turtle graphics library. The program creates a random maze and provides two solving algorithms: A* and Backtracking.

Table of Contents
Introduction
Features
How to Use
Solving Algorithms
Author
License
Introduction
This project generates a random maze and allows you to solve it using two different algorithms. It uses the Turtle graphics library to visualize the maze generation and solving process.

Features
Random maze generation with customizable size.
Maze solving using two different algorithms: A* and Backtracking.
Visual representation of the maze and solving process.
How to Use
Clone this repository to your local machine:

bash
Copy code
git clone <repository_url>
Install the required libraries:

bash
Copy code
pip install turtle
Run the maze_solver.py script:

bash
Copy code
python maze_solver.py
Use the GUI to select the solving algorithm (A* or Backtracking) and click the "Solve" button.

Watch as the program generates a random maze and solves it.

Solving Algorithms
A* Algorithm
The A* algorithm uses the Manhattan distance heuristic to find the shortest path from the start to the exit of the maze. It explores the maze by considering the tiles with the lowest heuristic values first.

Backtracking Algorithm
The Backtracking algorithm explores the maze by recursively searching for a path from the start to the exit. If it reaches a dead-end, it backtracks to the previous tile and continues exploring until it finds a path to the exit.

Author
This project was created by [Your Name].

License
This project is licensed under the MIT License. See the LICENSE file for details.

Enjoy exploring and solving mazes!
