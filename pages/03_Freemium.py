import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import altair as alt


coursera2 = pd.read_csv("data\coursera2.csv")


edx = pd.read_csv("data\edx_nuevo.csv")


udemy = pd.read_csv("data\\udemy_nuevo.csv", encoding="utf-8")



cursos_gratuitos = udemy[udemy['is_paid'] == False]
cursos_pagados = udemy[udemy['is_paid'] == True]

inscriptos_gratuitos = cursos_gratuitos['num_subscribers'].sum()


inscriptos_pagados = cursos_pagados['num_subscribers'].sum()


#Gráfico1

tasa_conversion = round((inscriptos_pagados / inscriptos_gratuitos) * 100, 2)

# st.subheader("Tasa de conversión")

conversion_text = f"{tasa_conversion}%"

style = """
    <style>
        .info-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            background-color: #e8f4f8;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
    </style>
"""
st.markdown(style, unsafe_allow_html=True)

st.markdown(f'<div class="info-box"><div>Tasa de conversión</div><div>{conversion_text}</div></div>', unsafe_allow_html=True)

st.markdown("***")

#Gráfico2

# Definir los datos y etiquetas para el gráfico de pie
datos = [inscriptos_pagados, inscriptos_gratuitos]
etiquetas = ['Pagados', 'Gratuitos']
colores = ['lightblue', 'lightgreen']

# Formatear los números de inscritos con separadores de miles
inscriptos_gratuitos_formateados = "{:,.0f}".format(inscriptos_gratuitos)
inscriptos_pagados_formateados = "{:,.0f}".format(inscriptos_pagados)

# Generar la leyenda
leyenda = f"Inscriptos pagados: {inscriptos_pagados_formateados}\nInscriptos gratuitos: {inscriptos_gratuitos_formateados}"

# Crear el gráfico de pie
fig, ax = plt.subplots()
ax.pie(datos, labels=etiquetas, colors=colores, autopct='%1.1f%%')
ax.set_title('Porcentaje de cursos pagados y gratuitos (Udemy)')
ax.legend(title='Inscriptos', loc='center', bbox_to_anchor=(0.5, -0.1), shadow=True, edgecolor='black',
           facecolor='white', frameon=True, fancybox=True, borderaxespad=0.)
ax.text(1.05, 0.08, leyenda, fontsize=10)
ax.axis('equal')  # Hace que el gráfico sea circular

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.markdown("***")


#Gráfico3

# Filtrar los cursos gratuitos
cursos_gratuitos = udemy[udemy['is_paid'] == False]

# Contar el número de cursos gratuitos por subject
conteo_subjects = cursos_gratuitos['subject'].value_counts()

# Ordenar los resultados de mayor a menor
conteo_subjects = conteo_subjects.sort_values(ascending=True)

# Crear una paleta de colores personalizada con tonos oscuros
paleta_colores = sns.color_palette("deep", len(conteo_subjects))

# Ordenar los colores en función del conteo de cursos gratuitos
colores_ordenados = [paleta_colores[i] for i in range(len(conteo_subjects))]

# Crear la figura con dos subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Graficar los cursos gratuitos por área de conocimiento
axs[0].barh(conteo_subjects.index, conteo_subjects.values, color=colores_ordenados, height=0.5)
axs[0].set_xlabel('Número de Cursos Gratuitos')
axs[0].set_ylabel('Áreas')
axs[0].set_title('Cursos gratuitos por área de conocimiento')

# Filtrar los cursos pagados
cursos_pagados = udemy[udemy['is_paid'] == True]

# Contar el número de cursos pagados por subject
conteo_subjects_pagados = cursos_pagados['subject'].value_counts()

# Ordenar los resultados de mayor a menor
conteo_subjects_pagados = conteo_subjects_pagados.sort_values(ascending=True)

# Graficar los cursos pagados por área de conocimiento
axs[1].barh(conteo_subjects_pagados.index, conteo_subjects_pagados.values, color=colores_ordenados, height=0.5)
axs[1].set_xlabel('Número de Cursos Pagados')
axs[1].set_ylabel('Áreas')
axs[1].set_title('Cursos pagados por área de conocimiento')

# Ajustar los espacios entre los subplots
plt.tight_layout()

# Mostrar los gráficos en Streamlit
st.pyplot(fig)





