import numpy as np
import matplotlib.pyplot as plt

epsilon_0 = 8.854e-12  
mu_0 = 4 * np.pi * 1e-7  
c = 1 / np.sqrt(epsilon_0 * mu_0)  

def get_input():
    L = float(input("Enter the length of the grid (in meters): ")) 
    Nx = int(input("Enter the number of grid points: ")) 
    pulse_width = float(input("Enter the width of the Gaussian pulse: "))  
    source_position = int(input(f"Enter the source position (0 to {Nx-1}): ")) 
    
    dx = L / Nx
    dt = dx / (2 * c)  # Time step to ensure stability
    T = int(input("Enter the number of time steps: "))  # Number of time steps
    
    return L, Nx, dx, dt, T, pulse_width, source_position

def gaussian_source(t, pulse_width):
    return np.exp(-((t - 30) / pulse_width)**2)

def run_simulation(L, Nx, dx, dt, T, pulse_width, source_position):
    Ez = np.zeros(Nx)  # Electric field (z-direction)
    Hy = np.zeros(Nx)  # Magnetic field (y-direction)

    for t in range(1, T):
        Hy[:-1] = Hy[:-1] - (dt / (mu_0 * dx)) * (Ez[1:] - Ez[:-1])

        Ez[1:] = Ez[1:] - (dt / (epsilon_0 * dx)) * (Hy[1:] - Hy[:-1])

        Ez[source_position] += gaussian_source(t, pulse_width)

        if t % 10 == 0:
            plt.clf()
            plt.subplot(2, 1, 1)
            plt.plot(Ez)
            plt.title(f"Electric Field (Ez) at time step {t}")
            plt.ylim(-1, 1)
            plt.subplot(2, 1, 2)
            plt.plot(Hy)
            plt.title(f"Magnetic Field (Hy) at time step {t}")
            plt.ylim(-1, 1)
            plt.pause(0.1)

    plt.show()

L, Nx, dx, dt, T, pulse_width, source_position = get_input()

run_simulation(L, Nx, dx, dt, T, pulse_width, source_position)
