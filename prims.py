# Number of vertices
V = 5

# Graph represented as adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Function to find minimum key vertex
def min_key(key, mst_set):
    min_val = float('inf')
    min_index = -1

    for v in range(V):
        if key[v] < min_val and mst_set[v] == False:
            min_val = key[v]
            min_index = v

    return min_index

# Prim's Algorithm
def prim_mst(graph):
    key = [float('inf')] * V
    parent = [-1] * V
    key[0] = 0
    mst_set = [False] * V

    for _ in range(V):
        u = min_key(key, mst_set)
        mst_set[u] = True

        for v in range(V):
            if graph[u][v] > 0 and mst_set[v] == False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Print MST
    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# -------- MAIN --------
prim_mst(graph)