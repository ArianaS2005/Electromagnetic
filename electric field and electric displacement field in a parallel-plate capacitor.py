import numpy as np

epsilon_0 = 8.854e-12  

# Function to calculate electric field and electric displacement field in a parallel-plate capacitor
def calculate_fields(V, d, A, epsilon_r):
    """
    Calculate the electric field and electric displacement field in a parallel-plate capacitor 
    filled with a dielectric.
    
    Parameters:
    V (float): Voltage applied across the plates (Volts)
    d (float): Separation between the plates (meters)
    A (float): Area of the plates (square meters)
    epsilon_r (float): Relative permittivity (dielectric constant) of the material
    
    Returns:
    E (float): Electric field inside the capacitor (Volts per meter)
    D (float): Electric displacement field inside the capacitor (Coulombs per square meter)
    C (float): Capacitance of the capacitor (Farads)
    """
    E = V / d
    D = epsilon_0 * epsilon_r * E
    C = (epsilon_0 * epsilon_r * A) / d
    
    return E, D, C

def get_input():
    V = float(input("Enter the applied voltage across the plates (in Volts): "))
    d = float(input("Enter the separation between the plates (in meters): "))
    A = float(input("Enter the area of the plates (in square meters): "))
    epsilon_r = float(input("Enter the relative permittivity (dielectric constant) of the material: "))
    
    return V, d, A, epsilon_r


def main():
    V, d, A, epsilon_r = get_input()
    
    E, D, C = calculate_fields(V, d, A, epsilon_r)
    
    print(f"Electric field (E) inside the capacitor: {E:.2e} V/m")
    print(f"Electric displacement field (D) inside the capacitor: {D:.2e} C/m²")
    print(f"Capacitance of the capacitor: {C:.2e} F")

if __name__ == "__main__":
    main()
