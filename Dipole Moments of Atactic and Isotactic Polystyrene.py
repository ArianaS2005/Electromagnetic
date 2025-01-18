import numpy as np

epsilon_0 = 8.854e-12     
N_A = 6.022e23            
mu_0 = 0.60               
specific_volume = 0.9526  
temperature = 311.55      
refractive_index = 1.59   

# Experimental dielectric constants and concentrations
dielectric_constants = {
    "atactic": [2.1, 2.2, 2.3, 2.4],   # Example values for atactic polystyrene
    "isotactic": [2.5, 2.6, 2.7, 2.8]  # Example values for isotactic polystyrene
}
concentrations = [5, 10, 15, 20]       # Polymer concentrations (%)


def calculate_molar_polarization(epsilon_r, concentration):
    """
    Calculate molar polarization using the Debye equation.
    """
    # Convert concentration from % to g/cm³ 
    conc_g_per_cm3 = concentration / 100
    # Debye equation for molar polarization
    molar_polarization = (epsilon_r - 1) / (epsilon_r + 2) * (3 / (4 * np.pi * epsilon_0))
    
    return molar_polarization * specific_volume / conc_g_per_cm3


def calculate_dipole_moment(molar_polarization, N):
    """
    Calculate dipole moment using the relationship with molar polarization.
    """
    return np.sqrt(molar_polarization / (N * mu_0**2))



results = {}
for polymer_type, epsilons in dielectric_constants.items():
    molar_polarizations = []
    dipole_moments = []
    for epsilon_r, conc in zip(epsilons, concentrations):
        polarization = calculate_molar_polarization(epsilon_r, conc)
        molar_polarizations.append(polarization)
        
        N = 100       #number of repeating units in the polymer chain
        dipole_moment = calculate_dipole_moment(polarization, N)
        dipole_moments.append(dipole_moment)
    
    results[polymer_type] = {
        "molar_polarizations": molar_polarizations,
        "dipole_moments": dipole_moments,
    }

for polymer_type, data in results.items():
    print(f"{polymer_type.capitalize()} Polystyrene Results:")
    print("Concentration (%)\tMolar Polarization (cm³/mol)\tDipole Moment (D)")
    for conc, polar, dipole in zip(concentrations, data["molar_polarizations"], data["dipole_moments"]):
        print(f"{conc}\t\t\t{polar:.4e}\t\t\t{dipole:.4f}")
    print()
