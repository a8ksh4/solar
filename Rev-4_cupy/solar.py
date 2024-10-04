#!/home/dan/venv/bin/python
'''foo
'''

import cupy as cp
import matplotlib
matplotlib.use('TkAgg')  # Change to an interactive backend
import matplotlib.pyplot as plt

# Simulation parameters
NUM_STARS = 1000  # Number of stars
# GRV_CONST = 6.67430e-11  # Gravitational constant
GRV_CONST = 2.0  # Gravitational constant
TIME_STEP = 0.1  # Time step
# MASS_MIN = 1e21  # Minimum mass
# MASS_MAX = 1e24  # Maximum mass
MASS_MIN = 1.0  # Minimum mass
MASS_MAX = 10.0  # Maximum mass



def main():
    # Initialize positions, velocities, and masses
    positions = cp.random.uniform(-1, 1, (NUM_STARS, 2))  # Random positions in 2D space
    velocities = cp.zeros((NUM_STARS, 2))  # Initial velocities
    masses = cp.random.uniform(MASS_MIN, MASS_MAX, NUM_STARS)  # Random masses

    for step in range(1000):
        if step % 10 == 0:
            # Calculate the current density and average velocity
            avg_vel = cp.mean(velocities, axis=0)
            avg_x_stdev = cp.std(velocities[:, 0])
            avg_y_stdev = cp.std(velocities[:, 1])
            print(step, avg_vel, avg_x_stdev, avg_y_stdev)

        # Calculate the gravitational forces
        diff = positions[:, cp.newaxis, :] - positions[cp.newaxis, :, :]
        dist_squared = cp.sum(diff ** 2, axis=-1) + 1e-9
        dist = cp.sqrt(dist_squared)
        forces = GRV_CONST * masses[:, cp.newaxis] * masses / dist_squared
        forces_matrix = forces[:, :, cp.newaxis] * diff / dist[:, :, cp.newaxis]
        net_forces = cp.sum(forces_matrix, axis=1)

        # Calculate the new velocities
        velocities += net_forces / masses[:, cp.newaxis] * TIME_STEP

        # Calculate the new positions
        positions += velocities * TIME_STEP


if __name__ == '__main__':
    main()
