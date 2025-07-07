# 🧬 Automatic Detection of Polyproline II (PPII) Helices in Proteins

This repository contains a Python module for the automatic detection of polyproline II (PPII) helices in protein structures. The system integrates directly into **PyMOL**, automating a process that, until now, was performed manually through visual inspection and structural measurements.

---

## 🔍 Extended Description

The identification of PPII helices is a challenge in protein structural analysis. These conformations are not easily recognized by conventional bioinformatics tools, as they require the evaluation of specific geometric criteria such as the φ (phi) and ψ (psi) dihedral angles, as well as potential non-canonical Cα–H···O hydrogen bonds.

The **PPIIMoL** module automates this process within **PyMOL**, a widely used environment in structural biochemistry. It has been developed in Python and includes an intuitive graphical user interface (GUI) built with Tkinter to facilitate its use by both experienced researchers and newcomers to structural bioinformatics.

### 🚀 Key Features

- 📂 **Load PDB files** and preprocess the structure (remove solvents, add hydrogens).  
- 📐 **Automatically calculate φ and ψ angles** for each residue.  
- 🔍 **Identify segments compatible with PPII helices** using user-defined criteria.  
- 🧪 **Optionally detect non-canonical Cα–H···O hydrogen bonds.**  
- 🎨 **Direct visualization in PyMOL**, with highlighted segments, distance lines, and pseudoatoms for key atoms.  
- ⚙️ **Advanced configuration options**: adjust angular tolerances, set allowed residue jumps, and define Cα–H···O angle ranges.  
- 💾 **Export results** to CSV or PDB files for further analysis.

The module has been validated with real structures, such as the model protein **3BOG**, used as a test case.

---

## 📦 Requirements

- Python 3.x  
- PyMOL (with scripting support)  
- Standard Python libraries: `tkinter`, `os`, `csv`

---

## 🚀 How to Use

1. Clone this repository or download the `PPIIMoL.py` file.  
2. Open PyMOL.  
3. Run the module from the PyMOL console:  

   ```pymol
   run PPIIMoL.py
A graphical interface will appear, allowing you to run all module functions interactively for the detection and analysis of PPII helices.

🧪 Example
The model protein 3BOG is used as a test case. When the module is executed, six previously documented PPII helices are identified, labels are added to the 3D structure, and dihedral angle values are exported to a text file.

📘 Base Publication
Segura Rodríguez, C. M., & Laurents, D. V. (2024). Architectonic principles of polyproline II helix bundle protein domains. Archives of Biochemistry and Biophysics. https://doi.org/10.1016/j.abb.2024.109981

👩‍💻 Author
Developed by Silvia Enma Rodríguez Fernández as part of her Bachelor’s Thesis in Computer Engineering (UNIR), in collaboration with IQF-CSIC.

📧 Contact: [optional: add your GitHub profile or professional email]

📄 License
This project is licensed under the GNU General Public License v3.0 (GPLv3).

This means that anyone can use, study, modify, and redistribute the code, provided that derivative works retain the same license. The GPLv3 ensures that this software and its future adaptations remain free and open, preventing proprietary appropriation.

🔗 Read the full GPLv3 license
