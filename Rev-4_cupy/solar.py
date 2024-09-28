#!/home/dan/venv/bin/python
'''foo
'''

import cupy as cp
import matplotlib
matplotlib.use('TkAgg')  # Change to an interactive backend
import cupy as cp
import matplotlib.pyplot as plt

# Simulation parameters
N = 100  # Number of stars
G = 6.67430e-11  # Gravitational constant
dt = 0.01  # Time step
mass_min = 1e21  # Minimum mass
mass_max = 1e24  # Maximum mass

# Initialize positions, velocities, and masses
positions = cp.random.uniform(-1, 1, (N, 2))  # Random positions in 2D space
velocities = cp.zeros((N, 2))  # Initial velocities
masses = cp.random.uniform(mass_min, mass_max, N)  # Random masses

# Function to compute gravitational forces
def compute_forces(positions, masses):
    diff = positions[:, cp.newaxis, :] - positions[cp.newaxis, :, :]  # Pairwise differences
    dist_squared = cp.sum(diff ** 2, axis=-1) + 1e-9  # Squared distances with small offset to avoid division by zero
    dist = cp.sqrt(dist_squared)  # Distances
    forces = G * masses[:, cp.newaxis] * masses / dist_squared  # Gravitational force magnitude
    forces_matrix = forces[:, :, cp.newaxis] * diff / dist[:, :, cp.newaxis]  # Force vectors
    net_forces = cp.sum(forces_matrix, axis=1)  # Net forces on each star
    return net_forces

# Update the positions and velocities
def update_positions(positions, velocities, masses, dt):
    forces = compute_forces(positions, masses)
    accelerations = forces / masses[:, cp.newaxis]  # F = ma -> a = F/m
    velocities += accelerations * dt  # Update velocities
    positions += velocities * dt  # Update positions
    return positions, velocities

# Visualization setup
fig, ax = plt.subplots()
scat = ax.scatter([], [], s=1)  # Initialize scatter plot with empty data
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Initialize the scatter plot with the initial positions
scat.set_offsets(cp.asnumpy(positions))

# Run the simulation loop
for step in range(1000):  # Number of frames
    print(step)
    positions, velocities = update_positions(positions, velocities, masses, dt)
    # Update scatter plot with new positions converted from GPU to CPU
    scat.set_offsets(cp.asnumpy(positions))  # Transfer positions to CPU
    plt.pause(0.01)  # Pause briefly to update the plot

plt.show()

