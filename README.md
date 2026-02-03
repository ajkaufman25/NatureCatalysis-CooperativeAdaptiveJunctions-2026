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

- Python **3.13.9**
- NumPy
- SciPy
- Matplotlib
- Pandas

All dependencies are available via standard Python scientific distributions.

---

## References:

1	Mills, T. J., Lin, F. & Boettcher, S. W. Theory and simulations of electrocatalyst-coated semiconductor electrodes for solar water splitting. Phys Rev Lett 112, 148304, doi:10.1103/PhysRevLett.112.148304 (2014).  
2	Nellist, M. R., Laskowski, F. A. L., Lin, F., Mills, T. J. & Boettcher, S. W. Semiconductor–Electrocatalyst Interfaces: Theory, Experiment, and Applications in Photoelectrochemical Water Splitting. Acc. Chem. Res. 49, 733-740, doi:10.1021/acs.accounts.6b00001 (2016).  
3	Mills, T. J. et al. The role of surface states in electrocatalyst-modified semiconductor photoelectrodes: Theory and simulations. arXiv e-prints, arXiv:1707.03112, doi:10.48550/arXiv.1707.03112 (2017).  

---

## Usage

Each script is self-contained and may be executed directly:

```bash
python Adaptive-Junction-Python-Script.py
python Buried-Junction-Python-Script.py
