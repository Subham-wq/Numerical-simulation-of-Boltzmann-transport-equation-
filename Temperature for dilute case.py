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
T_list = []
E_list = []
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
    # Temperature and energy
    v2 = vx ** 2 + vy ** 2
    T = 0.5 * np.mean(v2)
    E = 0.5 * np.sum(v2)

    T_list.append(T)
    E_list.append(E)
    # Store positions
    x_list.append(x.copy())
    y_list.append(y.copy())

    # Temperature and total energy
    v2 = vx ** 2 + vy ** 2
    T = 0.5 * np.mean(v2)
    E = 0.5 * np.sum(v2)

    T_list.append(T)
    E_list.append(E)

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
    plt.figure()
    plt.plot(T_list)
    plt.xlabel("Time step")
    plt.ylabel("Temperature")
    plt.title("Temperature vs Time")
    plt.show()
    plt.figure()
    plt.plot(E_list)
    plt.xlabel("Time step")
    plt.ylabel("Total Energy")
    plt.title("Energy vs Time")
    plt.show()

plt.show()
