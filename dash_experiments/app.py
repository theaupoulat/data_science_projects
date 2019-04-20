# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# colors = {"background":"#111111", 'text' : '#7FDBFF'}

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app.layout = html.Div([
    dcc.Graph(id = 'graph_with_slider'),
    dcc.Slider(
        id = 'year-slider',
        min = df['year'].min(),
        max = df['year'].max(),
        value = df['year'].min(),
        marks = {str(year): str(year) for year in df["year"].unique()}
    )
    ])

@app.callback(
    Output('graph_with_slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df.continent == i]
        traces.append(go.Scatter(
            x = df_by_continent["gdpPercap"],
            y = df_by_continent["lifeExp"],
            text = df_by_continent['country'],
            mode = 'markers',
            opacity = 0.7,
            marker = {
                'size':15,
                'line':{'width':0.5, 'color' : 'white'}
            },
            name = i
        ))
    return {
        'data': traces,
        'layout' : go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }



if __name__ == '__main__':
    app.run_server(debug=True)
























'''
    id = 'life-exp-vs-gdp',
    figure = {
        'data':[
            go.Scatter(
                x = df[df['continent'] == i]['gdp per capita'],
                y = df[df['continent'] == i]['life expectancy'],
                text = df[df['continent'] == i]['country'],
                mode = 'markers',
                opacity = 0.7,
                marker = {
                    'size':15,
                    'line':{'width':0.5, 'color':'white'}
                },
                name = i
            ) for i in df.continent.unique()
        ],
        'layout': go.Layout(
            xaxis = { 'title': 'GDP Per Capita'},
            yaxis = {'title': 'Life Expectancy'},
            margin = {'l': 40, 'b':40, 't':10, 'r':10},
            legend = {'x':0, 'y':1},
            hovermode = 'closest'
        )
    }
    )
)


This is a basic try

app.layout= html.Div(style = { 'backgroundColor': colors['background']},children=[
    html.H1(style = {
    'textAlign': 'center',
    'color':colors['text']},
    children = "Hello Dash"),

    html.Div(children = ''
    Dash: a web application framework for Python'',
    style = {
        'textAlign' : 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id = 'example-graph',
        figure = {
            'data': [
                {'x': [1, 2, 3], 'y': [2, 4, 6], 'type':'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [1, 5, 7], 'type':'bar', 'name': 'SF'},
                ],
            'layout':{
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font':{
                    'color': colors['text']
                }
                }
            }
        )
    ])
'''
