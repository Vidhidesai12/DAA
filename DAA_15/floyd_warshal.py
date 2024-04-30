def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf') for _ in range(V)] for _ in range(V)]
    
    # Initialize distances for existing edges
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif j in graph[i]:
                dist[i][j] = graph[i][j]
    
    # Calculate shortest paths
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example usage:
graph = {
    0: {1: 3, 3: 8},
    1: {0: 3, 2: 1},
    2: {0: 5, 3: 2},
    3: {2: 2}
}

shortest_distances = floyd_warshall(graph)
print("Shortest distances between all pairs of vertices:")
for row in shortest_distances:
    print(row)
