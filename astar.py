import heapq

# Heuristic function (Manhattan Distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    
    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        x, y = current
        
        # Neighbors (up, down, left, right)
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                temp_g = g_score[current] + 1

                if (nx, ny) not in g_score or temp_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = temp_g
                    f_score = temp_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f_score, (nx, ny)))
                    came_from[(nx, ny)] = current

    return None

# -------- MAIN --------
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

path = astar(grid, start, goal)

print("Shortest Path:", path)