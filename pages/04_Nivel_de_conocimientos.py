import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import altair as alt
from wordcloud import WordCloud



coursera2 = pd.read_csv("data\coursera2.csv")


edx = pd.read_csv("data\edx_nuevo.csv")


udemy = pd.read_csv("data\\udemy_nuevo.csv", encoding="utf-8")


#3

# Calcular el porcentaje de cursos ofertados por nivel en Udemy
udemy_counts = udemy['level'].value_counts()
udemy_percentages = (udemy_counts / udemy_counts.sum()) * 100

# Calcular el porcentaje de cursos ofertados por nivel en EDX
edx_counts = edx['Level'].value_counts()
edx_percentages = (edx_counts / edx_counts.sum()) * 100

# Ajustar el tamaño de la figura y crear los subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Gráfico de Udemy (izquierda)
udemy_sorted = udemy_percentages.sort_values(ascending=True)
axs[0].barh(udemy_sorted.index, udemy_sorted.values, color='#4682B4', height=0.6)
axs[0].set_xlabel('Porcentaje (%)')
axs[0].set_ylabel('Nivel')
axs[0].set_title('Porcentaje de cursos ofertados (Udemy)')
axs[0].xaxis.set_major_formatter('{:.1f}%'.format)  # Formato de porcentaje en el eje x

# Gráfico de EDX (derecha)
edx_sorted = edx_percentages.sort_values(ascending=True)
axs[1].barh(edx_sorted.index, edx_sorted.values, color='green', height=0.4)
axs[1].set_xlabel('Porcentaje (%)')
axs[1].set_ylabel('Nivel')
axs[1].set_title('Porcentaje de cursos ofertados (EDX)')
axs[1].xaxis.set_major_formatter('{:.1f}%'.format)  # Formato de porcentaje en el eje x

# Ajustar los subplots
plt.tight_layout()

# Mostrar los gráficos en Streamlit
st.pyplot(fig)

st.markdown("***")

#1
# Concatenar todos los nombres en una sola cadena de texto
text = ' '.join(edx['title'].astype(str))

# Crear el objeto de WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar la WordCloud en los ejes
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
ax.set_title('WordCloud de los nombres de los cursos de edX')

# Mostrar la figura en Streamlit
st.pyplot(fig)

st.markdown("***")
#Gráfico 2

# Agrupar por idioma y calcular la suma de n_enrolled
enrolled_by_language = edx.groupby('language')['n_enrolled'].sum().reset_index()

# Ordenar en orden descendente por n_enrolled
enrolled_by_language = enrolled_by_language.sort_values('n_enrolled', ascending=False)

# Obtener el top 2 idiomas con mayor n_enrolled
top_2_languages = enrolled_by_language.head(2).copy()

# Calcular los porcentajes de n_enrolled
total_enrolled = top_2_languages['n_enrolled'].sum()
top_2_languages['percentage'] = (top_2_languages['n_enrolled'] / total_enrolled) * 100

# Configurar los colores
colors = ['steelblue', '#FF8C00']

# Crear el gráfico de pie
fig, ax = plt.subplots()
ax.pie(top_2_languages['percentage'], labels=top_2_languages['language'], colors=colors, autopct='%1.1f%%')
ax.axis('equal')  # Aspecto circular
ax.set_title('Los 2 idiomas con más suscriptores (EDX)')

# Crear la leyenda con el número de suscriptores
legend_labels = [f"{lang} ({enrolled:,} suscriptores)" for lang, enrolled in zip(top_2_languages['language'], top_2_languages['n_enrolled'])]
ax.legend(legend_labels, loc='lower right', bbox_to_anchor=(1, 0), fontsize='small')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)



