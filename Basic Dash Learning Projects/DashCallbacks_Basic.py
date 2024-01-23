# Imports dash_table and dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Imports pandas to import csv file
import pandas as pd

# Imports plotly to create a histogram
import plotly.express as px

# Imports and assigns the csv file to the df variable
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initializes the app
app = Dash(__name__)

# Sets the app layout for the UI
app.layout = html.Div([
    # Displays a basic text string in the UI
    html.Div(children='My First App with Data, Graph, and Controls'),
    # Adds a page break of sorts
    html.Hr(),
    # Creates a widget which is 3 radio buttons. Basically a widget that has 3 circles that are selectable options.
    # Also assigned an id to the widget for the callback function later as the input
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    # Creates a table using the imported csv file
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    # Displays the data from the csv as a histogram and assigns it an id for later use in the callback function
    dcc.Graph(figure={}, id='controls-and-graph')
])

# Start of the callback function
@callback(
    # Used to change the output of the histogram. Has the component_id set to the histogram id as a reference.
    # The component property references the figure variable of the histogram. Basically, the histogram is the output of the function
    Output(component_id='controls-and-graph', component_property='figure'),
    # Used to get input to change the histogram. Has the component_id set to the radio buttons as a reference
    # The component property references the value variable for the radio buttons. This makes it so input is whichever radio button is selected
    Input(component_id='controls-and-radio-item', component_property='value')
)
# Here is the actual callback function. Takes input for the column chosen which is basically the component property for the callback Input
def update_graph(col_chosen):
    # Based upon the column chosen via the radio buttons, the fig will change, which will alter the graph
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    # Returns the new graph to be displayed
    return fig

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

