import matplotlib.pyplot as plt


def vis_pent(points):

    A, B, C, D, E, G = points['A'], points['B'], points['C'], points['D'], points['E'], points['G']
    pentagon_vertices = [A, B, C, D, E, A]

    conn_edges = [('A', 'G'), ('B', 'G'), ('D', 'G')]
    new_edges = [('C', 'G'), ('E', 'G')]
    col_tr = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'G'), ('B', 'G'), ('C', 'G')]

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.plot(*zip(*pentagon_vertices), label="Polygon Edges", color="brown")

    for edge in conn_edges + new_edges:
        p1, p2 = edge
        ax.plot(*zip(*[points[p1], points[p2]]), linestyle="dotted", color="orange" if edge in new_edges else "gray")

    for edge in col_tr:
        p1, p2 = edge
        ax.plot(*zip(*[points[p1], points[p2]]), color="green", linewidth=2, label="Triangle" if edge == col_tr[0] else "")

    for label, (x, y) in points.items():
        color = 'red' if label == 'G' else 'blue'
        ax.scatter(x, y, color=color, s=50, zorder=5)
        ax.annotate(label, (x, y), textcoords="offset points", xytext=(5, 5), ha='left', fontsize=10, color=color)

    ax.set_title("Exercise 5")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_aspect('equal', 'box')
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.legend(loc="upper right", fontsize="small")
    plt.show()

# Example points
#points = {"A": (0, 0), "B": (2, 2), "C": (4, 4), "D": (6, 0), "E": (3, -3), "G": (3, 1)}
points = {"A": (1, 0), "B": (1, 2), "C": (1, 4), "D": (4, 3), "E": (4, -1), "G": (2.5, 1.5)}
vis_pent(points)
