def is_safe(maze, n, x, y):
    return (x >= 0 and x < n and y >= 0 and y < n and maze[x][y] == 1)

def rat_in_a_maze(maze, n, x, y, solution, path_count):
    if (x == n - 1 and y == n - 1):
        solution.append(path_count)
        return
    
    if is_safe(maze, n, x, y):
        maze[x][y] = 0
        
        rat_in_a_maze(maze, n, x + 1, y, solution, path_count + 1) 
        rat_in_a_maze(maze, n, x, y + 1, solution, path_count + 1) 
        
        maze[x][y] = 1 
        return

def solve_maze(maze, n):
    solution = []
    rat_in_a_maze(maze, n, 0, 0, solution, 0)
    
    if len(solution) == 0:
        print("No path found")
    else:
        print("Number of possible paths:", len(solution))

maze = [[1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 0, 1, 1],
        [1, 1, 1, 1]]

n = len(maze)
solve_maze(maze, n)