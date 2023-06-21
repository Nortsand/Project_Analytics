
# Proyecto de Data Analytics en MOOCs (Udemy, Coursera, edX)
**Proyecto individual 2**

*Por Yuri Díaz Córdova*


Este proyecto se centra en el análisis de datos de tres reconocidas plataformas de cursos en línea masivos y abiertos (MOOCs): Udemy, Coursera y edX. A través de un proceso de Análisis Exploratorio de Datos (EDA) y la creación de un dashboard interactivo, se busca obtener información y conocimientos valiosos sobre estos MOOCs.

## Tabla de contenidos

1. [Introducción](#introducción)
2. [Datos](#datos)
3. [ETL](#datos)
4. [Análisis Exploratorio de Datos (EDA)](#análisis-exploratorio-de-datos-eda)
5. [Dashboard](#dashboard)
6. [Herramientas utilizadas](#herramientas-utilizadas)
7. [Instrucciones de Uso](#instrucciones-de-uso)
8. [Resultados](#resultados)
8. [Limitaciones](#limitaciones)



## Introducción

El objetivo principal de este proyecto es llevar a cabo un análisis exhaustivo de los datos disponibles para descubrir patrones, tendencias y estadísticas relevantes sobre los cursos y los estudiantes en estas plataformas. A través del Análisis Exploratorio de Datos (EDA), se exploran datos financieros, la distribución de los cursos, las calificaciones, y la ingeniería de precios, entre otros aspectos.

La finalidad es que la información obtenido sirva de insumo para una startup de tecnología que desea sumarse al mercado de cursos online, pero de una manera eficiente.


## Datos
Para este proyecto utilizaremos los siguientes datasets: Coursera_courses.csv, Coursera_revies.csv, edx_courses.csv y udemy_courses.csv.

Los archivos están ubicados en la carpeta Data del repositorio. 

Describe las fuentes de datos utilizadas en tu proyecto. Menciona las compañías (Udemy, Coursera, edX) y cualquier otra información importante sobre los conjuntos de datos. Si es posible, incluye enlaces a los conjuntos de datos o menciona cómo se pueden obtener.

## ETL

El proceso de ETL incluyó limpieza y transformaciones  útiles para nuestro análisis. 
* Transformación de columnas de fecha para poder segmentar datos estadísticos por año.
* Columnas de tipo object transformadas a entero para extraer los precios de los cursos.
* Eliminación de variables irrelevantes.
* Eliminación de datos duplicados
* Unión de dos datasets 

## Análisis Exploratorio de Datos (EDA)

* Búsqueda de correlaciones entre las variables por medio de una matriz de correlación.
* Calculamos y graficamos los ingresos anuales históricos de Udemy.
* Creamos una tabla de cambio porcental anual.
* Segmentación en gráfico de pie entre los subscriptores de cursos gratuitos y pagados.
* Estrategia *freemium* y *pricing ladder* en los MOOCs.
* Tasa de conversión de clientes.
* Comparación por áreas de conocimiento entre los cursos pagados y los gratuitos.
* Distribución de los precios de edX y Udemy.
* Distribución de precios por nivel de conocimientos.
* Porcentaje de cursos ofertados según área de conocimiento. 
* WordCloud de los títulos de los cursos. 
* Instituciones asociadas a Coursera con mayor rating promedio por curso. 
* Promedio anual histórico del rating de Coursera
* Segmentación por idioma y cantidad de subscriptores

## Dashboard
* Para la visualización de datos utilizamos Streamlit, una librería de Python especializada en crear aplicaciones web visuales para ciencia de datos. 
* Creamos diferentes tipos de gráficos y de métricas estadísticas.
* Mostramos los KPIs requeridos.



![Probando los gráficos en el local host:](local.jpg)


## Herramientas utilizadas
* Python: Pandas, Numpy, Matplotlib, Seaborn, wordcloud. 
* PowerBi.
* Git y Github.
* Visual Studio Code


## Resultados
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
* Tasa de conversión de Udemy del 2011 al 2017 de 228.88% explicada 

