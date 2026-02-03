import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
import pandas as pd

# HER = 0 V vs SHE, OER = 1.23 V vs SHE

# variables for Mill's model
JG = 0.5             # Gartner Current (mA/cm^2)
VscBar = 1.9 * 40    # semiconductor voltage (thermal units)((1.9 * 40) for CoOx driving OER and (0.4 * 40) for Pt driving the HER)
Jbarvbcat = 1e-10    # valance band equilibrium exchange current density "default values" (mA/cm^2)
Jbarcbcat = 1e-10    # conduction band equilibrium exchange current density "default values" (mA/cm^2)            
Jbarcatsol = 1e-3    # equilibrium exchange current density catalyst (mA/cm^2)((1e-3) for CoOx driving OER and (1) for Pt driving the HER)

pBar = 1e-30           # bulk hole concentration (cm^-3)
nBar = 1e17          # bulk electron concentration (cm^-3)

# constants
q = 1.602e-19      # elementary charge (C)
Dp = 3.4e-4        # hole diffusion coefficient from effective mass 1.3 me (cm^2/s)
delta = 1e-6       # hole diffusion length (cm)
kR = 1e-30         # recombination rate constant (cm^3/s)
w = 1e-5           # depletion width "default value" (cm)
E_g = 3.2          # bandgap (V)
kB = 1.381e-23     # Boltzmann's constant (J/K)
T = 300            # absolute temperature (K)
eps = 8.854e-14    # permittivity of free space (F/cm)
epsr = 300         # relative permittivity of SrTiO3

me = 9.11e-31       # mass of an electron (kg)
m_eff_e = 1.3 * me  # effective mass of electrons in SrTiO3
h = 6.626e-34       # Planck's constant (J·s)

# calculated constants
V_T = kB * T / q                 # thermal voltage in in V (V)
psBar = pBar * np.exp(VscBar)    # surface hole concentration (cm^-3)
epss = eps * epsr                # permittivity of SrTiO₃ (F/cm)

# calculated variables
w = np.sqrt((2*epss*VscBar/40)/(q*nBar))               # depletion width (cm)
print (f"w = {w}")

##from thermionic emission theory
A_n_star = (4 * np.pi * q * m_eff_e * kB**2) / (h**3) * 1e-4     # calculate Richardson constant
print(f"A_n_star = {A_n_star}")
A_p_star = A_n_star                 

# effective mass of holes assumed to be equal to electron                                                               
# However, hole effective mass has been reported to be around 5*m    

Jbarvbcat = A_p_star * T**2 * np.exp(-(E_g - VscBar / 40) / V_T) * 1000  # valance band equilibrium exhange current density (mA/cm^2)
Jbarcbcat = A_n_star * T**2 * np.exp(-(VscBar / 40) / V_T) *1000         # conduction band equilibrium exhange current density (mA/cm^2)

# Calculate JRbar from Equation (33)
#JRbar = q * (Dp / delta + kR * w * nBar) * psBar * np.exp(-VscBar)
JRbar = 1e-70
print(f"JRbar = {JRbar}")

#Governing Equations: 

def Jvbcat(ps, Ecat):
    return Jbarvbcat * (-np.exp(-Ecat) + ps / psBar)

def Jcbcat(Ecat, Vsc):
    return Jbarcbcat * (np.exp(Ecat) - np.exp(-Vsc))

def Jcatsol(Ecat):
    return Jbarcatsol * (np.exp(-Ecat / 2) - np.exp(Ecat / 2))

def solve_ps(Ecat, Vsc):
    '''This was done is Mills work...
    make ps a function of Ecat and Vsc, solve explicitly. 
    This assumes: Jbarvbcat is non zero, psBar is positive and finite, 
    and it neglects surface recombination by surface states - backwards, 
    flux is wrapped into the Jp term, system is at steady-state'''     
    A = JRbar * np.exp(VscBar - Vsc) / psBar
    B = Jbarvbcat / psBar
    numerator = JG + Jbarvbcat * np.exp(-Ecat)
    denominator = A + B if (A + B) > 0 else 1e-20  # avoid div/0
    return numerator / denominator

# Voltage sweep

Vsc_range = np.linspace(0.5 * 40, -1.5 * 40, 100)
results = []

for Vsc in Vsc_range:
    def residual(Ecat):
        ps = solve_ps(Ecat, Vsc)
        return Jcatsol(Ecat) - (Jvbcat(ps, Ecat) + Jcbcat(Ecat, Vsc))

    try:
        sol = root_scalar(residual, method='brentq', bracket=[-80, 80])
        if sol.converged:
            Ecat_sol = sol.root
            ps_sol = solve_ps(Ecat_sol, Vsc)
            Jcat_sol = Jcatsol(Ecat_sol)
            results.append((Vsc / 40, Jcat_sol, ps_sol))
        else:
            results.append((Vsc / 40, np.nan, np.nan))
    except ValueError:
        results.append((Vsc / 40, np.nan, np.nan))

# Plot results

results = np.array(results)
plt.figure()
plt.plot(results[:, 0], results[:, 1], label="Jcatsol")
plt.xlabel("V_app (V)")
plt.ylabel("Jcatsol (mA/cm²)")
plt.title("Jcatsol vs V_app")
plt.grid(True)
plt.ylim([-1, 1])
plt.tight_layout()
plt.legend()
plt.show()
