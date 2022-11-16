from dash.dependencies import Input, Output
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from app import app

# The model part, we read data from the csv file and clean the data
df_daily = pd.read_csv("Daily_Country_Wise_Confirmed_Cases.csv")
new_daily = df_daily.melt(id_vars=["Country"],
                          var_name="Date",
                          value_name="Value")

# The View part, shows the dashboard layout to the user
# We declare the Labels, Dropdowns, Page separating line, Tittles and Graphs
daily_layout = html.Div([
    html.H1("Daily Cases", style={"textAlign": "center"}),
    html.Hr(),
    html.Label('Select country'),  # Dropdown label
    dcc.Dropdown(id='country_dropdown', clearable=False,
                 options=new_daily['Country'].unique(),
                 value='Nigeria',
                 style={'width': '50%'}),
    dcc.Graph(id='line_graph', figure={}),
    html.Label("Daily cases shows the number of new cases reported for the most recent day of complete data",
               style={"textAlign": "center"}),
])


# The Controller part, where the View components interact with the Model
# Initialise/input the csv file data to the graphs and dropdown
@app.callback(
    Output(component_id='line_graph', component_property='figure'),
    Input(component_id='country_dropdown', component_property='value')
)
# The function return bar graph to output1, and scatter_plot graph to output2
def interactive_graph(y_axis):
    line_fig = px.line(data_frame=new_daily.loc[new_daily["Country"] == y_axis], x="Date", y='Value')
    return line_fig
