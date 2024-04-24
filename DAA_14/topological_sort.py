from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
      visited[v] = True

      for neighbor in self.graph[v]:
          if neighbor not in visited:
              self.topological_sort_util(neighbor, visited, stack)

      stack.append(v)


    def topological_sort(self):
      visited = {node: False for node in self.graph}
      stack = []

      # Create a copy of the dictionary keys before iterating
      for node in list(self.graph.keys()):
          if not visited[node]:
              self.topological_sort_util(node, visited, stack)

      return stack[::-1]


# Example usage
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

g = Graph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor in neighbors:
        g.add_edge(node, neighbor)

print("Topological sorting of the graph:")
print(g.topological_sort())