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




#Gráfico 1



cursos_gratuitos = udemy[udemy['is_paid'] == False]
cursos_pagados = udemy[udemy['is_paid'] == True]

inscriptos_gratuitos = cursos_gratuitos['num_subscribers'].sum()


inscriptos_pagados = cursos_pagados['num_subscribers'].sum()


income_by_year = (udemy['price'] * inscriptos_pagados).groupby(udemy['year']).sum()
formatted_income_by_year = income_by_year.apply(lambda x: '${:,.2f} millones'.format(x / 1000000))


# Formatear ingresos en millones con símbolo del dólar
formatted_income_by_year = income_by_year.apply(lambda x: '${:,.2f} millones'.format(x / 1000000))


# Crear el dataframe con los datos
data = pd.DataFrame({'Años': income_by_year.index.astype(int), 'Ingresos totales (en millones)': income_by_year.values})

# Crear el gráfico
fig, ax = plt.subplots()
income_by_year.plot(kind='line', marker='o', ax=ax)
ax.set_xlabel('Años')
ax.set_ylabel('Ingresos totales (en millones)')
ax.set_title('Ingresos totales por año (Udemy)')
ax.grid(True)

# Formatear el eje Y para mostrar los valores en millones
formatter = ticker.FuncFormatter(lambda x, pos: '${:,.0f}M'.format(x * 1e-6))
plt.gca().yaxis.set_major_formatter(formatter)

# Mostrar el gráfico en Streamlit
st.pyplot(fig)


#Gráfico 2




# cursos_gratuitos = udemy[udemy['is_paid'] == False]
# cursos_pagados = udemy[udemy['is_paid'] == True]

# inscriptos_gratuitos = cursos_gratuitos['num_subscribers'].sum()

# inscriptos_pagados = cursos_pagados['num_subscribers'].sum()

# # Calcular los ingresos totales por año
# income_by_year = (udemy['price'] * inscriptos_pagados).groupby(udemy['year']).sum()
# formatted_income_by_year = income_by_year.apply(lambda x: '${:,.2f} millones'.format(x / 1000000))

# #Mostramos los ingresos por año
# print(formatted_income_by_year)


#2


# Definir la función para mostrar los ingresos por año
def mostrar_ingresos_por_año():
    data = {
        'Año': ['2011', '2012', '2013', '2014', '2015', '2016', '2017'],
        'Ingresos (millones)': [2536.91, 15016.90, 88873.84, 194769.56, 555093.25, 689140.53, 442609.74]
    }

    df = pd.DataFrame(data)

    # Aplicar estilos CSS a la tabla
    table_style = """
    <style>
        table {
            border-collapse: collapse;
            width: 50%;
            border: 2px solid #0d47a1;
        }

        th, td {
            padding: 8px;
            text-align: left;
            border-bottom: 1px solid black;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
    """

    # Mostrar la tabla con los estilos personalizados
    st.markdown(table_style, unsafe_allow_html=True)
    st.table(df)

# Establecer el estilo del botón
button_style = """
<style>
    .blue-button {
        color: #0d47a1;
        font-weight: bold;
        border: 2px solid #0d47a1;
        border-radius: 5px;
        padding: 0.5em 1em;
    }
</style>
"""

# Mostrar el estilo del botón
st.markdown(button_style, unsafe_allow_html=True)

# Crear el botón "Ingresos por año" con el estilo personalizado
if st.button("Mostrar ingresos por año", key='ingresos_button'):
    mostrar_ingresos_por_año()


#3


# Calcular los ingresos totales por año
income_by_year = (udemy['price'] * inscriptos_pagados).groupby(udemy['year']).sum()
formatted_income_by_year = income_by_year.apply(lambda x: '${:,.2f} millones'.format(x / 1000000))

# Calcular el cambio porcentual de los ingresos totales entre un año y el siguiente
income_change = income_by_year.pct_change() * 100

# Crear una tabla con los cambios porcentuales y redondear los porcentajes a dos decimales
income_change_table = pd.DataFrame({'Año': income_change.index[1:],
                                    'Cambio Porcentual': income_change.values[1:].round(2)})

# Agregar el símbolo de porcentaje al DataFrame
income_change_table['Cambio Porcentual'] = income_change_table['Cambio Porcentual'].map("{:.2f}%".format)

# Función para mostrar los resultados del cambio porcentual
def mostrar_cambio_porcentual():
    st.table(income_change_table)

# Botón para mostrar los resultados
if st.button('Mostrar Cambio Porcentual interanual'):
    mostrar_cambio_porcentual()






    