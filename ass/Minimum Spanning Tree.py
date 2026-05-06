# Minimum Spanning Tree using Prim's Algorithm

INF = 9999999

V = 5

graph = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

selected = [False] * V

selected[0] = True

edge_count = 0

print("Edge : Weight")

while edge_count < V - 1:

    minimum = INF
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and graph[i][j]:

                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {graph[x][y]}")

    selected[y] = True
    edge_count += 1