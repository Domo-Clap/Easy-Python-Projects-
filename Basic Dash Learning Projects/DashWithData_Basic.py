# Imports dash_table and dash
from dash import Dash, html, dash_table

# Imports pandas to make dataframe from the imported csv file
import pandas as pd

# Uses pandas to load the csv data into a dataframe for later usage
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initializes dash app
app = Dash(__name__)

# Defines the layout for the dash app
app.layout = html.Div([
    # Creates a basic text string in the dash app
    html.Div(children='My First App with Data'),
    # Then it creates a dash_table object with data from the imported csv file.
    # It limits the number of rows to 10 per page.
    dash_table.DataTable(data = df.to_dict('records'), page_size=10)
])



if __name__ == '__main__':
    app.run(debug=True)

