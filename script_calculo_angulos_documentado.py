# Importación de módulos necesarios
from pymol import cmd, stored  # Módulos internos de PyMOL
import tkinter as tk  # Interfaz gráfica
from tkinter import filedialog, messagebox  # Diálogos estándar
from tkinter.scrolledtext import ScrolledText  # Caja de texto con scroll
import os  # Para manejo de archivos

# Variable global para almacenar la ruta del archivo PDB cargado
pdb_file = None

# Función para seleccionar y cargar un archivo PDB
def seleccionar_archivo():
    global pdb_file
    pdb_file = filedialog.askopenfilename(
        title="Selecciona un archivo PDB",
        filetypes=[("Archivos PDB", "*.pdb")]
    )
    if pdb_file:
        cmd.reinitialize()  # Reinicia PyMOL (borra todo lo anterior)
        cmd.load(pdb_file, "proteina")  # Carga el PDB con el nombre "proteina"
        cmd.hide("everything", "proteina")  # Oculta todas las representaciones
        cmd.show("licorice", "proteina")  # Muestra la proteína en estilo licorice
        messagebox.showinfo("Archivo cargado", f"Se cargó:\n{pdb_file}")

# Añade hidrógenos a toda la proteína
def anadir_hidrogenos():
    if not pdb_file:
        messagebox.showwarning("Advertencia", "Primero selecciona un archivo.")
        return
    cmd.h_add("all")  # Añade hidrógenos
    cmd.sort("all extend 1")  # Ordena átomos y mejora conectividad
    cmd.show("licorice", "all")  # Asegura que se muestren los hidrógenos
    messagebox.showinfo("Hidrógenos", "Hidrógenos añadidos y mostrados como licorice.")

# Elimina moléculas de solvente (por ejemplo, agua)
def eliminar_solventes():
    cmd.remove("solvent")
    messagebox.showinfo("Solventes", "Solventes eliminados.")

# Oculta todas las cadenas laterales, dejando solo el esqueleto peptídico (backbone)
def ocultar_side_chains():
    cmd.hide("everything", "proteina and not name N+CA+C+O")
    messagebox.showinfo("Backbone", "Cadenas laterales ocultas (solo backbone).")

# Crea un nuevo objeto en PyMOL por cada cadena encontrada en la proteína cargada
def separar_cadenas():
    stored.chains = []  # Lista temporal
    cmd.iterate("proteina", "stored.chains.append(chain)")  # Guarda todas las cadenas
    for cadena in set(stored.chains):  # Para cada cadena única
        nuevo_objeto = f"cadena_{cadena}"
        cmd.create(nuevo_objeto, f"proteina and chain {cadena}")  # Crea nuevo objeto por cadena
    messagebox.showinfo("Separación", "Cadenas separadas.")

# Calcula y guarda ángulos phi/psi para cada cadena separada en un archivo de texto
def guardar_angulos_phi_psi():
    salida = ""
    objetos = cmd.get_object_list()
    for obj in objetos:
        if obj.startswith("cadena_"):
            phipsi = cmd.get_phipsi(obj)
            if phipsi:
                salida += f"\nÁngulos phi/psi de {obj}:\n"
                for resi, angles in phipsi.items():
                    salida += f"  Residuo {resi}: phi={angles[0]:.2f}°, psi={angles[1]:.2f}°\n"
            else:
                salida += f"No se pudieron calcular ángulos para {obj}.\n"
    
    if salida:
        ruta_archivo = os.path.join(os.getcwd(), "angulos_phi_psi.txt")
        with open(ruta_archivo, "w") as f:
            f.write(salida)
        messagebox.showinfo("Ángulos", f"Los ángulos phi/psi se guardaron en '{ruta_archivo}'.")
    else:
        messagebox.showinfo("Ángulos", "No hay datos de ángulos.")

# Muestra los ángulos phi/psi en una ventana con scroll, sin guardarlos
def mostrar_angulos_phi_psi():
    salida = ""
    objetos = cmd.get_object_list()
    for obj in objetos:
        if obj.startswith("cadena_"):
            phipsi = cmd.get_phipsi(obj)
            if phipsi:
                salida += f"\nÁngulos phi/psi de {obj}:\n"
                for resi, angles in phipsi.items():
                    salida += f"  Residuo {resi}: phi={angles[0]:.2f}°, psi={angles[1]:.2f}°\n"
            else:
                salida += f"No se pudieron calcular ángulos para {obj}.\n"
    
    if salida:
        angulos_window = tk.Toplevel()
        angulos_window.title("Ángulos phi/psi")
        text_area = ScrolledText(angulos_window, width=100, height=30)
        text_area.insert(tk.END, salida)
        text_area.pack()
        text_area.config(state=tk.DISABLED)  # Solo lectura
    else:
        messagebox.showinfo("Ángulos", "No hay datos de ángulos.")

# Crea e inicia la ventana principal con botones para cada función
def lanzar_interfaz():
    root = tk.Tk()
    root.title("Análisis de Proteína en PyMOL")
    
    # Botones de la interfaz, uno por cada función
    tk.Button(root, text="Seleccionar archivo PDB", command=seleccionar_archivo, width=40).pack(pady=5)
    tk.Button(root, text="Añadir hidrógenos", command=anadir_hidrogenos, width=40).pack(pady=5)
    tk.Button(root, text="Eliminar solventes", command=eliminar_solventes, width=40).pack(pady=5)
    tk.Button(root, text="Ocultar cadenas laterales", command=ocultar_side_chains, width=40).pack(pady=5)
    tk.Button(root, text="Separar cadenas", command=separar_cadenas, width=40).pack(pady=5)
    tk.Button(root, text="Calcular ángulos phi/psi y guardar", command=guardar_angulos_phi_psi, width=40).pack(pady=5)
    tk.Button(root, text="Ver ángulos phi/psi", command=mostrar_angulos_phi_psi, width=40).pack(pady=5)
    tk.Button(root, text="Salir", command=root.destroy, width=40).pack(pady=10)

    root.mainloop()

# Ejecutar interfaz al cargar el script
lanzar_interfaz()
