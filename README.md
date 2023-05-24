<p align="center">
  <img alt="Files Logo" src="https://github.com/caozrich/AviationIncidentDashboard/assets/34092193/d0356121-de8c-430f-ba92-bf7fc54616f8" width="450" />
  <h1 align=center style="color: #FF2403">Proyecto de análisis de accidentes aéreos</h1>
</p>

![Python version](https://img.shields.io/badge/Python-3.11.0-lightgrey) ![AppFramework](https://img.shields.io/badge/libs-pandas-blue) ![AppFramework](https://img.shields.io/badge/-streamlit-yellow) ![AppFramework](https://img.shields.io/badge/-matplotlib-red) ![AppFramework](https://img.shields.io/badge/-seaborn-orange) ![AppFramework](https://img.shields.io/badge/-sqlite3-blue) ![AppFramework](https://img.shields.io/badge/-prophet-green) ![License](https://img.shields.io/badge/License-MIT-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen) ![Contributions](https://img.shields.io/badge/Contributions-Welcome-green)

## Contenido
- [Descripción](#Descripción)
- [Pipeline](#Pipeline)
- [ETL](#Extracción-Transformación-y-Carga-ETL)
- [EDA](#Análisis-Exploratorio-de-Datos-EDA)
- [KPIs](#KPIs
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

[Acede aquí al júpiter notebook](https://github.com/caozrich/AviationIncidentDashboard/blob/main/ETL.ipynb)

### 1. cargar los dataset a usar:
- Cargar el dataset [provisto](https://github.com/caozrich/AviationIncidentDashboard/blob/main/data/AccidentesAviones.csv)  y el dataset adicional _https://www.kaggle.com/datasets/warcoder/civil-aviation-accidents?resource=download_.

### Corregir nombre de columnas y reemplazar nulos por "?":
-Verificar y corregir los nombres de las columnas del dataset para asegurar consistencia.
-Identificar columnas con valores nulos y reemplazarlos por el carácter "?" para mantener una representación uniforme.
-Transformar los diferentes formatos de hora a HH:MM:

### Identificar las columnas que contienen información de hora en formatos diferentes.
-Realizar la transformación de los diferentes formatos de hora a un formato estandarizado **HH:MM**.

### Analizar la columna "Ruta" para identificar las locaciones presentes.
-Convertir las locaciones de la columna "Ruta" a nombres de países:

### Identificar las columnas más relevantes en cada dataset para el análisis de accidentes aéreos.
- Realizar una combinación de los datasets utilizando columnas clave, como la fecha del accidente, número de vuelo y fatalidades.

### Guardar los datasets en formato .csv:
- Guardar el dataset resultante del proceso de ETL.
- Guardar el nuevo dataset resultante de la combinación de los datos en un archivo .csv.
- Asegurarse de que el archivo .csv sea fácilmente accesible y esté listo para su uso posterior en análisis y visualización.

## Análisis Exploratorio de Datos (EDA)
[Acede aquí al júpiter notebook](https://github.com/caozrich/FilmRecSys-ML-DevOps/blob/main/EDA.ipynb)
