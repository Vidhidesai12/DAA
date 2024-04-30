#Vidhi Desai
#1002081553
import heapq
def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    return dist

# Example usage and output:
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 1), ('D', 2)],
    'C': [('D', 5)],
    'D': []
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in shortest_distances.items():
    print(vertex + ":", distance)
