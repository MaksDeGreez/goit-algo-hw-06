import networkx as nx

G = nx.Graph()
G.add_nodes_from(range(1, 11))
edges = [
    (1, 2), (1, 3), (2, 3), (2, 4), (3, 5),
    (4, 5), (4, 6), (5, 7), (6, 7), (6, 8),
    (7, 9), (8, 9), (8, 10), (9, 10)
]
G.add_edges_from(edges)

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                stack.append((neighbor, path + [neighbor]))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in set(graph.neighbors(vertex)) - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))

dfs_result = list(dfs_paths(G, 1, 10))
print("DFS paths from node 1 to node 10:")
for path in dfs_result:
    print(path)

bfs_result = list(bfs_paths(G, 1, 10))
print("\nBFS paths from node 1 to node 10:")
for path in bfs_result:
    print(path)
