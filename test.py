import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

\

# Define the vector function r(t)
def r(t):
    return np.array([t, t**2, t**3])

# Calculate the points on the curve
curve_points = np.array([r(ti) for ti in t])

# Plot the curve
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(curve_points[:, 0], curve_points[:, 1], curve_points[:, 2])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show plot
plt.show()
