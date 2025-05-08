# Detección automática de hélices de poliprolina II (PPII) en proteínas

Este repositorio contiene un módulo desarrollado en Python para la detección automática de hélices de tipo poliprolina II (PPII) en estructuras proteicas. El sistema se integra directamente en PyMOL y permite automatizar un proceso que, hasta ahora, se realizaba de forma manual mediante inspección visual y medición estructural.

## 🔬 Características principales

- Carga de estructuras en formato PDB.
- Eliminación de solventes y adición de hidrógenos.
- Cálculo automático de ángulos diedros φ y ψ.
- Detección de regiones compatibles con la conformación PPII.
- Identificación opcional de enlaces de hidrógeno no canónicos.
- Visualización directa en PyMOL con colores y etiquetas.
- Interfaz gráfica sencilla (Tkinter).

## 📦 Requisitos

- PyMOL (versión con soporte para scripting)
- Python 3.x
- Librerías estándar (`tkinter`, `os`)

## 🚀 Uso

1. Clonar el repositorio o descargar el archivo `.py`.
2. Abrir PyMOL.
3. Ejecutar el módulo desde la consola de PyMOL:
