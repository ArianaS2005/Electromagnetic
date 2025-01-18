import numpy as np

epsilon_0 = 8.854e-12  # Vacuum permittivity in F/m

# Function to calculate potential using Laplace's equation
def calculate_potential_laplace(Q, R, r_point):
    """
    Calculate the electric potential at a point using Laplace's equation for a uniformly charged sphere.
    
    Parameters:
    Q (float): Total charge of the sphere (Coulombs)
    R (float): Radius of the sphere (meters)
    r_point (numpy array): Position vector (x, y, z) where the potential is calculated (meters)
    
    Returns:
    float: Electric potential at the point r_point (Volts)
    """
    r = np.linalg.norm(r_point)

    

    if r > R:
        potential = Q / (4 * np.pi * epsilon_0 * r)
    else:
        surface_potential = Q / (4 * np.pi * epsilon_0 * R)
        potential = surface_potential
    
    return potential

def get_input():
    Q = float(input("Enter the total charge of the sphere (in Coulombs): "))  
    R = float(input("Enter the radius of the sphere (in meters): "))  
    x = float(input("Enter the x-coordinate of the point (in meters): "))
    y = float(input("Enter the y-coordinate of the point (in meters): "))
    z = float(input("Enter the z-coordinate of the point (in meters): "))
    
    r_point = np.array([x, y, z])
    
    return Q, R, r_point


def main():
    Q, R, r_point = get_input()
    
    potential = calculate_potential_laplace(Q, R, r_point)
    
    print(f"The electric potential at point {r_point} is {potential:.2e} V")

if __name__ == "__main__":
    main()
