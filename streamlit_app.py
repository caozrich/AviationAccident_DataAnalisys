import altair as alt
import json
import sqlite3 
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
from datetime import datetime
import numpy as np
import seaborn as sns
import streamlit as st
#from prophet import Prophet
from PIL import Image
from st_on_hover_tabs import on_hover_tabs
from streamlit_echarts import JsCode
from streamlit_echarts import Map
from streamlit_echarts import st_echarts
from CSS_styles import apply_styles

st.set_page_config(layout="wide")

dfo = pd.read_csv("data/AA_Clean.csv")
df2 = pd.read_csv("data/merged_data.csv")

dfo['date'] = pd.to_datetime(dfo['date'], errors='coerce')

apply_styles()

st.markdown('<style>' + open('css/style.css').read() + '</style>', unsafe_allow_html=True)

def box_label (wch_colour_box,i,sline,iconname): #color, titulo, dato
    wch_colour_font = (255,255,255)
    fontsize = 18
    valign = "left"
    lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
    esp = " "
    espacios = "    "
    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 1); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 1); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname} fa-xs'>{esp}</i>{esp}
                            <b>{i}</b><BR>
                            <span style='font-size: 25px; margin-top: 0;'>{espacios}{sline}</span></p>"""
    return lnk + htmlstr                        

                        
def page_1():
    
    
    df = dfo.copy()

    df['fatalities'] = df['fatalities'].fillna(0)
    df['all_aboard'] = df['all_aboard'].fillna(0)
    df['passenger_fatalities'] = df['passenger_fatalities'].fillna(0)    
    df['crew_fatalities'] = df['crew_fatalities'].fillna(0) 

    range_time = st.slider('Rango de fecha:', min_value=datetime(1908, 9, 17), max_value=datetime(2021, 7, 6), value=(datetime(1908, 9, 17), datetime(2021, 7, 6)), format="MM/DD/YYYY")
    df = df.loc[(df['date'] >= range_time[0]) & (df['date'] <= range_time[1])]



    formatter = JsCode(
        "function (params) {"
        + "var value = (params.value + '').split('.');"
        + "value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');"
        + "return params.seriesName + '<br/>' + params.name + ': ' + value;}"
    ).js_code

    with open("data/world.json", "r") as f:
        world_map_data = json.loads(f.read())


    country_counts = defaultdict(int)
    for country in df['Cleaned Country'].tolist():
        if not pd.isnull(country):
            country_counts[country] += 1

    world_map = Map(
        "world",
        world_map_data,
    )

    options = {
        "title": {
            "text": " ",
            "left": "right",
        },
        "tooltip": {
            "trigger": "item",
            "showDelay": 0,
            "transitionDuration": 0.2,
            "formatter": formatter,
        },
        "visualMap": {
            "left": "right",
            "min": 1,
            "max": 150,
            "inRange": {
                "color": [
                    "#FFFFFF",
                    "#EDF0F9",
                    "#DCE2F3",
                    "#CBD4ED",
                    "#BAC5E8",
                    "#A9B7E2",
                    "#98A9DC",
                    "#879AD7",
                    "#768CD1",
                    "#657ECB",
                    "#5470C6",
                    ]   
            },
            "text": ["High", "Low"],
            "calculable": True,
        },
        "toolbox": {
            "show": True,
            "left": "left",
            "top": "top",
            "feature": {
                "dataView": {"readOnly": False},
                "restore": {},
                "saveAsImage": {},
            },
        },
        "series": [
            {
                "name": "Países con más accidentes",
                "type": "map",
                "roam": True,
                "map": "world",
                "emphasis": {"label": {"show": True}},
                "textFixed": {"name": "Afghanistan", "value": 28397.812},
                "data":  [{"name": country, "value": count} for country, count in country_counts.items()],
            }
        ],
    }

    #--line
    df['year'] = df['date'].dt.year
    fatalities_by_year = df.groupby('year')['fatalities'].sum()
    line = {
        "title": {"text": " "},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
        },
        "legend": {"data": ["Fatalidades"]},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": [
            {
                "type": "category",
                "boundaryGap": False,
                "data": fatalities_by_year.index.tolist(),
            }
        ],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "name": "Fatalidades",
                "type": "line",
                "stack": "1",
                "areaStyle": {},
                "emphasis": {"focus": "series"},
                "data": fatalities_by_year.values.tolist(),
            }
        ],
    }

    #--BAR

    df['year'] = df['date'].dt.year

    accident_counts = df['year'].value_counts().sort_index()

    most_common_date = accident_counts.idxmax()
    indices = accident_counts.index.tolist()
    values = accident_counts.values.tolist()

    for i, idx in enumerate(indices):
        if idx == most_common_date:
            values[i] = {"value": values[i], "itemStyle": {"color": "#a90000"}}
            break

    bar = {
        "xAxis": {
            "type": "category",
            "data": accident_counts.index.tolist(),
        },
        "yAxis": {"type": "value"},
        "series": [
            {
                "data": values,
                "type": "bar",
                "itemStyle": {"normal": {"color": '#FAC858'}},
            }
        ],
    }
    #--bar2

    df['month'] = df['date'].dt.month
    accidents_by_month = df['month'].value_counts().sort_index()
    fatalities_by_month = df.groupby('month')['fatalities'].sum().sort_index()
    all_aboard_by_month = df.groupby('month')['all_aboard'].sum().sort_index()
    survivors_by_month = all_aboard_by_month - (df.groupby('month')['passenger_fatalities'].sum() + df.groupby('month')['crew_fatalities'].sum()).sort_index()


    month_bar = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["Fatalidades", "Surpervivientes", "Cantidad de accidentes"]  # Agregamos la categoría "Cantidad de accidentes"
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        },
        "series": [
            {
                "name": "Fatalidades",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": fatalities_by_month.tolist(),
            },
            {
                "name": "Surpervivientes",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": survivors_by_month.tolist(),
            },
            {
                "name": "Cantidad de accidentes",  
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": accidents_by_month.tolist(),
            },
        ],
    }
    #--bar3
    df['weekday'] = df['date'].dt.dayofweek
    accidents_by_weekday = df['weekday'].value_counts().sort_index()
    fatalities_by_weekday = df.groupby('weekday')['fatalities'].sum().sort_index()
    all_aboard_by_weekday = df.groupby('weekday')['all_aboard'].sum().sort_index()
    survivors_by_weekday = all_aboard_by_weekday - (df.groupby('weekday')['passenger_fatalities'].sum() + df.groupby('weekday')['crew_fatalities'].sum()).sort_index()

    weekday_bar = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["Fatalidades", "Supervivientes", "Cantidad de accidentes"]
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
        },
        "series": [
            {
                "name": "Fatalidades",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": fatalities_by_weekday.tolist(),
            },
            {
                "name": "Supervivientes",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": survivors_by_weekday.tolist(),
            },
            {
                "name": "Cantidad de accidentes",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": accidents_by_weekday.tolist(),
            },
        ],
    }
    #bar4---
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    df['hour'] = df['time'].dt.hour
    accidents_by_hour = df['hour'].value_counts().sort_index()
    fatalities_by_hour = df.groupby('hour')['fatalities'].sum().sort_index()
    all_aboard_by_hour = df.groupby('hour')['all_aboard'].sum().sort_index()
    survivors_by_hour = all_aboard_by_hour - (df.groupby('hour')['passenger_fatalities'].sum() + df.groupby('hour')['crew_fatalities'].sum()).sort_index()

    hour_bar = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["Fatalidades", "Supervivientes", "Cantidad de accidentes"]
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": [f"{hour:02d}:00" for hour in range(24)],
        },
        "series": [
            {
                "name": "Fatalidades",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": fatalities_by_hour.tolist(),
            },
            {
                "name": "Supervivientes",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": survivors_by_hour.tolist(),
            },
            {
                "name": "Cantidad de accidentes",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": accidents_by_hour.tolist(),
            },
        ],
    }
    #--PIE
    category_counts = df2['cat'].value_counts(normalize=True)

    data_list = [{"value": round(count*100,4), "name": category} for category, count in category_counts.items()]

    pie = {
        "tooltip": {"trigger": "item"},
        "legend": {"show": True},
        "series": [
            {
                "name": "Categoría",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {
                    "borderRadius": 10,
                    "borderColor": "#fff",
                    "borderWidth": 2,
                },
                "label": {"show": False, "position": "center"},
                "emphasis": {
                    "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                },
                "labelLine": {"show": False},
                "data":data_list,
            }
        ],
    }

    #---cake

    df_grouped = df2.groupby("cat").sum()
    df_grouped["fatality_percentage"] = (df_grouped["fatalities"] / df_grouped["all_aboard"]) * 100

    data = []
    for index, row in df_grouped.iterrows():
        percentage = round(row["fatality_percentage"], 1)  # Redondear a un decimal
        data.append({"value": percentage, "name": index})

    cake = {
        "tooltip": {"trigger": "item"},
        "legend": {"show": False},
        "series": [
            {
                "name": "Categorías",
                "type": "pie",
                "radius": "50%",
                "data": data,
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
            }
        ],
    }
    #---line1
    df_temp1 = dfo.copy()
    df_temp1 = df_temp1.groupby(df_temp1['date'].dt.year).agg({'fatalities': 'sum', 'all_aboard': 'sum'}).reset_index()
    df_temp1['mortality_rate'] = (df_temp1['fatalities'] / df_temp1['all_aboard']) * 100

    mortality_rate_by_year = df_temp1.set_index('date')['mortality_rate']

    line_1 = {
        "title": {"text": "   "},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
        },
        "legend": {"data": ["mortality_rate"]},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": [
            {
                "type": "category",
                "boundaryGap": False,
                "data": mortality_rate_by_year.index.tolist(),
            }
        ],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "name": "Tasa de mortalidad", 
                "type": "line",
                "stack": "1",
                "areaStyle": {"color": "#FC8452E6"},
                "itemStyle": {"color": "#FC8452"},  
                "emphasis": {"focus": "series"},
                "lineStyle": {"color": "#FC8452"}, 
                "data": mortality_rate_by_year.values.tolist(),
            }
        ],
    }

    #---line2
    df_temp2 = df.copy() 
    df_temp2['survivors'] = df_temp2['all_aboard'] - (df_temp2['passenger_fatalities'] + df_temp2['crew_fatalities'])
    df_temp2 = df_temp2.groupby(df_temp2['date'].dt.year).agg({'survivors': 'sum', 'all_aboard': 'sum'}).reset_index()

    df_temp2['survival_rate'] = (df_temp2['survivors'] / df_temp2['all_aboard']) * 100

    survival_rate_by_year = df_temp2.set_index('date')['survival_rate']


    line_2 = {
        "title": {"text": "    "},
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
        },
        "legend": {"data": ["survival_rate"]},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": [
            {
                "type": "category",
                "boundaryGap": False,
                "data": survival_rate_by_year.index.tolist(),
            }
        ],
        "yAxis": [{"type": "value"}],
        "series": [
            {
                "name": "Tasa de supervivencia",
                "type": "line",
                "stack": "1",
                "areaStyle": {"color": "#FFC24BE6"},
                "itemStyle": {"color": "#FFC24B"},  
                "emphasis": {"focus": "series"},
                "lineStyle": {"color": "#FFC24B"},  
                "data": survival_rate_by_year.values.tolist(),
            }
        ],
    }
    #tasa de mortalidad----------------------------------------------

    mortality_rate_total = (df['fatalities'].sum() / df['all_aboard'].sum()) * 100
    mortality_rate_total = str(round(mortality_rate_total,1)) + "%"

    #--

    df_temp1 = dfo.copy() 
    df_temp1 = df_temp1.groupby(df_temp1['date'].dt.year).agg({'fatalities': 'sum', 'all_aboard': 'sum'}).reset_index()


    df_temp1['mortality_rate'] = (df_temp1['fatalities'] / df_temp1['all_aboard']) * 100
    last_year = df_temp1['mortality_rate'].iloc[-1]  # Tasa de mortalidad del último año
    second_last_year = df_temp1['mortality_rate'].iloc[-2]  # Tasa de mortalidad del penúltimo año
    percentage_change = ((last_year - second_last_year) / second_last_year) * 100
    percentage_change = str(round(percentage_change,1)) + "% en el ultimo año"

    #tasa de supervivencia--------------------------------------------

    total_survivors = df['all_aboard'].sum() - (df['passenger_fatalities'].sum() + df['crew_fatalities'].sum())
    total_all_aboard = df['all_aboard'].sum()
    survival_rate_total = (total_survivors / total_all_aboard) * 100
    survival_rate_total = str(round(survival_rate_total,1)) + "%"
     
    #---

    df_temp2 = dfo.copy() 
    df_temp2['survivors'] = df_temp2['all_aboard'] - (df_temp2['passenger_fatalities'] + df_temp2['crew_fatalities'])
    df_temp2 = df_temp2.groupby(df_temp2['date'].dt.year).agg({'survivors': 'sum', 'all_aboard': 'sum'}).reset_index()

    df_temp2['survival_rate'] = (df_temp2['survivors'] / df_temp2['all_aboard']) * 100
    last_year_survival_rate = df_temp2['survival_rate'].iloc[-1]
    penultimate_year_survival_rate = df_temp2['survival_rate'].iloc[-2]
    percentage_change_2 = ((last_year_survival_rate - penultimate_year_survival_rate) / penultimate_year_survival_rate) * 100
    percentage_change_2 = str(round(percentage_change_2,1)) + "% en el ultimo año"

    #media de fallecidos --------------------------------------------
     
    df_temp3 = dfo.copy()
    df_temp3 = df_temp3.groupby(df_temp3['date'].dt.year).agg({'fatalities': 'mean'}).reset_index()

    last_year_average = df_temp3['fatalities'].iloc[-1]
    second_last_year_average = df_temp3['fatalities'].iloc[-2] 
    kpi_formated = str(round(last_year_average,1)) + "% en el ultimo año"

    #porcentaje de accidentes fatales --------------------------------------------   
    df_temp4 = dfo.copy()
    df_high_lethality = df_temp4[df_temp4['fatalities'] >= df_temp4['all_aboard']]
    high_lethality_by_year = df_high_lethality.groupby(df_high_lethality['date'].dt.year).size()
    total_accidents_by_year = df_temp4.groupby(df_temp4['date'].dt.year).size()
    percentage_high_lethality_by_year = (high_lethality_by_year / total_accidents_by_year) * 100
    percentage_high_lethality_by_year = percentage_high_lethality_by_year.round(1)
    last_year_percentage = percentage_high_lethality_by_year.iloc[-1]  
    second_last_year_percentage = percentage_high_lethality_by_year.iloc[-2]  
    f_percent = str(second_last_year_percentage) + "%"
    s_percent = str(last_year_percentage) + "% en el ultimo año"
    #--content


    st.markdown("""<hr style="height:7px;border:none;color:#5470C6;background-color:#5470C6;" /> """, unsafe_allow_html=True)


    col1, col2, col3 ,col4= st.columns([3, 3, 3, 3])
    col1.metric("Tasa de mortalidad en el año pasado", round(second_last_year,1), delta = percentage_change,help = "fatalities/all_aboard*100")
    col2.metric("Tasa de supervivencia en el año pasado",round(penultimate_year_survival_rate,1), delta = percentage_change_2,help = "total_survivors/total_all_aboard*100")
    col3.metric("Media de fallecidos en el año pasado:",round(second_last_year_average,1), delta = kpi_formated,help = "mean(fatalities)")
    col4.metric("% de accidentes sin supervivientes en el año pasado", f_percent, delta = s_percent,help = "high_lethality_by_year/total_accidents_by_year*100")
    st.divider() 


    TOTACC = df.shape[0]
    TOTFAT = df["fatalities"].sum()
    df["sobrevivientes"] = df["all_aboard"] - (df["passenger_fatalities"] + df["crew_fatalities"])
    TOTSUV = df["sobrevivientes"].sum()
    TOTPLANE = df["registration"].nunique()

    cola, colb, colc , cold = st.columns(4)
    cola.markdown(box_label((255,194,75),"ACCIDENTES TOTALES",TOTACC,"fas fa-exclamation-triangle"), unsafe_allow_html=True)
    colb.markdown(box_label((84,112,198),"FATALIDADES TOTALES",int(TOTFAT),"fas fa-user-times"), unsafe_allow_html=True)
    colc.markdown(box_label((145,204,117),"SUPERVIVIENTES TOTALES",int(TOTSUV),"fas fa-user"), unsafe_allow_html=True)
    cold.markdown(box_label((252,132,82),"AVIONES INVOLUCRADOS",TOTPLANE,"fas fa-plane"), unsafe_allow_html=True)   




    col_map,col_bar, col_element = st.columns([4, 2, 2])
    with col_map:
        col_map.write('• Países con más accidentes aéreos:')
        st_echarts(options, map=world_map, key="map_chart")

    with col_bar:
        col_bar.write('• Accidentes por año:')
        st_echarts( options=bar, height="350px",)

    with col_element:
        col_element.write('• Fatalidades por año:')
        st_echarts( options=line, height="310px",)


    st.divider() 

    st.write('• Accidentes aéreos, fatalidades y supervivientes por mes, día y hora:')
    month_col,col_weekday,col_hour = st.columns([4, 2, 2]) 
    with month_col:
        st_echarts( options=month_bar, height="400px",)
    with col_weekday:
        st_echarts( options=weekday_bar, height="400px",)
    with col_hour:
        st_echarts( options=hour_bar, height="400px",)
    st.divider() 


    st.write('• Tasa de mortalidad por años:')
    st_echarts( options=line_1, height="310px",)
    st.write('• Tasa de supervivencia por años:')
    st_echarts( options=line_2, height="310px",)

    st.divider() 
    st.markdown('### Accidentes civiles por categoría')
    col_element2,col_pie,col_cake = st.columns([1,1,2])
    
    with col_element2:    
        with st.expander('', expanded=True):
            st.markdown(f'''
            ##### Categorías de Accidentes(ASN):
            <ul style="padding-left:20px">
            <li>A = Accidente</li>
            <li>I = Incidente.</li>
            <li>H = Secuestro</li>
            <li>C = Ocurrencia criminal (sabotaje, derribo)</li>
            <li>O = Otra ocurrencia (fuego en tierra, sabotaje)</li>
            <br>
            <li>1 = Pérdida total de la aeronave </li>                         
            <li>2 = Daños reparables </li>                             
            </ul>
            ''', unsafe_allow_html=True)

    with col_pie:
        col_pie.write('• Porcentage por categoría:')
        st_echarts(options=pie, height="500px")
    with col_cake:
        col_cake.write('• Categorías con más porcentaje de fatalidades:')
        st_echarts(options=cake, height="500px")


    st.markdown("""<hr style="height:7px;border:none;color:#5470C6;background-color:#5470C6;" /> """, unsafe_allow_html=True)



def page_2():
    
    df = dfo.copy()
    df['fatalities'] = df['fatalities'].fillna(0)
    df['all_aboard'] = df['all_aboard'].fillna(0)
    df['passenger_fatalities'] = df['passenger_fatalities'].fillna(0)    
    df['crew_fatalities'] = df['crew_fatalities'].fillna(0) 

    #--bar_1
        
    fatalities_by_operator = df.groupby('operator')['fatalities'].sum().sort_values(ascending=False)
    accidents_by_operator = df['operator'].value_counts()
    all_aboard_by_operator = df.groupby('operator')['all_aboard'].sum()

    data = {
        'Operadores': fatalities_by_operator.index[:10],
        'Fatalidades': fatalities_by_operator.values[:10],
        'Accidentes': accidents_by_operator[fatalities_by_operator.index[:10]].values,
        'Supervivientes': all_aboard_by_operator[fatalities_by_operator.index[:10]].values - (df.groupby('operator')['passenger_fatalities'].sum() + df.groupby('operator')['crew_fatalities'].sum())[fatalities_by_operator.index[:10]].values
    }

    df_fatalities = pd.DataFrame(data)

    #---bar_2

    fatalities_by_type = df.groupby('ac_type')['fatalities'].sum().sort_values(ascending=False)
    accidents_by_type = df['ac_type'].value_counts()
    all_aboard_by_type = df.groupby('ac_type')['all_aboard'].sum()
    passenger_fatalities_by_type = df.groupby('ac_type')['passenger_fatalities'].sum()
    crew_fatalities_by_type = df.groupby('ac_type')['crew_fatalities'].sum()

    data = {
        'Tipo de avión': fatalities_by_type.index[:10],
        'Fatalidades': fatalities_by_type.values[:10],
        'Accidentes': accidents_by_type[fatalities_by_type.index[:10]].values,
        'Supervivientes': all_aboard_by_type[fatalities_by_type.index[:10]].values - (passenger_fatalities_by_type.values[:10] + crew_fatalities_by_type.values[:10])
    }

    df_fatalities_by_type = pd.DataFrame(data)

    #---scatter   
    survivors_counts = df['all_aboard'] - (df['passenger_fatalities'] + df['crew_fatalities'])

    data = {
        'Total de personas a bordo': df['all_aboard'].astype(int),
        'Fatalidades': df['fatalities'].astype(int),
        'Supervivientes': survivors_counts.astype(int)
    }

    df_stats = pd.DataFrame(data)


    chart = alt.Chart(df_stats).mark_circle().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color=alt.value('steelblue')  # Asigna un color fijo a los puntos, por ejemplo, azul acero.
    ).properties(
        width=200,
        height=200
    ).repeat(
        row=['Total de personas a bordo','Fatalidades', 'Supervivientes'],
        column=['Total de personas a bordo','Fatalidades', 'Supervivientes']
    )



    st.markdown("""<hr style="height:7px;border:none;color:#5470C6;background-color:#5470C6;" /> """, unsafe_allow_html=True)
    st.markdown('### Accidentes, Fatalidades y Supervivientes por Operadores y tipo de avión')
    col_bar, col_scatt= st.columns([2, 2]) 
    with col_bar:
        col_bar.write('• Operadores:')
        st.bar_chart(df_fatalities, x='Operadores', y="Accidentes")
        st.bar_chart(df_fatalities, x='Operadores', y=["Fatalidades", "Supervivientes"])
    with col_scatt:
        col_scatt.write('• Tipo de avión:')
        st.bar_chart(df_fatalities_by_type, x='Tipo de avión', y="Accidentes")
        st.bar_chart(df_fatalities_by_type, x='Tipo de avión', y=["Fatalidades", "Supervivientes"])


    st.divider() 

    st.markdown('### Correlaciones')
    st.write('• Correlaciones entre personas a bordo, fatalidades y supervivientes:')
    st.write(' ')
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
      st.write("")

    with col2:
      st.altair_chart(chart, use_container_width=True)

    with col3:
      st.write("")

    st.divider() 





def page_3():

    df = dfo.copy()

    df['fatalities'] = df['fatalities'].fillna(0)
    df['all_aboard'] = df['all_aboard'].fillna(0)
    df['passenger_fatalities'] = df['passenger_fatalities'].fillna(0)    
    df['crew_fatalities'] = df['crew_fatalities'].fillna(0) 
  
    data = df.groupby(df['date'].dt.year)['fatalities'].sum().reset_index()
    data.columns = ['ds', 'y']
    st.markdown("""<hr style="height:7px;border:none;color:#5470C6;background-color:#5470C6;" /> """, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: black;'>Pronóstico de Fatalidades por Año</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>Pronóstico de Fatalidades a 10 años en el futuro</h2>", unsafe_allow_html=True)
    
    image = Image.open('img/forescasting.png')

    st.image(image)
    #model = Prophet()
    #model.fit(data)
    
    #future = pd.date_range(start=data['ds'].min(), periods=len(data) - 50, freq='Y')
    #future = pd.DataFrame({'ds': future})
    
    #forecast = model.predict(future)

    #fig = model.plot(forecast)
    #plt.xlabel('Año')
    #plt.ylabel('Fatalidades')
    #plt.title("")
    #plt.grid(False) 
    #color = (145/255, 204/255, 117/255)
    #plt.gca().get_lines()[0].set_markerfacecolor(color)
    #plt.gca().get_lines()[0].set_markeredgecolor(color)
    #line_color = (84/255, 112/255, 198/255)  # Color rojo (RGB)
    #lines = plt.gca().get_lines()
    #for line in lines:
        #line.set_color(line_color)
    #st.pyplot(fig)
    #st.divider() 
    st.markdown("<h2 style='text-align: center; color: black;'>Tendencia de los últimos 50 años y Descomposición Estacional</h2>", unsafe_allow_html=True)
    image2 = Image.open('img/seasonal.png')

    st.image(image2)
    #fig = model.plot_components(forecast)
    #plt.grid(False) 
    #st.pyplot(fig)



def page_4():
  st.markdown("""<hr style="height:7px;border:none;color:#5470C6;background-color:#5470C6;" /> """, unsafe_allow_html=True)

  st.header("Introducción")
  st.markdown("Los **accidentes aéreos** son eventos imprevistos y no deseados que causan daños físicos tanto a las personas como a las aeronaves involucradas. Pueden afectar cualquier tipo de aeronave, desde aviones comerciales hasta aviones privados, helicópteros y planeadores. La industria de la aviación, las autoridades reguladoras y los investigadores dedican constantes esfuerzos para mejorar la seguridad de la aviación y prevenir futuros accidentes. En este sentido, el análisis de datos históricos de accidentes aéreos desempeña un papel fundamental. La recopilación y el análisis sistemático de datos permiten identificar patrones, tendencias y factores contribuyentes, lo cual puede conducir a mejoras significativas en la seguridad.")
  st.markdown("En este informe, se presentarán los hallazgos obtenidos a partir del análisis de los datos obtenidos y del dashboard interactivo que junto a los indicadores clave de rendimiento propuestos (**KPIs**), serán utilizados para evaluar y monitorear la seguridad de la aviación civil.")


  st.header("KPIs")
  st.write(
        """    
