import numpy as np
import scipy.constants as const
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import pandas as pd

# HER = 0 V vs SHE, OER = 1.23 V vs SHE
# Constants
q = 1.602e-19      # Elementary charge (C)
k = 1.38e-23       # Boltzmann constant (J/K)
T = 300            # Temperature in Kelvin
V_T = k*T/q        # (V)

# Material-specific parameters
A_p_star = 150           # Hole Richardson constant ((A*cm^-2*K^-2)) 
                         # (example value, calculated from a effective mass of 1.3))
A_n_star = 150           # Electron Richardson constant ((A*cm^-2*K^-2))
                         # (example value, calculated from a effective mass of 1.3))
E_g = 3.2                # Bandgap energy (V) (SrTiO3)
phi_b_n = 1.9            # Barrier height (V)
                         # (example values: CoOx|nSTO = 1.3, Pt|nSTO = 0.9, HER|nSTO = 0.4, OER|nSTO = 1.9)
J_0_cat = 1e-3           # Equilibrium exchange current density (A/cm^2) (example value)
J_ph = 1*10**-3.3        # Photocurrent density (A/m^2) (example value)
m_J_0_p = 1              # scaling factor for the equilibrium exchange current density to account for the thermalization
m_J_0_n = 1              # scaling factor for the equilibrium exchange current density to account for the thermalization


# Compute equilibrium exchange current densities
J_0_p = m_J_0_p * A_p_star * T**2 * np.exp(-1*(E_g - phi_b_n) / (V_T))
J_0_n = m_J_0_n *  A_n_star * T**2 * np.exp(-phi_b_n / V_T)

# Ranges
V_app_values = np.linspace(-2, 1, 1000)     # Voltage range, V=0 -|> Vjxn -> Vcat
J_0_cat_values = np.linspace(1e-3,1,3)      # Equilibrium exchange current density (A/cm^2)
J_cat_values = []
J_cat_guess = 1e-2                          # Initial guess for J_cat

# Function to solve for J_cat
def J_cat_equation(J_cat, V_app):
    V_cat = (2 * V_T) * np.arcsinh(J_cat / (2 * J_0_cat))
    term1 = J_0_p * np.exp(( V_cat) / (V_T)) * (np.exp((V_app - 2 * V_cat) / (V_T)) - 1)
    term2 = J_0_n * np.exp(- V_cat / (V_T)) * (np.exp(-(V_app - 2 * V_cat) / (V_T)) - 1)
    return term1 - term2 + J_ph - J_cat

# Iterate over V_app values
for V_app in V_app_values:
    J_cat_solution = fsolve(J_cat_equation, J_cat_guess, args=(V_app))[0]
    J_cat_values.append(J_cat_solution)
    J_cat_guess = J_cat_solution  # Update guess for next iteration

# Convert to numpy array
J_cat_values = np.array(J_cat_values)

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(V_app_values, J_cat_values, label='J_cat vs V_app')
plt.xlabel('Applied Voltage (V)')
plt.ylabel('J_cat (A/m^2)')
plt.title('Numerical Solution for J_cat as a Function of V_app')
plt.legend()
plt.ylim(-0.0002, 0.0006)
plt.grid()
plt.show()
