# Imports dash_table and dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Imports pandas to import csv file
import pandas as pd

# Imports plotly to create a histogram
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Initializes the app
app = Dash(__name__)

# Sets the app layout for the UI
app.layout = html.Div([
    # Creates a graph with an assigned id
    dcc.Graph(id='graph-with-slider'),
    # Creates a slider that has min and max values relative to the year column of the df
    # Used to change the year being shown. Has an id assigned for later use in callback function
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])

# Callback starts here. Used to change the data shown in the graph output.
@callback(
    # Output is the graph figure
    Output('graph-with-slider', 'figure'),
    # Input is the slider's year value
    Input('year-slider', 'value'))
# Actual callback function. Updates the graph figure, or the output, by passing in a specific year value from the slider
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run(debug=True)