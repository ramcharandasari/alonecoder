import random
import os
from collections import deque

# ANSI color codes (same as in your code)
# ...

# Maze class (unchanged)

# Dijkstra's pathfinding algorithm
def find_path_dijkstra(maze, start, end):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path + [(x, y)]

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (x + dx, y + dy)

            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == OPEN_SPACE:
                queue.append((neighbor, path + [(x, y)]))

    return None

# Main function
def main():
    print("Welcome to the Terminal-Based Maze Solver!")

    while True:
        size = int(input("Enter the size of the maze (n x n): "))
        wall_percentage = 0.25  # Adjust this to change the percentage of walls

        maze = Maze(size, wall_percentage)
        maze.print_maze()

        choice = input("Options:\n1. Print Path (Dijkstra)\n2. Generate Another Maze\n3. Exit\nEnter your choice: ")

        if choice == '1':
            start = (0, 0)
            end = (size - 1, size - 1)
            path = find_path_dijkstra(maze.maze, start, end)
            if path:
                for x, y in path:
                    maze.maze[x][y] = PATH
                maze.print_maze()
            else:
                print("No path found.")
        elif choice == '2':
            continue
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
