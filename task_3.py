import networkx as nx
import heapq
import random

G = nx.Graph()
G.add_nodes_from(range(1, 11))
edges = [
    (1, 2), (1, 3), (2, 3), (2, 4), (3, 5),
    (4, 5), (4, 6), (5, 7), (6, 7), (6, 8),
    (7, 9), (8, 9), (8, 10), (9, 10)
]
for edge in edges:
    weight = random.randint(1, 10)
    G.add_edge(edge[0], edge[1], weight=weight)

def dijkstra(graph, source):
    distances = { vertex: float('inf') for vertex in graph.nodes() }
    previous_vertices = { vertex: None for vertex in graph.nodes() }
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.neighbors(current_vertex):
            edge_weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + edge_weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices

def get_shortest_path(previous_vertices, target):
    path = []
    current_vertex = target
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    return path

# Apply the algorithm for all pairs of nodes
nodes = list(G.nodes())
shortest_paths = dict()

for source in nodes:
    distances, previous_vertices = dijkstra(G, source)
    for target in nodes:
        if source != target:
            path = get_shortest_path(previous_vertices, target)
            length = distances[target]
            shortest_paths[(source, target)] = (path, length)

for (source, target), (path, length) in shortest_paths.items():
    print(f"\nShortest path from node {source} to node {target}: {path}")
    print(f"Total weight: {length}")
