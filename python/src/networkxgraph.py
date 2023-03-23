import networkx as nx
import matplotlib.pyplot as plt

# Create an empty directed graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_nodes_from(["P1", "P2", "R1", "R2", "R3"])

# Add edges between nodes
G.add_edges_from([("P2", "R1"), ("R1", "P1"), ("P1", "R2"), ("P1", "R3"), ("P2", "R2"), ("P2", "R3")])

# Set node labels
node_labels = {"P1": "P1", "P2": "P2", "R1": "R1", "R2": "R2", "R3": "R3"}
nx.set_node_attributes(G, node_labels, "label")

# Set node colors
node_colors = {"P1": "green", "P2": "green", "R1": "yellow", "R2": "yellow", "R3": "yellow"}
nx.set_node_attributes(G, node_colors, "color")

# Set edge labels
edge_labels = {("P2", "R1"): "request", ("R1", "P1"): "grant", ("P1", "R2"): "claim", ("P1", "R3"): "claim", ("P2", "R2"): "claim", ("P2", "R3"): "claim"}
nx.set_edge_attributes(G, edge_labels, "label")

# Set edge colors
edge_colors = {("P2", "R1"): "blue", ("R1", "P1"): "green", ("P1", "R2"): "blue", ("P1", "R3"): "blue", ("P2", "R2"): "red", ("P2", "R3"): "red"}
nx.set_edge_attributes(G, edge_colors, "color")

# Set edge styles
edge_styles = {("P2", "R1"): "dashed", ("R1", "P1"): "solid", ("P1", "R2"): "dashed", ("P1", "R3"): "dashed", ("P2", "R2"): "dashed", ("P2", "R3"): "dashed"}
nx.set_edge_attributes(G, edge_styles, "style")

# Set node positions
pos = {"P1": (0, 1), "P2": (0, -1), "R1": (1, 0), "R2": (2, 1), "R3": (2, -1)}

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=1000, font_size=14, node_color=[node_colors[node] for node in G.nodes()], edge_color=[edge_colors[edge] for edge in G.edges()], style=[edge_styles[edge] for edge in G.edges()], labels=nx.get_node_attributes(G, "label"))
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "label"), font_color="black", font_size=12)

# Show the plot
plt.show()

