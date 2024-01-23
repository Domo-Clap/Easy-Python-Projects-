# Imports dash_table and dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Imports pandas to import csv file
import pandas as pd

# Imports plotly to create a histogram
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initializes the app
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Sets the app layout for the UI
app.layout = html.Div([

    # Creates an input box that the user can interact with. Uses the number data type
    dcc.Input(
        id='num-multi',
        type='number',
        value=5
    ),

    # Creates a table to be displayed in the webpage. Has 5 rows all assigned their own id.
    # Each row has two columns: 1 for the math equation, and a 2nd for the result of the equation
    html.Table([
        html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
        html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
        html.Tr([html.Td([2, html.Sup('x')]), html.Td(id='twos')]),
        html.Tr([html.Td([3, html.Sup('x')]), html.Td(id='threes')]),
        html.Tr([html.Td(['x', html.Sup('x')]), html.Td(id='x^x')]),
    ]),
])

# Callback starts here. Used to change the data shown in the table output.
@callback(
    Output('square', 'children'),
    Output('cube', 'children'),
    Output('twos', 'children'),
    Output('threes', 'children'),
    Output('x^x', 'children'),
    Input('num-multi', 'value'))
# Actual callback function. Returns the results of the performed math calculations based on the input. Output will change based on this
def callback_a(x):
    return x**2, x**3, 2**x, 3**x, x**x


if __name__ == '__main__':
    app.run(debug=True)