# Imports dash_table and dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Imports pandas to import csv file
import pandas as pd

# Imports plotly to create a histogram
import plotly.express as px

# Initializes the app
app = Dash(__name__)

# Sets the app layout for the UI
app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    # Creates an input box for a user to enter text. Assigns an id to the object and makes it accept text
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    # Creates an output object to display a value and assigns it an id
    html.Div(id='my-output'),

])

# Callback used to change the output value based upon the input value. Assigns the input and output to specific ids
# Input is the "value" property of the component that has the ID "my-input"
# Output is the "children" property of the component with the ID "my-output"
@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
# Callback function that will actually change the output object
def update_output_div(input_value):
    return f'Output: {input_value + "!"}'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
