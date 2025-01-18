import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from shapely.geometry import Polygon, Point
import numpy as np

P1 = (0, 5)
P2 = (3, -2)
P3 = (-1, -2)
P4 = (3, 0)
P5 = (1, 2)
P6 = (3, 2)
P = [P1, P5, P6, P4, P2, P3]

polygon = Polygon(P)

min_x, min_y, max_x, max_y = polygon.bounds
x = np.linspace(min_x, max_x, 100)
y = np.linspace(min_y, max_y, 100)
xx, yy = np.meshgrid(x, y)
grid_points = np.c_[xx.ravel(), yy.ravel()]
inside_points = [Point(p).coords[0] for p in grid_points if polygon.contains(Point(p))]
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Plot for subpoint a)
axs[0].plot(*polygon.exterior.xy, label="Polygon", color="black")
camera_position = (0, -1)
lines = [[camera_position, point] for point in inside_points]
lc = LineCollection(lines, colors="purple", linewidths=0.2, alpha=0.5)
axs[0].add_collection(lc)
axs[0].plot(camera_position[0], camera_position[1], "ro", label="Camera")

axs[0].set_title("Single Camera Monitoring the Polygon")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].grid(True)
axs[0].axis("equal")
axs[0].legend()

# Plot for subpoint b)
axs[1].plot(*polygon.exterior.xy, label="Polygon", color="black")
camera_positions = [(0, 4.3), (1.8, -1)]
colors = ["green", "blue"]
for camera, color in zip(camera_positions, colors):
    lines = [[camera, point] for point in inside_points]
    lc = LineCollection(lines, colors=color, linewidths=0.1, alpha=0.5)
    axs[1].add_collection(lc)
    axs[1].plot(camera[0], camera[1], "ro", label=f"Camera")
axs[1].set_title("Two Cameras Monitoring the Polygon")
axs[1].set_xlabel("x")
axs[1].set_ylabel("y")
axs[1].grid(True)
axs[1].axis("equal")
axs[1].legend()

plt.tight_layout()
plt.show()
