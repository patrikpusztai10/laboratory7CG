import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay


def create_tr(nv, ne, tt):
    if nv < 3:
        print("Error: At least 3 vertices are required for Delaunay triangulation.")
        return None, 0, None

    points = np.random.rand(nv, 2)

    delaunay = Delaunay(points)
    G = nx.Graph()
    G.add_nodes_from(range(nv))
    edges = set()
    for simplex in delaunay.simplices:
        for i in range(3):
            edge = tuple(sorted((simplex[i], simplex[(i + 1) % 3])))
            edges.add(edge)
    if ne > len(edges):
        print(f"Error: Triangulation with {nv} vertices only provides "
              f"{len(edges)} edges, which is less than the requested {ne} edges.")
        return None, 0, points

    selected_edges = list(edges)[:ne]
    G.add_edges_from(selected_edges)

    triangles = [
        {u, v, w}
        for u, v in G.edges()
        for w in G.neighbors(u)
        if G.has_edge(v, w) and u != v and u != w and v != w
    ]
    triangle_count = len(set(frozenset(t) for t in triangles))

    print(f"Number of triangles found: {triangle_count}")

    return G, triangle_count, points


def visual_graph(graph, points,color_map):
    if graph is None:
        print("Cannot visualize an invalid graph.")
        return

    pos = {i: point for i, point in enumerate(points)}
    plt.figure(figsize=(6, 6))
    nx.draw(graph, pos, with_labels=True, node_color=color_map, edge_color="black",
            node_size=800, font_size=15)
    plt.title("Exercise 3")
    plt.show()
def make_3_colorable(graph):
    coloring = nx.coloring.greedy_color(graph, strategy="largest_first")
    color_set = set(coloring.values())
    if len(color_set) > 3:
        print("Error: The graph cannot be 3-colored.")
        return None
    else:
        color_map = [coloring[node] for node in graph.nodes()]
        return color_map

vc = int(input("Enter nr of vertices: "))
nredge = int(input("Enter nr of edges: "))
tr = int(input("Enter nr of desired triangles: "))

graph, triangle_count, points = create_tr(vc, nredge, tr)
if graph:
    color_map = make_3_colorable(graph)

    if color_map:
        visual_graph(graph, points, color_map)
    else:
        print("Graph could not be 3-colored.")
