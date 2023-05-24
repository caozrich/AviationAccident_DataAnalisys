<p align="center">
  <img alt="Files Logo" src="https://github.com/caozrich/AviationIncidentDashboard/assets/34092193/d0356121-de8c-430f-ba92-bf7fc54616f8" width="450" />
  <h1 align=center style="color: #FF2403">Proyecto de análisis de accidentes aéreos</h1>
</p>

![Python version](https://img.shields.io/badge/Python-3.11.0-lightgrey) ![AppFramework](https://img.shields.io/badge/libs-pandas-blue) ![AppFramework](https://img.shields.io/badge/-streamlit-yellow) ![AppFramework](https://img.shields.io/badge/-matplotlib-red) ![AppFramework](https://img.shields.io/badge/-seaborn-orange) ![AppFramework](https://img.shields.io/badge/-sqlite3-blue) ![AppFramework](https://img.shields.io/badge/-prophet-green) ![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-green)

## Contenido
- [Descripción](#Descripción)
- [ETL](#Extracción-Transformación-y-Carga-ETL)
- [EDA](#Análisis-Exploratorio-de-Datos-EDA)
- [KPIs](#KPIs)
- [Dashboard](#Dashboard)
- [Contribuciones](#Contribuciones)
- [Contacto](#Contacto)
- 
### Descripción del Problema
Los accidentes aéreos son eventos imprevistos y no deseados que causan daños físicos tanto a las personas como a las aeronaves involucradas. Pueden afectar cualquier tipo de aeronave, desde aviones comerciales hasta aviones privados, helicópteros y planeadores.El objetivo es recopilar, analizar y visualizar datos relevantes sobre accidentes aéreos para identificar patrones y tendencias en la seguridad de la aviación civil, lo cual puede conducir a mejoras significativas en la seguridad.

### Rol a Desarrollar
En este proyecto, usted asumirá el rol de Data Analyst dentro de la Organización de Aviación Civil Internacional (OACI). Como Data Analyst, será responsable de realizar el análisis de datos de accidentes aéreos y desarrollar un dashboard interactivo que permita a los usuarios explorar los datos y obtener información detallada sobre accidentes específicos. También deberá generar KPIs relevantes para el análisis de seguridad de la aviación civil.

## Objetivos del Proyecto

- [x]  Los objetivos del proyecto son los siguientes:

- [x] Realizar el análisis de datos de accidentes aéreos, utilizando los datos proporcionados por la OACI y otras fuentes disponibles públicamente.

- [x] Identificar patrones, tendencias y factores contribuyentes en los accidentes aéreos, a través del análisis de los datos recopilados.

- [x] Desarrollar un dashboard interactivo que permita a los usuarios explorar los datos y obtener información detallada sobre accidentes específicos.

- [x] Generar KPIs relevantes para evaluar la seguridad de la aviación civil, incluyendo la reducción en un 5% anual de la tasa de mortalidad en accidentes aéreos, junto con otros 3 KPIs adicionales que usted deberá generar.

Presentar los hallazgos obtenidos del análisis de datos a través del informe detallado y el dashboard interactivo.

## Extracción, Transformación y Carga (ETL):

[Acede aquí al júpiter notebook](https://github.com/caozrich/AviationAccident_DataAnalisys/blob/main/ETL.ipynb)

### 1. cargar los dataset a usar:
- Cargar el dataset [provisto](https://github.com/caozrich/AviationAccident_DataAnalisys/blob/main/data/AccidentesAviones.csv)  y el   dataset adicional _https://www.kaggle.com/datasets/warcoder/civil-aviation-accidents?resource=download_.

### 2. Corregir nombre de columnas y reemplazar nulos por "?":
- Verificar y corregir los nombres de las columnas del dataset para asegurar consistencia.
- Identificar columnas con valores nulos y reemplazarlos por el carácter "?" para mantener una representación uniforme.
- Transformar los diferentes formatos de hora a HH:MM:

### 3. Identificar las columnas que contienen información de hora en formatos diferentes.
- Realizar la transformación de los diferentes formatos de hora a un formato estandarizado **HH:MM**.

### 4. Analizar la columna "Ruta" para identificar las locaciones presentes.
- Convertir las locaciones de la columna "Ruta" a nombres de países:

### 5. Identificar las columnas más relevantes en cada dataset para el análisis de accidentes aéreos.
- Realizar una combinación de los datasets utilizando columnas clave, como la fecha del accidente, número de vuelo y fatalidades.

### 6. Guardar los datasets en formato .csv:
- Guardar el dataset resultante del proceso de ETL.
- Guardar el nuevo dataset resultante de la combinación de los datos en un archivo .csv.
- Asegurarse de que el archivo .csv sea fácilmente accesible y esté listo para su uso posterior en análisis y visualización.

## Análisis Exploratorio de Datos (EDA)
[Acede aquí al júpiter notebook](https://github.com/caozrich/AviationAccident_DataAnalisys/blob/main/EDA.ipynb)

<img src="https://github.com/caozrich/AviationAccident_DataAnalisys/assets/34092193/abe6f226-dffe-4126-9718-8263dc71c251" width="800" height="538"/>

### 1.Lectura del conjunto de datos:
- Utilizar la función pd.read_csv() para cargar el conjunto de datos en un DataFrame. 

### 2.Exploración del conjunto de datos:
- Utilizar métodos como df.head(), df.info(), df.describe(), entre otros, para obtener una vista inicial del conjunto de datos. Estos métodos proporcionan información sobre las primeras filas, la estructura de las columnas, el resumen estadístico, etc.

### 3.Visualización de variables:
- Número de accidentes por año: Representar gráficamente la cantidad de accidentes aéreos registrados en cada año.
- Número de fatalidades por año: Mostrar la evolución del número de fatalidades en accidentes aéreos a lo largo de los años.
- Número de accidentes por país: Crear un gráfico que muestre la distribución de accidentes por país.
- Número de accidentes por mes: Visualizar la frecuencia de accidentes aéreos según el mes del año.
- Número de accidentes por día: Mostrar la cantidad de accidentes aéreos por día del mes o día de la semana.
- Número de accidentes por operador: Representar gráficamente la frecuencia de accidentes según los operadores de las aeronaves involucradas.
- Nube de palabras con la columna "summary": Generar una nube de palabras que resalte las palabras más frecuentes en la columna "summary" para identificar patrones o temas comunes.

### 4.Análisis estadístico:
- Utilizar el método df.describe() para obtener estadísticas descriptivas de las variables numéricas del conjunto de datos.
- Calcular la matriz de correlación para evaluar las relaciones entre las variables numéricas y detectar posibles correlaciones.
- Realizar análisis univariado de variables específicas para comprender su distribución y características individuales.

## 5. Forecasting (de fatalidades por año):
-Realizar una exploración visual y estadística de la variable objetivo para comprender su distribución, tendencia y patrones temporales.

## 6. Detección de outliers numéricas:
- Seleccionar las variables numéricas relevantes en las que se desea detectar outliers.
- Aplicar métodos de detección de outliers, como el rango intercuartil (IQR) Y el método de los valores extremos

## KPIs

**_Tasa de mortalidad_**: Proporción de fallecimientos en relación con el total de personas involucradas en accidentes aéreos.
- Indica la eficacia de las medidas de seguridad y se expresa como un porcentaje.
   * Tasa de mortalidad total: **71.77**.
   * Año con la tasa de mortalidad más alta: **1919** (115).
   * Año con la tasa de mortalidad más baja: **1999** (30).
   
**_Tasa de supervivencia_**: Proporción de personas que sobreviven a los accidentes aéreos. 
- Muestra la efectividad de las medidas de rescate y evacuación, y se expresa como un porcentaje.
   * Tasa de supervivencia total: **30.77**.
   * Año con la tasa de supervivencia más alta: **1909** (100.0).
   * Año con la tasa de supervivencia más baja: **1919** (-5.0).
   
**_Media de fatalidades**: Promedio del número de fallecidos en accidentes aéreos.
- Brinda una medida general del impacto en pérdidas humanas.
  * Media de fatalidades total: **22.29**.
  * Año con el media más alta de fatalidades: **2014** (49.6).
  * Año con el media más baja de fatalidades: **1908** (1.0).
  
**_% de accidentes sin supervivientes_**: Proporción de accidentes en los que no hubo ningún superviviente. 
- Destaca la gravedad de los accidentes sin posibilidad de rescate y la necesidad de mejorar las posibilidades de supervivencia.
  * Porcentaje de accidentes sin supervivientes total: **63.5**.
  * Año con el mayor porcentaje de accidentes sin supervivientes: **1909** (100.0).
  * Año con el menor porcentaje de accidentes sin supervivientes: **2020** (37.5).




