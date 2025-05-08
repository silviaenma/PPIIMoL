# Detección automática de hélices de poliprolina II (PPII) en proteínas

Este repositorio contiene un módulo desarrollado en Python para la detección automática de hélices de tipo poliprolina II (PPII) en estructuras proteicas. El sistema se integra directamente en PyMOL y permite automatizar un proceso que, hasta ahora, se realizaba de forma manual mediante inspección visual y medición estructural.

## 🔍 Descripción ampliada

La identificación de hélices PPII representa un reto dentro del análisis estructural de proteínas, ya que estas conformaciones no se detectan automáticamente mediante herramientas bioinformáticas convencionales. Su reconocimiento requiere evaluar criterios geométricos como los ángulos diedros φ (phi) y ψ (psi), así como posibles enlaces de hidrógeno no canónicos.

Este módulo automatiza ese proceso dentro del entorno PyMOL, herramienta ampliamente usada por investigadores en bioquímica estructural. Entre sus funcionalidades:

- Carga de estructuras en formato PDB.
- Eliminación de solventes y adición de hidrógenos.
- Cálculo automático de ángulos φ y ψ.
- Identificación de tramos compatibles con hélices PPII.
- Detección opcional de enlaces de hidrógeno no canónicos.
- Visualización directa en PyMOL con colores y etiquetas.
- Interfaz gráfica sencilla mediante Tkinter.

Desarrollado en colaboración con el grupo del Instituto de Química-Física “Blas Cabrera” (IQF-CSIC), el módulo ha sido validado sobre estructuras reales como la proteína modelo 3BOG.

## 📦 Requisitos

- Python 3.x
- PyMOL (con soporte para scripting)
- Librerías estándar (`tkinter`, `os`)

## 🚀 Uso

1. Clona este repositorio o descarga el archivo `ppii_module.py`.
2. Abre PyMOL.
3. Ejecuta el módulo desde la consola de PyMOL con:

script_calculo_angulos_documentado # nombre provisional estoy todavía creándolo

4. Se abrirá una interfaz gráfica desde la cual pueden ejecutarse todas las funciones del módulo de forma interactiva.

## 🧪 Ejemplo de uso

La proteína modelo `3BOG` se utiliza como caso de prueba. Al ejecutarse el módulo, se identifican seis hélices PPII previamente documentadas, se generan etiquetas sobre la estructura tridimensional y se exportan los valores de ángulos diedros a un archivo de texto.

## 📘 Publicación base

Segura Rodríguez, C. M., & Laurents, D. V. (2024). *Architectonic principles of polyproline II helix bundle protein domains*. Archives of Biochemistry and Biophysics. https://doi.org/10.1016/j.abb.2024.109981

## 👩‍💻 Autora

Desarrollado por **Silvia Enma Rodríguez Fernández** como parte del Trabajo de Fin de Grado en Ingeniería Informática (UNIR), en colaboración con el IQF-CSIC, especialmente, con Cristian Moisés Segura Rodríguez.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Eres libre de utilizar, modificar y redistribuir el código, siempre que mantengas esta nota de licencia y cites el repositorio si lo usas en proyectos académicos o científicos.
