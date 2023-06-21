
import streamlit as st


st.title("Resultados")

# Texto del resumen
resumen = '''

* Comprobación del uso de las estrategias *freemium* y *pricing ladder* en los MOOCs como instrumento de conversión de clientes.
* Más del 90% de cursos son enseñados en idioma inglés.
* Promedio histórico del rating en Coursera de 4.69 en una escala de 1 a 5. 
* Tasa de conversión de Udemy del 2011 al 2017 de 228.88% explicada. 
* Distribución de precios similar entre Udemy y edX.
* No existe una relación directa entre el precio y el número de cursos pagados.
* Los cursos ofertados en niveles aptos para todo público representan más del 50% tanto para Udemy como para edX.
* La palabra "Beginner" e "Introduction" son las que más se repiten en los títulos de los cursos.
* Los cursos de nivel avanzado son los más caros con una mediana superior a los 50$
* Los cursos gratuitos y pagados ofertados coinciden en áreas de conocimiento por volumen de demanda. 
* Tasa de conversión de Udemy del 2011 al 2017 de 228.88% explicada'''

# Mostrar el resumen en Streamlit
st.markdown(resumen)


