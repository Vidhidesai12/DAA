class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph):
    edges = []
    for v in graph:
        for n, w in graph[v].items():
            edges.append((v, n, w))
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])

    mst = {}
    disjoint_set = DisjointSet(vertices)

    for edge in edges:
        v1, v2, w = edge
        if disjoint_set.find(v1) != disjoint_set.find(v2):
            disjoint_set.union(v1, v2)
            mst[(v1, v2)] = w

    return mst


graph = {
    'A': {'B': 3, 'D': 1},
    'B': {'A': 3, 'D': 3, 'C': 1},
    'C': {'B': 1, 'D': 1, 'E': 5},
    'D': {'A': 1, 'B': 3, 'C': 1},
    'E': {'C': 5}
}

minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree (Kruskal's Algorithm):")
for edge, weight in minimum_spanning_tree.items():
    print(edge, "-", weight)

