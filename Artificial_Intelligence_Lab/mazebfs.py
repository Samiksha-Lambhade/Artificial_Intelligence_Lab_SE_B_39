from collections import deque

def bfs(maze, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])  
    visited = {start}        # Set of visited cells
    parent = {start: None}   # Track path

    while queue:
        current = queue.popleft()
        if current == end:
            # Reconstruct path
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]   # Reverse path from start → end

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= next_cell[0] < len(maze) and
                0 <= next_cell[1] < len(maze[0]) and
                maze[next_cell[0]][next_cell[1]] != '#' and
                next_cell not in visited):

                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current  # Store parent

    return None  # No path found


# Example maze
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 0)
end = (6, 6)

path = bfs(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path exists.")
