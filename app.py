import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Calculadora de Derivadas", layout="centered")

# Título
st.title("🧮 Calculadora de Derivadas con Límites y Gráfica")

# Entrada de usuario
func_input = st.text_input("Ingresa una función en términos de x:", value="x**2")
var = sp.Symbol('x')

# Cálculo paso a paso
if func_input:
    try:
        func = sp.sympify(func_input)
        st.latex(f"f(x) = {sp.latex(func)}")

        # Derivada simbólica
        derivada = sp.diff(func, var)
        st.subheader("📘 Paso a Paso - Derivación")
        steps = sp.calculus.util.function_range(func, var, sp.S.Reals)
        st.markdown("*1. Derivada simbólica:*")
        st.latex(f"f'(x) = {sp.latex(derivada)}")

        # Límite opcional
        st.subheader("📐 Cálculo de Límite")
        calc_limit = st.checkbox("¿Deseas calcular un límite?")
        if calc_limit:
            punto = st.number_input("Valor de x hacia el cual tiende:", value=1.0)
            direccion = st.selectbox("Dirección del límite", ("Ambos lados", "Izquierda (-)", "Derecha (+)"))

            if direccion == "Ambos lados":
                limite = sp.limit(func, var, punto)
            elif direccion == "Izquierda (-)":
                limite = sp.limit(func, var, punto, dir='-')
            else:
                limite = sp.limit(func, var, punto, dir='+')

            st.latex(f"\\lim_{{x \\to {punto}}} f(x) = {sp.latex(limite)}")

        # Gráfica
        st.subheader("📊 Gráfica de la función y su derivada")

        x_vals = np.linspace(-10, 10, 400)
        f_lambd = sp.lambdify(var, func, 'numpy')
        d_lambd = sp.lambdify(var, derivada, 'numpy')

        fig, ax = plt.subplots()
        ax.plot(x_vals, f_lambd(x_vals), label="f(x)", linewidth=2)
        ax.plot(x_vals, d_lambd(x_vals), label="f'(x)", linestyle='--', color='red')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title("Función y su Derivada")
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error al procesar la función: {e}")
