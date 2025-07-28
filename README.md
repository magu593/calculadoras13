# 🧮 Calculadora de Derivadas con Límites y Gráfica

Esta es una aplicación interactiva desarrollada con Streamlit que permite:
- Calcular la derivada simbólica de una función en términos de `x`.
- Calcular el límite de la función en un punto (opcional).
- Visualizar gráficamente la función original y su derivada.

## 🚀 Requisitos

Necesitas tener Python 3.7 o superior instalado. Luego, instala las dependencias con:

O manualmente:

```bash
pip install streamlit sympy matplotlib numpy
```

## 📂 Cómo usar

1. Clonar este repositorio o descargar el archivo `calculadora_derivadas.py`.

2. Abrir una terminal en la carpeta del proyecto y ejecutar:

```bash
streamlit run calculadora_derivadas.py
```

3. Se abrirá automáticamente tu navegador con la aplicación web.

## ✏️ Instrucciones de uso

* En el campo de texto, ingresar una función válida en términos de `x`. Ejemplos:

  * `x**2`
  * `sin(x)`
  * `exp(-x)*cos(x)`
  * `ln(x)`
  * `1/(x+2)`
* Si deseas calcular un límite, marca la casilla correspondiente y proporciona:

  * El valor hacia el cual tiende `x`.
  * La dirección del límite (ambos lados, izquierda o derecha).
* Visualiza la gráfica de la función original y su derivada en el mismo plano.

## 🛠️ Tecnologías utilizadas

* [Streamlit](https://streamlit.io/)
* [SymPy](https://www.sympy.org/)
* [Matplotlib](https://matplotlib.org/)
* [NumPy](https://numpy.org/)


