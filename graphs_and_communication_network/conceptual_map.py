import matplotlib.pyplot as plt
import networkx as nx

# Original expanded concepts
concepts_expanded = [
    "Complex Systems",
    "Chaos Theory",
    "Information",
    "Entropy",
    "Communication",
    "Swarms",
    "Intellect",
    "Self-Organisation",
    "Simple Rules",
    "Complex Behavior",
    "Automatons",
    "Non-Linearity",
    "Games",
    "Networks",
    "Thermodynamics",
    "Criticality",
    "Fractals"
]

# Add new concepts
concepts_final = concepts_expanded + ["Adaptation", "Flexibility", "Energy"]

# Expanded edges
edges_expanded = [
    ("Complex Systems", "Chaos Theory"),
    ("Complex Systems", "Self-Organisation"),
    ("Complex Systems", "Swarms"),
    ("Complex Systems", "Communication"),
    ("Complex Systems", "Networks"),
    ("Chaos Theory", "Non-Linearity"),
    ("Chaos Theory", "Fractals"),
    ("Chaos Theory", "Criticality"),
    ("Information", "Entropy"),
    ("Information", "Communication"),
    ("Information", "Networks"),
    ("Information", "Intellect"),
    ("Entropy", "Thermodynamics"),
    ("Entropy", "Criticality"),
    ("Communication", "Swarms"),
    ("Swarms", "Self-Organisation"),
    ("Swarms", "Simple Rules"),
    ("Swarms", "Complex Behavior"),
    ("Self-Organisation", "Intellect"),
    ("Self-Organisation", "Automatons"),
    ("Simple Rules", "Automatons"),
    ("Simple Rules", "Games"),
    ("Complex Behavior", "Intellect"),
    ("Automatons", "Games"),
    ("Games", "Networks"),
    ("Networks", "Criticality"),
    ("Non-Linearity", "Complex Behavior"),
    ("Thermodynamics", "Self-Organisation"),
    ("Criticality", "Fractals"),
    ("Fractals", "Complex Behavior")
]

# Add new connections
edges_final = edges_expanded + [
    ("Adaptation", "Flexibility"),
    ("Adaptation", "Intellect"),
    ("Flexibility", "Self-Organisation"),
    ("Energy", "Thermodynamics"),
    ("Energy", "Self-Organisation"),
    ("Energy", "Complex Systems")
]

# Create final graph
G_final = nx.Graph()
G_final.add_nodes_from(concepts_final)
G_final.add_edges_from(edges_final)

# Draw graph
plt.figure(figsize=(12, 14))
pos = nx.spring_layout(G_final, seed=23, k=1.2)
# pos = nx.kamada_kawai_layout(G_final)
# pos = nx.circular_layout(G_final)
# pos = nx.shell_layout(G_final)
nx.draw_networkx_nodes(G_final, pos, node_size=1000, node_color="#FFD580", edgecolors="black")
nx.draw_networkx_edges(G_final, pos, arrows=True, width=1.8, alpha=0.6) # connectionstyle="arc3,rad=0.4"
nx.draw_networkx_labels(G_final, pos, font_size=9, font_weight="bold")

nx.write_gexf(G_final, "network.gexf")

# Title
plt.title("Expanded Concept Map of Complexity, Chaos, and Emergence", fontsize=14, fontweight="bold")
plt.axis("off")

# Save as PNG
plt.savefig("complexity_final.png", format="png", dpi=300, bbox_inches="tight")
plt.show()

