import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
Lx = 6
Ly = 4
# Initial positions
x1, x2 = 1.0, 3.0
y1, y2 = 0.0, 2.0

# Velocities
vx1, vx2 = 1.0, -1.0
vy1, vy2 = 2.0, -2.0

dt = 0.05
r = 0.2
r_wall=0.02
time=10
steps= int(time/dt)

x1_list, y1_list = [], []
x2_list, y2_list = [], []

# Simulation

for _ in range(steps):
    x1 += vx1 * dt
    y1 += vy1 * dt
    x2 += vx2 * dt
    y2 += vy2 * dt

    # Reflecting boundaries for particle 1
    if x1 <= r_wall:
        x1 = r_wall
        vx1 = -vx1
    if x1 >= Lx - r_wall:
        x1 = Lx - r_wall
        vx1 = -vx1

    if y1 <= r_wall:
        y1 = r_wall
        vy1 = -vy1
    if y1 >= Ly - r_wall:
        y1 = Ly - r_wall
        vy1 = -vy1

    # Reflecting boundaries for particle 2
    if x2 <= r_wall:
        x2 = r_wall
        vx2 = -vx2
    if x2 >= Lx - r_wall:
        x2 = Lx - r_wall
        vx2 = -vx2

    if y2 <= r_wall:
        y2 = r_wall
        vy2 = -vy2
    if y2 >= Ly - r_wall:
        y2 = Ly - r_wall
        vy2 = -vy2

    dx = x1 - x2
    dy = y1 - y2
    dist = np.sqrt(dx**2 + dy**2)

    if dist < 2*r:
        nx = dx / dist
        ny = dy / dist

        vrel = (vx1 - vx2) * nx + (vy1 - vy2) * ny

        vx1 = vx1 - vrel * nx
        vy1 = vy1 - vrel * ny

        vx2 = vx2 + vrel * nx
        vy2 = vy2 + vrel * ny

    x1_list.append(x1)
    y1_list.append(y1)
    x2_list.append(x2)
    y2_list.append(y2)

# Animation
fig, ax = plt.subplots()
ax.set_xlim(0, Lx)
ax.set_ylim(0, Ly)

particle1, = ax.plot([], [], 'ro', markersize=12)
particle2, = ax.plot([], [], 'bo', markersize=12)

def update(frame):
    particle1.set_data([x1_list[frame]], [y1_list[frame]])
    particle2.set_data([x2_list[frame]], [y2_list[frame]])
    return particle1, particle2

anim = FuncAnimation(fig, update, frames=len(x1_list), interval=50)

plt.show()