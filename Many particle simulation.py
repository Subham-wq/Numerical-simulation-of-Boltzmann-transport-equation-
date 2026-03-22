import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 20
Lx, Ly = 6, 4

# Initial positions
x = np.random.uniform(0.5, Lx-0.5, N)
y = np.random.uniform(0.5, Ly-0.5, N)

# Initial velocities
vx = np.random.uniform(-2, 2, N)
vy = np.random.uniform(-2, 2, N)

dt = 0.05
r = 0.15
time = 40
steps = int(time / dt)

x_list, y_list = [], []

# Simulation
for _ in range(steps):

    # Move particles
    for i in range(N):
        x[i] += vx[i] * dt
        y[i] += vy[i] * dt

        # Wall reflection
        if x[i] <= r:
            x[i] = r
            vx[i] *= -1
        if x[i] >= Lx - r:
            x[i] = Lx - r
            vx[i] *= -1

        if y[i] <= r:
            y[i] = r
            vy[i] *= -1
        if y[i] >= Ly - r:
            y[i] = Ly - r
            vy[i] *= -1

    # Particle collisions
    for i in range(N):
        for j in range(i+1, N):

            dx = x[i] - x[j]
            dy = y[i] - y[j]
            dist = np.sqrt(dx**2 + dy**2)

            if dist < 2*r:
                nx = dx / dist
                ny = dy / dist

                vrel = (vx[i] - vx[j]) * nx + (vy[i] - vy[j]) * ny

                vx[i] -= vrel * nx
                vy[i] -= vrel * ny
                vx[j] += vrel * nx
                vy[j] += vrel * ny

    # Store positions
    x_list.append(x.copy())
    y_list.append(y.copy())

# Animation
fig, ax = plt.subplots()
ax.set_xlim(0, Lx)
ax.set_ylim(0, Ly)
ax.set_aspect('equal')

particles, = ax.plot([], [], 'bo', markersize=4)

def update(frame):
    particles.set_data(x_list[frame], y_list[frame])
    return particles,

anim = FuncAnimation(fig, update, frames=len(x_list), interval=30)
plt.show()
