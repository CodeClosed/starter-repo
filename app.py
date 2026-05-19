import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load and prepare the data
df = pd.read_csv('data/formatted_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# Create the Dash app
app = dash.Dash(__name__)
app.title = "Soul Foods - Pink Morsel Sales"

# App layout
app.layout = html.Div(className='app-container', children=[
    html.Div(className='header-container', children=[
        html.H1(
            className='header-title',
            children='Soul Foods - Pink Morsel Sales Visualizer'
        ),
        html.P(
            className='header-subtitle',
            children='Analyze regional sales trends around the January 15, 2021 price increase.'
        )
    ]),
    
    html.Div(className='controls-container', children=[
        html.Label('Select Region:', className='radio-label'),
        dcc.RadioItems(
            id='region-filter',
            className='radio-group',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True
        )
    ]),
    
    html.Div(className='chart-container', children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
        
    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=f'Pink Morsel Sales - {selected_region.capitalize()} Region(s)',
        labels={'date': 'Date', 'sales': 'Sales ($)'},
        color_discrete_sequence=['#ff4081']  # Pink color for pink morsels!
    )
    
    fig.update_layout(
        plot_bgcolor='#fcfcfc',
        paper_bgcolor='#ffffff',
        font_family='"Inter", "Helvetica", sans-serif',
        title_font_size=20,
        title_x=0.5,
        margin=dict(l=40, r=40, t=60, b=40),
        xaxis=dict(showgrid=True, gridcolor='#eeeeee'),
        yaxis=dict(showgrid=True, gridcolor='#eeeeee')
    )
    
    # Highlight the date of the price increase
    fig.add_vline(x='2021-01-15', line_width=2, line_dash="dash", line_color="#333333")
    fig.add_annotation(
        x='2021-01-15', 
        y=filtered_df['sales'].max() * 0.9 if not filtered_df.empty else 1,
        text="Price Increase", 
        showarrow=True, 
        arrowhead=1,
        ax=-50,
        ay=0
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
