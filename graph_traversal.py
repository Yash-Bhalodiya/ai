graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# ---------------- DFS (Recursive) ----------------
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# ---------------- BFS ----------------
def bfs(graph, start):
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# ---------------- MAIN ----------------
print("DFS Traversal:")
dfs(graph, 'A', set())

print("\nBFS Traversal:")
bfs(graph, 'A')