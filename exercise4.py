import networkx as nx
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np

def triangulate_and_color():
    #points = {'A': (1, 0), 'B': (0.5, 0.87), 'C': (-0.5, 0.87), 'D': (-1, 0), 'E': (-0.5, -0.87), 'F': (0.5, -0.87),'G': (0, -1)}
    points = {'A': (-1, -1),'B': (0, 0),'C': (1, 1),'D': (2, 0),'E': (1, -1),'F': (0, -2),'G': (-1, -2)}
    coordinates = np.array(list(points.values()))
    labels = list(points.keys())
    triangulation = Delaunay(coordinates)
    edges = set()

    for simplex in triangulation.simplices:
        for i in range(3):
            for j in range(i + 1, 3):
                edge = tuple(sorted((labels[simplex[i]], labels[simplex[j]])))
                edges.add(edge)
    graph = nx.Graph()
    graph.add_nodes_from(points.keys())
    graph.add_edges_from(edges)
    colors = nx.coloring.greedy_color(graph, strategy="largest_first")
    color_map = ['red', 'blue', 'green']
    plt.figure(figsize=(8, 8))
    pos = points
    nx.draw(
        graph, pos, with_labels=True, node_size=800,
        node_color=[color_map[colors[node]] for node in graph.nodes],
        edge_color='black', font_size=10
    )
    plt.title("Triangulated Graph with 3-Coloring")
    plt.show()
    print("Node Color Assignments:")
    for node, color in colors.items():
        print(f"{node}: {color_map[color]}")
triangulate_and_color()
