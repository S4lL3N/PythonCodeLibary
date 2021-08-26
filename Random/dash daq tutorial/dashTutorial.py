import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
import webbrowser

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#external_stylesheets = ['Python\app.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.Gauge(
        id='my-gauge',
        label="DashTutorial",
        value=7
    ),
    dcc.Slider(
        id='my-gauge-slider',
        min=0,
        max=10,
        step=1,
        value=5
    ),
])


@app.callback(
    dash.dependencies.Output('my-gauge', 'value'),
    [dash.dependencies.Input('my-gauge-slider', 'value')]
)
def update_output(value):
    return value

webbrowser.open("http://127.0.0.1:8050")

if __name__ == '__main__':
    app.run_server(debug=True)