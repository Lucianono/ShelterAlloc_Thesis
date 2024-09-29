import networkx as nx # type: ignore
import matplotlib.pyplot as plt

# Define the distances between communities and shelters
Community = [
    {"name": "CommA", "population": 500, "distances": {"ShelA": 140, "ShelB": 220}},
    {"name": "CommB", "population": 400, "distances": {"ShelA": 530, "ShelB": 2100}},
    {"name": "CommC", "population": 300, "distances": {"ShelA": 1210, "ShelB": 420}}
]

Shelter = [
    {"name": "ShelA", "capacity": 10000, "cost": 500},
    {"name": "ShelB", "capacity": 10000, "cost": 500}
]

# Create a network graph
G = nx.Graph()

# Add communities as nodes
for community in Community:
    G.add_node(community["name"], type='community', size=community["population"])

# Add shelters as nodes
for shelter in Shelter:
    G.add_node(shelter["name"], type='shelter', size=shelter["capacity"] / 100)

# Add edges (with distances as weights)
for community in Community:
    for shelter in Shelter:
        distance = community["distances"][shelter["name"]]
        G.add_edge(community["name"], shelter["name"], weight=distance)

# Draw the graph
pos = nx.spring_layout(G)  # Use spring layout for positioning

# Draw nodes with different sizes
sizes = [G.nodes[node]['size'] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color='skyblue')

# Draw edges with labels (distances as weights)
edges = G.edges(data=True)
weights = [edge[2]['weight'] for edge in edges]
nx.draw_networkx_edges(G, pos, width=[w/500 for w in weights])  # Adjust width based on distance
nx.draw_networkx_labels(G, pos)

# Add edge labels (showing distances)
edge_labels = {(u, v): d['weight'] for u, v, d in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Community to Shelter Distance Network")
plt.show()
