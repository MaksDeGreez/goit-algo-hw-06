import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(range(1, 11))
edges = [
    (1, 2), (1, 3), (2, 3), (2, 4), (3, 5),
    (4, 5), (4, 6), (5, 7), (6, 7), (6, 8),
    (7, 9), (8, 9), (8, 10), (9, 10)
]
G.add_edges_from(edges)

pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("Transport Network Graph")
plt.axis('off')
plt.show()

# Analysis
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f"Number of nodes (intersections): {num_nodes}")
print(f"Number of edges (roads): {num_edges}")

degrees = dict(G.degree())
print("\nDegrees of nodes:")
for node, degree in degrees.items():
    print(f"Node {node}: {degree}")

average_degree = sum(degrees.values()) / num_nodes
print(f"\nAverage degree: {average_degree:.2f}")

shortest_path = nx.shortest_path(G, source=1, target=10)
print(f"\nShortest path from node 1 to node 10: {shortest_path}")

diameter = nx.diameter(G)
print(f"\nDiameter of the graph: {diameter}")

# Clustering coefficient
clustering_coeffs = nx.clustering(G)
print("\nClustering coefficients:")
for node, coeff in clustering_coeffs.items():
    print(f"Node {node}: {coeff:.2f}")

# Betweenness centrality
betweenness = nx.betweenness_centrality(G)
print("\nBetweenness centrality:")
for node, centrality in betweenness.items():
    print(f"Node {node}: {centrality:.2f}")