- **_Tasa de mortalidad_**: Proporción de fallecimientos en relación con el total de personas involucradas en accidentes aéreos. Indica la eficacia de las medidas de seguridad y se expresa como un porcentaje.
    - Tasa de mortalidad total: **71.77**
    - Año con la tasa de mortalidad más alta: **1919** (115)
    - Año con la tasa de mortalidad más baja: **1999** (30)
        """
    )
  st.write(
        """    
- **_Tasa de supervivencia_**: Proporción de personas que sobreviven a los accidentes aéreos. Muestra la efectividad de las medidas de rescate y evacuación, y se expresa como un porcentaje.
    - Tasa de supervivencia total: **30.77**
    - Año con la tasa de supervivencia más alta: **1909** (100.0)
    - Año con la tasa de supervivencia más baja: **1919** (-5.0)
        """
    )
  st.write(
        """    
- **_Media de fallecidos_**: Promedio del número de fallecidos en accidentes aéreos. Brinda una medida general del impacto en pérdidas humanas.
    - Media de fatalidades total: **22.29**
    - Año con el media más alta de fatalidades: **2014** (49.6)
    - Año con el media más baja de fatalidades: **1908** (1.0)
        """
    ) 
  st.write(
        """    
- **_% de accidentes sin supervivientes_**: Proporción de accidentes en los que no hubo ningún superviviente. Destaca la gravedad de los accidentes sin posibilidad de rescate y la necesidad de mejorar las posibilidades de supervivencia.
    - Porcentaje de accidentes sin supervivientes total: **63.5**
    - Año con el mayor porcentaje de accidentes sin supervivientes: **1909** (100.0)
    - Año con el menor porcentaje de accidentes sin supervivientes: **2020** (37.5)
        """
    )                

  st.divider() 
  st.header("Observaciones")
  st.markdown("- El número total de accidentes en el conjunto de datos es de **5008**, y el número total de víctimas mortales es de **111470**.")
  st.markdown("- Los accidentes ocurrieron entre 1908 y 2021, con el mayor número de accidentes ocurriendo en las décadas de 1970 y 1980.")
  st.markdown("- El mes con más accidentes es Diciembre con un total de **10906**.")
  st.markdown("- El rango de hora del día con más accidentes es desde las 10 pm hasta las 8 pm.")
  st.markdown("- Los tipos de aviones más comunes involucrados en los accidentes fueron **Douglas DC-3**, de Havilland Canada DHC-6 Twin Otter y Cessna 208 Caravan.")
  st.markdown("- Los tipos de aviones más antiguos, como el **Douglas DC-3**, presentaron una proporción más alta de fatalidades en comparación con los modelos más modernos.")
  st.markdown("- Los operadores más comunes involucrados en los accidentes fueron **Militar - Fuerza Aérea de los Estados Unidos** y **Aeroflot**.")
  st.markdown("- Los países más comunes donde ocurrieron los accidentes fueron **Estados Unidos**, **Rusia**, **Colombia** y **Brasil**.")
  st.markdown("- El operador **Aeroflot** fue el que más accidentes y fatalidades tuvo.")
  st.markdown("- En general, el conjunto de datos proporciona información valiosa sobre los accidentes de aviación civil en el último siglo, resaltando la importancia de los esfuerzos continuos para mejorar la seguridad aérea.")
  st.divider() 
  st.header("Conclusiones")
  st.markdown("- Desde 1985, ha habido una notable disminución en la cantidad de accidentes aéreos y fatalidades asociadas. Esta tendencia se debe a mejoras en los sistemas de seguridad, avances tecnológicos y una mayor conciencia sobre la importancia de la seguridad en la aviación. Las medidas y regulaciones más estrictas, junto con avances en la ingeniería de aeronaves, sistemas de navegación más precisos, mayor capacitación y enfoque en los factores humanos, han contribuido a esta reducción. La colaboración entre organizaciones internacionales y aerolíneas ha sido clave para compartir datos y mejores prácticas, identificar áreas de mejora y desarrollar soluciones efectivas para prevenir accidentes. En resumen, la mejora en la seguridad aérea se ha logrado gracias a un enfoque global en la seguridad, avances tecnológicos y una mayor conciencia sobre los riesgos y medidas preventivas.")
  st.markdown("- Aunque la tendencia de accidentes aéreos ha disminuido, la tasa de mortalidad sigue siendo alta debido a la naturaleza intrínsecamente peligrosa de los accidentes de avión. A pesar de los avances en la seguridad de la aviación, sobrevivir a un accidente de avión sigue siendo extremadamente difícil debido a las fuerzas involucradas, la violencia del impacto y otros factores. Aunque se han implementado medidas para mejorar la resistencia de las aeronaves y la capacitación de la tripulación en situaciones de emergencia, es importante reconocer que la supervivencia en un accidente aéreo sigue siendo un desafío significativo.")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.write(" ")
  st.markdown("¡Gracias por leer mi reporte de análisis de Accidentes Aéreos! by Richard Libreros `:D`")



def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data 


def page_5():
    conn = sqlite3.connect('data/AA_Cleaned.db')
    cursor = conn.cursor()

    accidentes_aereos = ['date', 'time', 'Ruta', 'operator', 'flight_no', 'type', 'ac_type', 'registration', 'cn_ln', 'all_aboard', 'Passengers Aboard', 'crew_aboard', 'fatalities', 'passenger_fatalities', 'crew_fatalities', 'ground', 'summary', 'Country', 'Cleaned Country']
    st.title("Implementación de SQL - Accidentes de aviones:")
    st.markdown("""<hr style="height:7px;border:none;color:#5470C6;background-color:#5470C6;" /> """, unsafe_allow_html=True)

    # Columns/Layout
    col1, col2 = st.columns(2)

    with col1:
        with st.form(key='query_form'):
            raw_code = st.text_area("SQL query:","SELECT * FROM accidentes_aereos LIMIT 10")
            submit_code = st.form_submit_button("Ejecutar")

        # Table of Info
        with st.expander("Info Tabla"):
            table_info = {'accidentes_aereos': accidentes_aereos}
            st.json(table_info)

    # Results Layouts
    with col2:
        if submit_code:
            st.info("Query enviada")
            st.code(raw_code)

            # Results
            cursor.execute(raw_code)
            result = cursor.fetchall()

            with st.expander("Resultados tabla:"):
                query_df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
                st.dataframe(query_df)
                
            with st.expander("Resultados:"):
                st.write(result)

                
    st.divider() 

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard', 'Reporte de análisis', 'SQL'], 
                         iconName=['dashboard', 'plagiarism','table'], default_choice=0)

if tabs =='Dashboard':
    st.title("Dashboard - Accidentes Aéreos :airplane_departure:")
    tab1,tab2,tab3 = st.tabs(["General Data", "Specific Data", "Forecasting"])
    with tab1:
        page_1()
    with tab2:
        page_2()
    with tab3:
        page_3()


elif tabs == 'Reporte de análisis':
    st.title(":bookmark_tabs: Reporte de análisis de Accidentes Aéreos")
    page_4()


elif tabs == 'SQL':
    page_5()




