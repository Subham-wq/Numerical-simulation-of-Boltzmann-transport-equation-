# Boltzmann Transport Simulation – Dilute Gas (Molecular Dynamics)

## Overview

This project simulates a dilute gas using elastic hard-sphere particle collisions inside a 2D box with reflecting boundaries. The simulation demonstrates how Boltzmann transport and statistical mechanics emerge from Newtonian mechanics through many-particle collisions.

Instead of directly solving the Boltzmann equation PDE, this project uses particle dynamics (molecular dynamics approach), where macroscopic thermodynamic behavior emerges from microscopic collisions.

---

## Physics Model

The system consists of:

* N particles in a 2D box
* Elastic particle–particle collisions
* Reflecting boundary walls
* No external force (free streaming + collisions)
* Dilute gas approximation (binary collisions only)

This corresponds to the Boltzmann equation without external force:

∂f/∂t + v · ∇f = (∂f/∂t)_collision

Where:

* Free streaming → particle motion
* Collision term → elastic particle collisions
* Distribution function → velocity histogram

---

## Features of the Simulation

The simulation includes:

* Random initialization of particle positions and velocities
* Elastic collisions between particles
* Reflecting boundary conditions
* Animation of particle motion
* Temperature calculation from kinetic energy
* Energy conservation check
* Velocity distribution evolution (Maxwell–Boltzmann distribution)

---

## Temperature Calculation

Temperature is computed from average kinetic energy:

T = (1/2) ⟨vx² + vy²⟩

This follows kinetic theory where temperature is proportional to the mean squared velocity.

---

## What This Simulation Demonstrates

This simulation shows the emergence of macroscopic physics from microscopic mechanics:

| Microscopic Mechanics  | Macroscopic Physics      |
| ---------------------- | ------------------------ |
| Particle motion        | Free streaming           |
| Elastic collisions     | Boltzmann collision term |
| Many particles         | Gas                      |
| Average kinetic energy | Temperature              |
| Wall collisions        | Pressure                 |
| Velocity histogram     | Maxwell distribution     |
| Random motion          | Diffusion                |
| Collisions             | Thermalization           |

This connects:
Newton Mechanics → Boltzmann Equation → Thermodynamics


## How to Run

Install dependencies:

```
pip install numpy matplotlib
```

Run the simulation:

```
python main.py
```

---

## Project Type

This project lies at the intersection of:

* Statistical Mechanics
* Kinetic Theory
* Boltzmann Transport
* Molecular Dynamics
* Computational Physics

---

## Summary

This project demonstrates how thermodynamics and statistical mechanics emerge from simple Newtonian particle collisions, providing a computational approach to understanding the Boltzmann transport equation and dilute gas dynamics.
