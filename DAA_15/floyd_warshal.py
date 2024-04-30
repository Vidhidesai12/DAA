#Vidhi Desai
#1002081553
def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('inf') for _ in range(V)] for _ in range(V)]
    
    # Initialize distances for existing edges
    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
    
    # Calculate shortest paths
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example usage:
graph = [
    [0, 2, 5, float('inf')],
    [float('inf'), 0, 1, 2],
    [float('inf'), float('inf'), 0, 5],
    [float('inf'), float('inf'), float('inf'), 0]
]

shortest_distances = floyd_warshall(graph)
print("Shortest distances between all pairs of vertices:")
for row in shortest_distances:
    print(row)
