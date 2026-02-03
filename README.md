# NatureCatalysis-CooperativeAdaptiveJunctions-2026
Python Code for Adaptive Junctions and Buried Junctions in "Cooperative Adaptive Junctions Govern Overall Photoelectrochemical Water Splitting"

# Adaptive and Buried Junction Simulations for Photoelectrochemical Water Splitting

This repository contains Python scripts used to generate and analyze numerical simulations reported in:

**Cooperative Adaptive Junctions Govern Overall Photoelectrochemical Water Splitting**  
*Nature Catalysis* (2026)

**Authors:**  
Aaron Kaufman¹²³, Kaden Wheeler³⁴, Ethan J. Crumlin⁵⁶*, Shannon W. Boettcher¹²³*  

¹ Department of Chemical & Biomolecular Engineering and Department of Chemistry, University of California, Berkeley  
² Energy Storage and Distributed Resources Division, Lawrence Berkeley National Laboratory  
³ Department of Chemistry and Biochemistry and the Oregon Center for Electrochemistry, University of Oregon  
⁴ Department of Chemistry and Biochemistry, University of California, Santa Barbara  
⁵ Chemical Sciences Division, Lawrence Berkeley National Laboratory  
⁶ Advanced Light Source, Lawrence Berkeley National Laboratory  

---

## Scientific Scope

These scripts implement numerical models describing charge transport and interfacial reaction kinetics in **semiconductor | catalyst | electrolyte** photoelectrochemical (PEC) systems. The models are used to compute steady-state catalytic current densities as a function of applied potential for wide-bandgap semiconductor photoelectrodes (e.g., SrTiO₃).

The simulations follow and extend the adaptive junction framework developed in prior work¹–³, incorporating:
- Thermionic emission–based carrier injection from semiconductor bands
- Catalyst–electrolyte Butler–Volmer kinetics
- Self-consistent determination of catalyst energetics under steady-state operation

---

## Repository Contents

### 1. `Adaptive-Junction-Python-Script.py`
Implements the **adaptive junction model** used in the main text.

**Key features:**
- Evaluates the steady-state catalyst–solution current density (`Jcatsol`) as a function of applied potential (`V_app`)
- Includes contributions from:
  - Valence-band hole current (`Jvbcat`)
  - Conduction-band electron current (`Jcbcat`)
  - Catalyst–electrolyte current (`Jcatsol`)
- Exchange current densities are estimated using thermionic emission theory with a small reverse recombination flux
- A nested nonlinear solver (Brent’s method via `scipy.optimize.root_scalar`) self-consistently determines the catalyst energy level (`Ecat`) such that net current balance is satisfied

This model captures **adaptive barrier evolution**, where interfacial energetics shift in response to operating conditions. A more complete treatment including surface-state charging and explicit band-edge motion is discussed in prior work and related extensions (see Ref. 3).

---

### 2. `Buried-Junction-Python-Script.py`
Implements a **buried junction model** for comparison and conceptual clarity.

**Key features:**
- Computes catalytic current density (`J_cat`) as a function of applied voltage (`V_app`)
- Uses thermionic emission and detailed balance for charge transfer
- Solves the steady-state current balance numerically using `scipy.optimize.fsolve`
- Catalyst overpotential is determined via a Butler–Volmer–type relation

This script represents a simplified junction treatment consistent with earlier adaptive-junction analyses¹² and is useful for benchmarking and interpretation.

---

## Dependencies

Tested with:
- OS Windows 11 Home
  
- Python **3.13.9**
- NumPy **2.3.3**
- SciPy **1.16.2**
- Matplotlib **3.20.6**
- Pandas **2.3.3**

The code is OS-agnostic and should run on any system with a compatible Python installation.
All dependencies are available via standard Python scientific distributions.

---
### Non-standard hardware
No non-standard hardware is required.  
The simulations run on a standard desktop or laptop CPU.

---

### Installation instructions
1. Ensure Python 3.13.9 (or compatible) is installed.
2. Clone or download this repository.
3. Install required packages:

```bash
pip install numpy scipy matplotlib pandas
```

Expected install time on a "normal" desktop computer is <1  min

---

### Included demo data

The simulations are fully self-contained and generate their own simulated datasets internally.
No external input files are required.

### Demo instructions

Run either script directly:

python Adaptive-Junction-Python-Script.py
or
python Buried-Junction-Python-Script.py

---

### Expected output

Numerical solution of steady-state catalytic current density as a function of applied voltage

A plotted current–voltage curve displayed on screen:

Jcatsol vs V_app for the adaptive junction model

J_cat vs V_app for the buried junction model

Representative output includes smooth current–voltage curves consistent with those shown in the manuscript figures.

---

### Expected runtime for demo

On a normal desktop or laptop computer: < 30 seconds per script.

---

### Reproducibility Notes

All constants, parameters, and equations are explicitly defined in code.
The simulations reproduce qualitative and quantitative trends reported in the manuscript.
The code represents a physics-based model rather than a device-scale engineering simulator.

## References:

1	Mills, T. J., Lin, F. & Boettcher, S. W. Theory and simulations of electrocatalyst-coated semiconductor electrodes for solar water splitting. Phys Rev Lett 112, 148304, doi:10.1103/PhysRevLett.112.148304 (2014).  
2	Nellist, M. R., Laskowski, F. A. L., Lin, F., Mills, T. J. & Boettcher, S. W. Semiconductor–Electrocatalyst Interfaces: Theory, Experiment, and Applications in Photoelectrochemical Water Splitting. Acc. Chem. Res. 49, 733-740, doi:10.1021/acs.accounts.6b00001 (2016).  
3	Mills, T. J. et al. The role of surface states in electrocatalyst-modified semiconductor photoelectrodes: Theory and simulations. arXiv e-prints, arXiv:1707.03112, doi:10.48550/arXiv.1707.03112 (2017).  

---

## Usage
### Citation

If you use this software, please cite:
A. Kaufman, K. Wheeler, E. J. Crumlin, S. W. Boettcher,
Cooperative Adaptive Junctions Govern Overall Photoelectrochemical Water Splitting,
Nature Catalysis (2026).

### Instructions for Use

How to run the software on your own data
The scripts are parameter-driven and may be adapted by modifying physical constants and material parameters defined at the top of each file, including:
-Bandgap energy
-Barrier heights
-Exchange current densities
-Carrier concentrations
-Applied voltage range

Users can:
-Adjust material parameters directly in the script
-Re-run the simulation
-Generate updated current–voltage curves

The code is intended for research and educational use, enabling exploration of adaptive junction behavior in semiconductor–catalyst photoelectrochemical systems.

Each script is self-contained and may be executed directly:

```bash
python Adaptive-Junction-Python-Script.py
```
or
```bash
python Buried-Junction-Python-Script.py
```
