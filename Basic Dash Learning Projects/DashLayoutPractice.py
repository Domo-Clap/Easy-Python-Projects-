# Imports dash_table and dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Imports pandas to import csv file
import pandas as pd

# Imports plotly to create a histogram
import plotly.express as px

# Initializes the app
app = Dash(__name__)

# Sets colors to be used when called upon for HTML elements
colors = {'background': '#111111',
          'text': '#7FDBFF'
}

# Creates a dataframe with 3 columns: Fruit, Amount, and City
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Creates a bar graph called fig and uses the data from df to populate the graph
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(plot_bgcolor=colors['background'],
                  paper_bgcolor=colors['background'],
                  font_color=colors['text']
)

# Sets the app layout for the UI
app.layout = html.Div(children=[
    # Header with a text string
    html.H1(children='Hello Dash',
            style={'textAlign': 'center',
                   'color': colors['text']
            }
    ),

    # General text string under the header
    html.Div(children='Dash: A web application framework for your data.',
             style={
                    'textAlign': 'center',
                    'color': colors['text']
             }
    ),

    # Displays the graph made prior under the text string
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Runs the app
if __name__ == '__main__':
    app.run(debug=True)
