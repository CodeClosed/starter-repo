import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load and prepare the data
df = pd.read_csv('data/formatted_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Create the Dash app
app = dash.Dash(__name__)

# Create the visualization
fig = px.line(
    df,
    x='date',
    y='sales',
    title='Pink Morsel Sales Before and After Price Increase',
    labels={'date': 'Date', 'sales': 'Sales ($)'}
)

# App layout
app.layout = html.Div(children=[
    html.H1(
        children='Soul Foods - Pink Morsel Sales Visualizer',
        style={'textAlign': 'center', 'color': '#333333'}
    ),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
