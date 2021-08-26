# -*- coding: utf-8 -*-
import dash
from dash import *
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

import webbrowser



#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['Python\app.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

theme = {
    'dark': True,
    'background-color': '#303030',
    'color': 'white'
}

app.layout = html.Div(children=[
    html.H1(children='Hello Dash(#1)'),

    html.Div(children='''
        Dash: A web application framework for Python(#2).
    '''),

    daq.Gauge(
        color={"gradient":True,"ranges":{"green":[0,6],"yellow":[6,8],"red":[8,10]}},
        value=3,
        label='Gauge #1',
        max=10,
        min=0,
    ),

    daq.Gauge(
        color="#9B51E0",
        value=5,
        label='Gauge #2',
        max=5,
        min=0,
    ),

    daq.Gauge(
        showCurrentValue=True,
        units="MPH",
        value=5,
        label='Gauge #3',
        max=10,
        min=0,
    ),

    daq.Gauge(
        size=200,
        value=2,
        label='gauge #4',
        theme="dark"

    ),

    daq.Thermometer(
        min=95,
        max=105,
        value=100,
        showCurrentValue=True,
        units="C"
    )    
    
    
])#end app layout

webbrowser.open("http://127.0.0.1:8050")

if __name__ == '__main__':
    app.run_server(debug=True)