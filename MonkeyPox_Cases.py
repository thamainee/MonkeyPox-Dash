import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# The model part, we read data from the csv file and clean the data
df = pd.read_csv("Monkey_Pox_Cases_Worldwide.csv")
monkeypox_deprecated_df = pd.read_csv("Worldwide_Case_Detection_Timeline.csv", dtype=str)
temp_df = pd.DataFrame(monkeypox_deprecated_df['Symptoms'].value_counts()).reset_index()
temp_df = temp_df.append(
    pd.DataFrame({'index': 'multiple or other', 'Symptoms': temp_df.loc[temp_df['Symptoms'] < 5]['Symptoms'].sum()},
                 index=[0]))
temp_df = temp_df.loc[temp_df['Symptoms'] > 4]

# The View part, shows the dashboard layout to the user
# We declare the Labels, Dropdowns, Page separating line, Tittles and Graphs
Cases_layout = html.Div([
    html.H1("Distribution of Symptoms", style={"textAlign": "center"}),
    html.Hr(),
    dcc.Graph(figure=px.pie(data_frame=temp_df, names='index', values='Symptoms',
                            color_discrete_sequence=px.colors.sequential.Plasma, hole=0.5)),
    html.Label("Pie chart showcasing the various symptoms"),
    html.Hr(),
    html.H1(" Travel History vs Confirmed Cases", style={"textAlign": "center"}),  # Graph title
    dcc.Graph(figure=px.scatter(df, x='Travel_History_Yes', y='Confirmed_Cases',color='Hospitalized', hover_name='Country')),
    html.Label("Scatter plot graph visualizing patients' travel history"),
])
