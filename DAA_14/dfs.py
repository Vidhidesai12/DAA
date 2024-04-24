class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        if v in self.graph:
            for i in self.graph[v]:
                if i not in visited or not visited[i]:
                    self.dfs_util(i, visited)

    def dfs(self, v):
        visited = {node: False for node in self.graph}
        self.dfs_util(v, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

g = Graph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor in neighbors:
        g.add_edge(node, neighbor)

print("Depth First Traversal starting from vertex 'A':")
g.dfs('A')
