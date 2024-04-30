#Vidhi Desai
#1002081553
def bellman_ford(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    
    for u in graph:
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative cycle")
    
    return dist

# Example usage and output:
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 1), ('D', 2)],
    'C': [('D', 5)],
    'D': []  
    
}

start_vertex = 'A'
shortest_distances = bellman_ford(graph, start_vertex)
print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in shortest_distances.items():
    print(vertex + ":", distance)
