# libs
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# import
data = pd.read_csv('train_df.csv')

# jams

fig = px.histogram(
    data,
    x='jams',
    color='weekday',
    facet_col='hour_type',
    nbins=10,
    title="Распределение интенсивности заторов"
)

bin_width = 1
start = data['jams'].min()
end = data['jams'].max()

fig.update_traces(
    xbins=dict(
        start=start - 0.5,
        end=end + 0.5,
        size=bin_width
    ),
    marker_line=dict(color='white', width=0.5)
)

unique_values = list(range(start, end + 1))
for i in range(1, len(data['hour_type'].unique()) + 1):
    fig.layout[f'xaxis{i}'].tickvals = unique_values
    fig.layout[f'xaxis{i}'].ticktext = [str(v) for v in unique_values]
    fig.layout[f'xaxis{i}'].title.text = "Баллы"

fig.update_layout(
    title=dict(
        text="Распределение интенсивности заторов",
        font=dict(size=18),
        x=0.5  
    ),
    yaxis_title="Количество случаев",
    legend_title="День недели",
    font=dict(size=14),
    showlegend=True,
    legend=dict(
        orientation="h",  
        y=-0.2,  
        x=0.5,
        xanchor='center',
        yanchor='top'
    ),
    margin=dict(l=30, r=30, t=50, b=50), 
    plot_bgcolor="white",  
)


fig.update_xaxes(showgrid=False, zeroline=False) 
fig.update_yaxes(showgrid=True, zeroline=False, gridcolor="lightgrey") 

hour_type_titles = {
    'night': 'Ночь',
    'morning': 'Утро',
    'afternoon': 'День',
    'evening': 'Вечер'
}
fig.for_each_annotation(lambda a: a.update(text=hour_type_titles[a.text.split('=')[1]]))
fig.show()

fig.write_html("graph1.html")



### crashes

fig = px.histogram(
    data,
    x='crash',
    color='weather',
    facet_col='hour_type',
    nbins=10,
    title="Распределение ДТП"
)

bin_width = 1
start = data['jams'].min()
end = data['jams'].max()

fig.update_traces(
    xbins=dict(
        start=start - 0.5,
        end=end + 0.5,
        size=bin_width
    ),
    marker_line=dict(color='white', width=0.5) 
)

unique_values = list(range(start, end + 1))
for i in range(1, len(data['hour_type'].unique()) + 1):
    fig.layout[f'xaxis{i}'].tickvals = unique_values
    fig.layout[f'xaxis{i}'].ticktext = [str(v) for v in unique_values]
    fig.layout[f'xaxis{i}'].title.text = "Количество ДТП"

fig.update_layout(
    title=dict(
        text="Распределение интенсивности ДТП",
        font=dict(size=18),
        x=0.5  
    ),
    yaxis_title="Количество случаев",
    legend_title="Погода",
    font=dict(size=14),
    showlegend=True,
    legend=dict(
        orientation="h",  
        y=-0.2,  
        x=0.5,
        xanchor='center',
        yanchor='top'
    ),
    margin=dict(l=30, r=30, t=50, b=50),  
    plot_bgcolor="white", 
)

fig.update_xaxes(showgrid=False, zeroline=False) 
fig.update_yaxes(showgrid=True, zeroline=False, gridcolor="lightgrey")  

hour_type_titles = {
    'night': 'Ночь',
    'morning': 'Утро',
    'afternoon': 'День',
    'evening': 'Вечер'
}
fig.for_each_annotation(lambda a: a.update(text=hour_type_titles[a.text.split('=')[1]]))
fig.show()
fig.write_html("graph2.html")



### traffic

fig = px.box(
    data,
    x='weekday', 
    y='traffic',  
    color='weekday', 
    title="Распределение интенсивности трафика по дням недели"
)

fig.update_layout(
    title=dict(
        text="Распределение интенсивности трафика по дням недели",
        font=dict(size=18),
        x=0.5
    ),
    xaxis_title="День недели",
    yaxis_title="Интенсивность трафика",
    font=dict(size=14),
    plot_bgcolor="white",
    margin=dict(l=40, r=40, t=50, b=50)
)

fig.show()
fig.write_html("graph3.html")
