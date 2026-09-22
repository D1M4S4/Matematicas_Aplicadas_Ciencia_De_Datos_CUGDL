# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo>=0.19.0",
#     "matplotlib",
#     "numpy",
#     "pandas",
#     "scipy",
#     "seaborn",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium", app_title="Repaso: Student Performance")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Actividad: Análisis Exploratorio y Distribución Gaussiana
    ## Matemáticas Aplicadas a Ciencia de Datos


    **Licenciatura en Ciencia de Datos e Inteligencia Artificial**

    Actividad de repaso para el examen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Contexto

    Vamos a utilizar el dataset **Student Performance** que contiene información sobre estudiantes de matemáticas en dos escuelas portuguesas. El dataset incluye variables demográficas, sociales y académicas, así como sus calificaciones finales.

    **Variables principales:**
    - `G1`: Calificación del primer periodo (0-20)
    - `G2`: Calificación del segundo periodo (0-20)
    - `G3`: Calificación final (0-20)
    - `studytime`: Tiempo de estudio semanal (1: <2hrs, 2: 2-5hrs, 3: 5-10hrs, 4: >10hrs)
    - `absences`: Número de ausencias (0-93)
    - `age`: Edad del estudiante (15-22)
    - `failures`: Número de materias reprobadas anteriormente (0-4)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Preparación de los datos

    Importa las librerías necesarias y carga el dataset.

    Resuelve cada inciso en su celda de código y completa los espacios de *Respuesta* con tu interpretación.

    En marimo, utiliza nombres distintos para los resultados de cada inciso. Puedes reutilizar las variables que ya definiste en otras celdas.
    """)
    return


@app.cell
def _():
    # Importar librerías necesarias
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats

    return (pd,)


@app.cell
def _(mo, pd):
    # Cargar el dataset
    df = pd.read_csv(mo.notebook_dir() / "student-mat.csv", sep=";")
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Análisis Exploratorio de Datos

    ### 1.1 Medidas de Tendencia Central y Dispersión

    Para la variable **G3 (calificación final)**:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **a) Calcula la media, mediana y moda**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Calcula la desviación estándar, varianza y rango intercuartílico (IQR)**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Interpreta estos resultados: ¿Qué te dicen sobre el desempeño general de los estudiantes?**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.2 Visualización
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **a) Crea un histograma de la variable G3 con al menos 10 bins.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Crea un boxplot de G3. Identifica si existen outliers y menciona cuántos hay.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Crea un scatter plot entre G2 (eje x) y G3 (eje y). ¿Qué relación observas?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1.3 Análisis de Distribución
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **a) Observando el histograma de G3, ¿consideras que la distribución es aproximadamente simétrica, sesgada a la derecha o sesgada a la izquierda? Justifica tu respuesta**

    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Compara la media y la mediana de G3. ¿Qué te indica esta comparación sobre la simetría de los datos? (5 puntos)**

    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ## 2. Distribución Gaussiana

    ### 2.1 Ajuste de Distribución Normal

    Considera la variable **G3 (calificación final)**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **a) Estima los parámetros μ (media) y σ (desviación estándar) de una distribución normal que se ajuste a los datos de G3.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) Crea un gráfico que superponga:**
    - **El histograma normalizado (densidad) de G3**
    - **La curva de la distribución normal N(μ, σ²) con los parámetros estimados**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Crea un gráfico Q-Q (quantile-quantile plot) para evaluar qué tan bien se ajusta G3 a una distribución normal. ¿Los datos siguen aproximadamente una distribución normal? Justifica.**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2.2 Cálculo de Probabilidades

    Asumiendo que G3 sigue una distribución normal con los parámetros estimados en 2.1:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **a) ¿Cuál es la probabilidad de que un estudiante seleccionado al azar obtenga una calificación final mayor a 15?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) ¿Cuál es la probabilidad de que un estudiante obtenga una calificación entre 10 y 14?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) ¿Qué calificación representa el percentil 75? Es decir, ¿por debajo de qué calificación se encuentra el 75% de los estudiantes?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **d) Si se considera que un estudiante está "en riesgo" si su calificación está por debajo del percentil 25, ¿cuál es la calificación límite para estar en riesgo?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **e) ¿Cuál es la probabilidad de que un estudiante repruebe (G3 < 10)?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---

    ### 2.3 Interpretación y Aplicación
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **a) Basándote en el modelo gaussiano ajustado, si la escuela tiene 500 estudiantes, ¿aproximadamente cuántos estudiantes esperarías que obtengan una calificación mayor a 16?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **b) La escuela quiere implementar un programa de tutorías para el 20% de estudiantes con calificaciones más bajas. ¿Cuál debería ser la calificación de corte para seleccionar a estos estudiantes?**
    """)
    return


@app.cell
def _():
    # Escribe aquí tu código.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **c) Reflexiona: ¿Consideras que el modelo de distribución normal es apropiado para modelar las calificaciones de los estudiantes? ¿Qué limitaciones podría tener este modelo?**

    *Respuesta:*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Criterios de Evaluación

    - **Justificación matemática y estadística**: 50%
    - **Calidad del código y visualizaciones**: 25%
    - **Interpretación y análisis crítico**: 25%

    **Total: 100 puntos**
    """)
    return


if __name__ == "__main__":
    app.run()
