import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from app import app

# The model part, we read data from the csv file and clean the data
df = pd.read_csv("Monkey_Pox_Cases_Worldwide.csv")

# The View part, shows the dashboard layout to the user
# We declare the Labels, Dropdowns, page separating line, Tittles and Graphs
country_layout= html.Div([
    html.H1(" Type Of Cases vs Countries", style={"textAlign": "center"}),  # Graph title
    html.Div(id="output_cases", children=[]),
    html.Label('Select type of case'),                      # Dropdown label
    dcc.Dropdown(id="y_case_type", clearable=False,
                 value='Confirmed_Cases',
                 options=[{'label': y, 'value': y} for y in df[:2]],
                 style={'width': '50%'}),
    dcc.Graph(id='bar_graph', figure={}),
    html.Label("Bar graph visualizing total number of Monkeypox type of cases for a specific country"),
    html.Hr(),
    html.H1(" Map of Confirmed Cases", style={"textAlign": "center"}),
    html.Hr(),
    dcc.Graph(id='choropleth_graph', figure={}),
    html.Label("Choropleth map visualizing total number of Monkeypox cases worldwide"),

])

# The Controller part, where the View components interact with the Model
# Initialise/input the csv file data to the graphs and dropdown, and get the output
@app.callback(
    [Output(component_id='bar_graph', component_property='figure'),
     Output(component_id='choropleth_graph', component_property='figure')],
    Input(component_id='y_case_type', component_property='value')
)
# The function return bar graph to output1, and choropleth graph(Geography map) to output2
def interactive_graph(y_axis):
    bar_graph_fig = px.histogram(data_frame=df, x='Country', y=y_axis, hover_name='Country', color='Country',height=700
                                 )
    choropleth_fig = px.choropleth(df, locations="Country",
                    color="Confirmed_Cases",
                    hover_name="Country",
                    color_continuous_scale=px.colors.sequential.Plasma,
                    locationmode= 'country names' ,
                    range_color=[500,30000],projection='natural earth',
                    scope ='world')
    return bar_graph_fig,choropleth_fig
