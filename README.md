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
- [Observaciones/Conclusiones](#Observaciones/Conclusiones)
- [Contribuciones](#Contribuciones)
- [Contacto](#Contacto)

### Descripción del Problema
Los accidentes aéreos son eventos imprevistos y no deseados que causan daños físicos tanto a las personas como a las aeronaves involucradas. Pueden afectar cualquier tipo de aeronave, desde aviones comerciales hasta aviones privados, helicópteros y planeadores.El objetivo es recopilar, analizar y visualizar datos relevantes sobre accidentes aéreos para identificar patrones y tendencias en la seguridad de la aviación civil, lo cual puede conducir a mejoras significativas en la seguridad.

### Rol a Desarrollar
En este proyecto, usted asumirá el rol de Data Analyst dentro de la Organización de Aviación Civil Internacional (OACI). Como Data Analyst, será responsable de realizar el análisis de datos de accidentes aéreos y desarrollar un dashboard interactivo que permita a los usuarios explorar los datos y obtener información detallada sobre accidentes específicos. También deberá generar KPIs relevantes para el análisis de seguridad de la aviación civil.

## Objetivos del Proyecto

Los objetivos del proyecto son los siguientes:

- [x] Realizar el análisis de datos de accidentes aéreos, utilizando los datos proporcionados por la OACI y otras fuentes disponibles públicamente.

- [x] Identificar patrones, tendencias y factores contribuyentes en los accidentes aéreos, a través del análisis de los datos recopilados.

- [x] Desarrollar un dashboard interactivo que permita a los usuarios explorar los datos y obtener información detallada sobre accidentes específicos.

- [x] Generar KPIs relevantes para evaluar la seguridad de la aviación civil, incluyendo la reducción en un 5% anual de la tasa de mortalidad en accidentes aéreos, junto con otros 3 KPIs adicionales que usted deberá generar.

- [x] Presentar los hallazgos obtenidos del análisis de datos a través del informe detallado.

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
  * Se aprecia un decremento significativo desde **1990** y esto se debe a las mejora en los protocolos de seguridad.
- Número de fatalidades por año: Mostrar la evolución del número de fatalidades en accidentes aéreos a lo largo de los años.
  * Al igual que con el número de accidentes, las fatalidades también siguen la dicha tendencia debido a la correlación de esas dos variables.
- Número de accidentes por país: Crear un gráfico que muestre la distribución de accidentes por país.
  * Se aprecia claramente como **Estados Unidos** es el país con más accidentes aereos superando por mucho a los otros países con más accidentes, y esto se debe a que es una de las principales rutas de tráfico en la aeronáutica comercial.
- Número de accidentes por mes: Visualizar la frecuencia de accidentes aéreos según el mes del año.
  * El mes con mas accidentes aereos es **Diciembre**, y esto coincide con la descomposicion estacionaria que muestra un patron de incremento al final de cada año, Esto podría deberse al aumento del tráfico durante la temporada de festividades y vacaciones.
- Número de accidentes por hora del  día: Mostrar la cantidad de accidentes aéreos por hora del día.
  * Se aprecia un rango de tiempo (de **8:00 am** a **8:00 pm**) en el cual el número de accidentes es bastante alto. Esto se debe a que son horas de mayor actividad en el tráfico aéreo, coincidiendo con los horarios de mayor demanda de vuelos comerciales y operaciones aéreas en general.
- Número de accidentes por operador: Representar gráficamente la frecuencia de accidentes según los operadores de las aeronaves involucradas.
  * Se observa que el operador Aeroflot tiene un número de accidentes notablemente alto, considerando que el segundo puesto lo ocupa un operador militar. Esto podría deberse a que Aeroflot es una aerolínea establecida desde **1923** y la más grande de Rusia, lo que implica que su volumen de vuelos es proporcional a la cantidad de accidentes
- Nube de palabras con la columna "summary": Generar una nube de palabras que resalte las palabras más frecuentes en la columna "summary" para identificar patrones o temas comunes.
  * En este gráfico de nube de palabras se puede observar que las palabras más comunes en las descripciones de los accidentes coinciden con el contexto del conjunto de datos. Algunas de ellas son especialmente interesantes, como **_land, failure, takeoff, y ground_**.

### 4.Análisis estadístico:
- Utilizar el método df.describe() para obtener estadísticas descriptivas de las variables numéricas del conjunto de datos.
- Calcular la matriz de correlación para evaluar las relaciones entre las variables numéricas y detectar posibles correlaciones.
  * Se puede destacar la correlacion entre las fatalidades y los pasajeros a bordo, ya que son proporcionales una a la otra, la tendencia es que entre mas pasajeros a bordo mas numero de fatalidades.
- Realizar análisis univariado de variables específicas para comprender su distribución y características individuales.

### 5. Forecasting (de fatalidades por año):
- Realizar una exploración visual y estadística de la variable objetivo para comprender su distribución, tendencia y patrones temporales.
  * la descomposicíon estacional nos dejo ver que hay un incremento a final de cada año y posterior decremento al comienzo del   siguiente.

### 6. Detección de outliers numéricas:
- Seleccionar las variables numéricas relevantes en las que se desea detectar outliers.
- Aplicar métodos de detección de outliers, como el rango intercuartil (IQR) Y el método de los valores extremos
  *  la fecha 1977-03-27 tuvo un total de  **644.0** pasajeros a bordo, y un total de **583.0** fallecidos, siendo estos valores una anomalia ya que la media de fatalidades es **22**


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
   
**_Media de fatalidades_**: Promedio del número de fallecidos en accidentes aéreos.
- Brinda una medida general del impacto en pérdidas humanas.
  * Media de fatalidades total: **22.29**.
  * Año con el media más alta de fatalidades: **2014** (49.6).
  * Año con el media más baja de fatalidades: **1908** (1.0).
  
**_% de accidentes sin supervivientes_**: Proporción de accidentes en los que no hubo ningún superviviente. 
- Destaca la gravedad de los accidentes sin posibilidad de rescate y la necesidad de mejorar las posibilidades de supervivencia.
  * Porcentaje de accidentes sin supervivientes total: **63.5**.
  * Año con el mayor porcentaje de accidentes sin supervivientes: **1909** (100.0).
  * Año con el menor porcentaje de accidentes sin supervivientes: **2020** (37.5).

## Dashboard:

<img src="https://github.com/caozrich/AviationAccident_DataAnalisys/assets/34092193/e1a82247-9d5e-466f-8850-b786d849770a" width="700" height="438"/>
<img src="https://github.com/caozrich/AviationAccident_DataAnalisys/assets/34092193/f2441136-5705-4588-ac8f-2dd4661800d3" width="700" height="438"/>
<img src="https://github.com/caozrich/AviationAccident_DataAnalisys/assets/34092193/72ac376b-cc82-48d5-8262-0fffb39a2b56" width="700" height="438"/>
<img src="https://github.com/caozrich/AviationAccident_DataAnalisys/assets/34092193/589b89d7-d523-4fad-af87-e0315a943871" width="700" height="438"/>

Se desarrolló un **dashboard** interactivo utilizando `Streamlit`, La interfaz es intuitiva y fácil de usar.
 * contiene graficos interactivos de varios tipos
 * contiene un informe de analisis.
 * contiene una implementacion del motor **SQL**

- Accede a la app desplegada en Streamlit Cloud (https://caozrich-aviationaccident-dataanalisys-streamlit-app-e7zt50.streamlit.app/) 

## Observaciones/Conclusiones:

### Observaciones:
- El número total de accidentes en el conjunto de datos es de **5008**, y el número total de víctimas mortales es de **111470**.
- Los accidentes ocurrieron entre 1908 y 2021, con el mayor número de accidentes ocurriendo en las décadas de 1970 y **1980**.
- El mes con más accidentes es Diciembre con un total de **10906**.
- El rango de hora del día con más accidentes es desde las 10 pm hasta las 8 pm.
- Los tipos de aviones más comunes involucrados en los accidentes fueron **Douglas DC-3**, de Havilland Canada DHC-6 Twin Otter y Cessna 208 Caravan.
- Los tipos de aviones más antiguos, como el **Douglas DC-3**, presentaron una proporción más alta de fatalidades en comparación con - los modelos más modernos.
- Los operadores más comunes involucrados en los accidentes fueron Militar - Fuerza Aérea de los Estados Unidos y **Aeroflot**.
- Los países más comunes donde ocurrieron los accidentes fueron **Estados Unidos, Rusia, Colombia y Brasil**.
- El operador **Aeroflot** fue el que más accidentes y fatalidades tuvo.
- En general, el conjunto de datos proporciona información valiosa sobre los accidentes de aviación civil en el último siglo, resaltando la importancia de los *esfuerzos continuos* para mejorar la seguridad aérea.

### Conclusiones
* Desde *1985*, ha habido una notable disminución en la cantidad de accidentes aéreos y fatalidades asociadas. Esta tendencia se debe a mejoras en los sistemas de seguridad, avances tecnológicos y una mayor conciencia sobre la importancia de la seguridad en la aviación. Las medidas y regulaciones más estrictas, junto con avances en la ingeniería de aeronaves, sistemas de navegación más precisos, *mayor capacitación* y enfoque en los factores humanos, han contribuido a esta reducción. La colaboración entre organizaciones internacionales y aerolíneas ha sido clave para compartir datos y mejores prácticas, identificar áreas de mejora y desarrollar *soluciones efectivas* para prevenir accidentes. En resumen, la mejora en la seguridad aérea se ha logrado gracias a un enfoque global en la seguridad, avances tecnológicos y una mayor conciencia sobre los riesgos y medidas preventivas.

* Aunque la tendencia de accidentes aéreos ha venido disminuyendo a lo largo de las últimas cuatro décadas, la *tasa de mortalidad* sigue siendo alta debido a la naturaleza intrínsecamente peligrosa de los accidentes de avión. A pesar de los avances en la seguridad de la aviación, sobrevivir a un accidente de avión sigue siendo extremadamente difícil debido a las fuerzas involucradas, la violencia del impacto y otros factores. Aunque se han implementado medidas para mejorar la resistencia de las aeronaves y la capacitación de la tripulación en situaciones de emergencia, es importante reconocer que la supervivencia en un accidente aéreo sigue siendo un desafío significativo.

### Uso
1. Clona el repositorio a través de ``` https://https://github.com/caozrich/AviationAccident_DataAnalisys```  o descarga el repositorio.
 > Nota: La clonación del repositorio puede llevar algo de tiempo debido a que los conjuntos de datos son relativamente grandes.
2. Instala las dependencias con ```pip install -r requirements.txt```.
3. Ejecuta la aplicación con streamlit run streamlit_app.py. La aplicación se abrirá en tu navegador web local.

## Contribuciones

Si estás interesado en desarrollar habilidades como Data Analyst, este proyecto de código abierto es perfecto para ti. Estoy abierto a contribuciones y sugerencias, por lo que si deseas colaborar, sigue las siguientes instrucciones:

* Haga un fork del repositorio
* Cree una nueva rama con su característica o corrección
* Realice sus cambios y asegúrese de seguir las mejores prácticas de codificación y documentación
* Realice un pull request y espere la revisión y aprobación.

## Licencia

* Este proyecto está licenciado bajo la licencia [MIT](https://opensource.org/licenses/MIT)

## Contacto

Si tiene alguna pregunta o comentario sobre este proyecto, no dude en ponerse en contacto a través de un mensaje directo a mi correo `libreros00@gmail.com` o abriendo un issue en este repositorio.

⭐ Este repositorio si te resulto útil!


