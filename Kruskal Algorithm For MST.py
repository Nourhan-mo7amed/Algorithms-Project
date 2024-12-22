class DisjointSet:
    def __init__(self):
        self.parent = {}

    def makeSet(self, n):
        for i in range(n):
            self.parent[i] = i

    def find(self, k):
        if self.parent[k] == k:
            return k
        self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent[x] = y


def KruskalAlgo(edges, n):
    MST = []
    ds = DisjointSet()
    ds.makeSet(n)
    index = 0

    edges.sort(key=lambda x: x[2])

    while len(MST) != n - 1:
        (src, dest, weight) = edges[index]
        index += 1
        x = ds.find(src)
        y = ds.find(dest)
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)
    return MST


if __name__ == '__main__':
    print('###########################################################################################')
    print("# Welcome to Kruskal's Algorithm MST 3>                                                   #")
    print("# You need to input the graph as follows:                                                 #")
    print("# 1. Enter the total number of nodes.                                                     #")
    print("# 2. Enter the total number of edges.                                                     #")
    print("# 3. For each edge, enter three values: source node, destination node, and edge weight.   #")
    print("# Example: If you have an edge between node 0 and node 1 with weight 7, input: 0 1 7.     #")
    print("# Nodes are labelled from 0 to N-1.                                                       #")
    print('###########################################################################################')

    try:
        n = int(input("\nEnter the number of nodes(N): "))
        if n <= 0:
            raise ValueError("The number of nodes must be a positive integer.")

        m = int(input("Enter the number of edges(E): "))
        if m < 0:
            raise ValueError("The number of edges cannot be negative.")

        edges = []
        print("\nEnter the edges (source destination weight):")
        for i in range(m):
            edge_input = input(f"Edge {i + 1}: ").strip().split()
            if len(edge_input) != 3:
                raise ValueError("Each edge must have exactly 3 values: source, destination, weight.")

            src, dest, weight = map(int, edge_input)
            if src < 0 or src >= n or dest < 0 or dest >= n:
                raise ValueError(f"Node values must be between 0 and {n - 1}.")
            edges.append((src, dest, weight))

        mst = KruskalAlgo(edges, n)

        print("\nThe edges in the Minimum Spanning Tree (MST) are:")
        for src, dest, weight in mst:
            print(f"Edge ({src} - {dest}) with weight {weight}")

    except ValueError as e:
        print(f"Input Error: {e}")