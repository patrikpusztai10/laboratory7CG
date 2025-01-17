import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from shapely.geometry import Polygon, Point
import numpy as np

P1 = (4, -4)
P2 = (-5, 6)
P3 = (6, -4)
P4 = (-7, 4)
P5 = (9, 6)
P6 = (11, 6)
P7 = (11, -6)
P8 = (9, -6)
P9 = (-7, -4)
P10 = (6, 4)
P11 = (-5, -6)
P12 = (4, 4)
P = [P9, P11, P1, P3, P8, P7, P6, P5, P10, P12, P2, P4]

polygon = Polygon(P)
min_x, min_y, max_x, max_y = polygon.bounds
x = np.linspace(min_x, max_x, 100)
y = np.linspace(min_y, max_y, 100)
xx, yy = np.meshgrid(x, y)
grid_points = np.c_[xx.ravel(), yy.ravel()]
inside_points = [Point(p).coords[0] for p in grid_points if polygon.contains(Point(p))]

#Camera position
camera= (4, 0)


lines = [[camera, point] for point in inside_points]
fig, ax = plt.subplots()
x, y = polygon.exterior.xy
ax.plot(x, y, label="Polygon", color="black")
lc = LineCollection(lines, colors="blue", linewidths=0.5, alpha=0.1)
ax.add_collection(lc)
ax.plot(camera[0], camera[1], "ro", label="Camera")

ax.legend()
plt.title("Rays from Camera to Polygon Interior Points")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.show()
