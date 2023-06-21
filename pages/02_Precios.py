import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import altair as alt



coursera2 = pd.read_csv("data\coursera2.csv")


edx = pd.read_csv("data\edx_nuevo.csv")


udemy = pd.read_csv("data\\udemy_nuevo.csv", encoding="utf-8")




# Obtener los valores de la columna "_price_numeric"
precios_edx = edx['price_numeric']

# Filtrar los cursos pagados de Udemy
cursos_pagados = udemy[udemy['is_paid'] == True]

# Obtener la columna de precios de Udemy
precios_udemy = cursos_pagados['price']





#Gráfico 1

# Obtener los valores de la columna "_price_numeric"
precios_edx = edx['price_numeric']

# Ajustar el tamaño de los gráficos
fig, axs = plt.subplots(1, 2, figsize=(15, 7.5))

# Crear el histograma de EDX
axs[0].hist(precios_edx, bins=20, edgecolor='black', color='green')
axs[0].set_title('Distribución de precios (EDX)', fontsize=16)
axs[0].set_xlabel('Precios', fontsize=14)
axs[0].set_ylabel('Frecuencia', fontsize=14)

# Filtrar los cursos pagados de Udemy
cursos_pagados = udemy[udemy['is_paid'] == True]

# Obtener la columna de precios de Udemy
precios_udemy = cursos_pagados['price']

# Crear el histograma de Udemy
axs[1].hist(precios_udemy, bins=20, edgecolor='black')
axs[1].set_title('Distribución de Precios (Udemy)', fontsize=16)
axs[1].set_xlabel('Precios', fontsize=14)
axs[1].set_ylabel('Frecuencia', fontsize=14)

# Ajustar la disposición de los subplots y los espacios entre ellos
plt.tight_layout(pad=3.0)

# Ajustar el tamaño de las fuentes de los ejes x e y
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Evitar que Streamlit restrinja el tamaño de los gráficos
st.set_option('deprecation.showPyplotGlobalUse', False)

# Mostrar los histogramas en Streamlit
st.pyplot(fig)

st.markdown("***")

#Gráfico 2



# Calcular el promedio de precios por año
promedio_precios_por_año = udemy.groupby('year')['price'].mean()


# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los promedios de precios por año en un gráfico de línea
ax.plot(promedio_precios_por_año.index, promedio_precios_por_año.values, marker='o')

# Establecer las etiquetas de los ejes y el título del gráfico
ax.set_xlabel('Año')
ax.set_ylabel('Promedio de precios en dólares')
ax.set_title('Promedio de precios por año (Udemy)')

# Habilitar las grillas
ax.grid(True)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.markdown("***")

cursos_gratuitos = udemy[udemy['is_paid'] == False]
cursos_pagados = udemy[udemy['is_paid'] == True]

inscriptos_gratuitos = cursos_gratuitos['num_subscribers'].sum()
print(inscriptos_gratuitos )

inscriptos_pagados = cursos_pagados['num_subscribers'].sum()
print(inscriptos_pagados)



#Gráfico 3

# Filtrar los cursos pagados
cursos_pagados = udemy[udemy['is_paid'] == True]

# Crear la tabla pivot con el precio y el número de inscriptos pagados
tabla_pivot = cursos_pagados.pivot_table(index='price', values='num_subscribers', aggfunc='sum')

# Ordenar los resultados en orden descendente
tabla_pivot = tabla_pivot.sort_values('num_subscribers', ascending=False)

# Obtener los precios ordenados de mayor a menor número de inscriptos pagados
precios_ordenados = tabla_pivot.index

# Graficar la tabla pivot en un gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
tabla_pivot.plot(kind='bar', ax=ax)
ax.set_xlabel('Precio')
ax.set_ylabel('Número de inscriptos pagados')
ax.set_title('Precios con más inscriptos pagados (Udemy)')
ax.set_xticklabels(precios_ordenados, rotation=45)  # Personalizar las etiquetas del eje x

# Añadir una etiqueta en el eje y para explicar la escala
max_value = tabla_pivot['num_subscribers'].max()
ax.annotate(f'Máximo: {max_value}', xy=(0, max_value), xytext=(0, max_value * 1.1),
            arrowprops=dict(facecolor='black', arrowstyle='->'))

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


st.markdown("El número de cursos pagados de 20 dólares supera en un 181.36 por ciento a los cursos pagados de 200$.")



