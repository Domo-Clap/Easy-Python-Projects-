# Imports dash_table and dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Imports pandas to import csv file
import pandas as pd

# Imports plotly to create a histogram
import plotly.express as px

# Initializes the app
app = Dash(__name__)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

# Sets the app layout for the UI
app.layout = html.Div([
    html.Div([

        # Creates a dropdown box and a set of radio items
        html.Div([
            # Specifically creates the dropdown box with specific data from the df as options. Fertility rate. Assigned to x-axis
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Fertility rate, total (births per woman)',
                id='xaxis-column'
            ),
            # Specifically creates the radio items with 2 options: Linear and Log. Assigned to x-axis
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='xaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        # Creates another dropdown box and set of radio items
        html.Div([
            # Specifically creates the dropdown box with specific data from the df as options. Life Expectancy. Assigned to y-axis
            dcc.Dropdown(
                df['Indicator Name'].unique(),
                'Life expectancy at birth, total (years)',
                id='yaxis-column'
            ),
            # Specifically creates the radio items with 2 options: Linear and Log. Assigned to y-axis
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    # Creates a graph with an assigned id
    dcc.Graph(id='indicator-graphic'),

    # Creates a slider that has min and max values relative to the year column of the df
    # Used to change the year being shown. Has an id assigned for later use in callback function
    dcc.Slider(
        df['Year'].min(),
        df['Year'].max(),
        step=None,
        id='year--slider',
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},

    )
])

# Callback starts here. Used to change the data shown in the graph output.
@callback(
    # Output is the graph figure
    Output('indicator-graphic', 'figure'),
    # Input is the x and y axis, and the year slider
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year--slider', 'value'))
# Actual callback function. Updates the graph figure, or the output, by passing in specific input from the above widgets
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig


if __name__ == '__main__':
    app.run(debug=True)