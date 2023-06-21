import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import altair as alt
from wordcloud import WordCloud




coursera2 = pd.read_csv("data\coursera2.csv")


edx = pd.read_csv("data\edx_nuevo.csv")


udemy = pd.read_csv("data\\udemy_nuevo.csv", encoding="utf-8")



#Gráfico 1

# Calcular el promedio anual del rating
promedio_rating_anual = coursera2.groupby('year')['rating'].mean()

# Configurar el gráfico de línea
fig, ax = plt.subplots()
ax.plot(promedio_rating_anual.index, promedio_rating_anual.values, color='purple', label='Promedio de Rating')

# Ajustar un polinomio de grado 1 (lineal)
fit = np.polyfit(promedio_rating_anual.index, promedio_rating_anual.values, 1)
fit_fn = np.poly1d(fit)

# Agregar la curva de tendencia al gráfico
ax.plot(promedio_rating_anual.index, fit_fn(promedio_rating_anual.index), color='orange', linestyle='--', label='Curva de Tendencia')

# Configurar etiquetas y título del gráfico
ax.set_xlabel('Año')
ax.set_ylabel('Promedio de Rating')
ax.set_title('Promedio anual del rating en Coursera')
ax.set_xticks(promedio_rating_anual.index)
ax.set_xticklabels(promedio_rating_anual.index, rotation=45)
ax.legend()

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.markdown("***")

#Gráfico 2

# Agrupar por nombre de curso y calcular el promedio de los ratings
rating_promedio_por_curso = coursera2.groupby('name')['rating'].mean()

# Obtener los top 5 cursos con mejores promedios de rating
top_cursos_nombres = rating_promedio_por_curso.nlargest(5)

# Ordenar los datos de mayor a menor
top_cursos_nombres = top_cursos_nombres.sort_values(ascending=True)

# Configurar el gráfico de barras horizontal
fig, ax = plt.subplots()
ax.barh(top_cursos_nombres.index, top_cursos_nombres.values, color='purple')

# Agregar etiquetas de promedio de rating en las barras
for i, v in enumerate(top_cursos_nombres.values):
    ax.text(v + 0.1, i, f'{v:.2f}', color='black')

# Configurar etiquetas y título del gráfico
ax.set_xlabel('Promedio de Rating')
ax.set_ylabel('Nombre del Curso')
ax.set_title('Top 5 Cursos con mejores promedios de rating en Coursera')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

st.markdown("***")

#Gráfico 3

# Agrupar por institución y calcular el promedio de los ratings
rating_promedio_por_institucion = coursera2.groupby('institution')['rating'].mean()

# Ordenar de forma descendente y obtener el top 10
top_10_instituciones = rating_promedio_por_institucion.nlargest(10).sort_values(ascending=True)

# Configurar el gráfico de barras horizontal
fig, ax = plt.subplots()
ax.barh(top_10_instituciones.index, top_10_instituciones.values, color='purple')

# Configurar etiquetas y título del gráfico
ax.set_xlabel('Rating promedio')
ax.set_ylabel('Institución')
ax.set_title('Top 10 instituciones con mayor rating promedio en Coursera')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)