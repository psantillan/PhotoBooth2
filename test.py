import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the initial view
ax.view_init(elev=15, azim=-25)

# Set the axes limits
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Set the axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Create a FuncAnimation object to animate the Earth's orbit
earth_orbit, = ax.plot([], [], [], 'b')


def animate(i):
    # Generate the x, y, and z coordinates for the Earth's orbit
    x = np.cos(i)
    y = np.sin(i)
    z = 0

    # Update the Earth's orbit
    earth_orbit.set_data(x, y)
    earth_orbit.set_3d_properties(z)


anim = FuncAnimation(fig, animate, frames=np.linspace(0, 2 * np.pi, 120), interval=20)

# Show the animation
plt.show()
