import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Output, Input
from app import app

# Connect to the layout and callbacks of each tab
from MonkeyPox_Cases import Cases_layout
from Country_Cases import country_layout
from Daily_Cases import daily_layout

# # The View part, shows the main layout
# it consists of 3-tabs

app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Daily Cases", tab_id="tab-daily", labelClassName="text-success font-weight-bold",
                        activeLabelClassName="text-danger"),
                dbc.Tab(label="Global Cases", tab_id="tab-country", labelClassName="text-success font-weight-bold",
                        activeLabelClassName="text-danger"),
                dbc.Tab(label="Confirmed Cases and Symptoms", tab_id="tab-cases",
                        labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger")
            ],
            id="tabs",
            active_tab="tab-daily",
        ),
    ], className="mt-3"
)

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Monkeypox Analytics Dashboard",
                            style={"textAlign": "center"}), width=18)),
    html.Hr(),
    dbc.Row(dbc.Col(app_tabs, width=18), className="mb-3"),
    html.Div(id='content', children=[])

])


# The Controller part, where the View components interact with the Model
# return a tab chosen by the user
@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-country":
        return country_layout
    elif tab_chosen == "tab-cases":
        return Cases_layout
    elif tab_chosen == "tab-daily":
        return daily_layout
    return html.P("This shouldn't be displayed for now...")


if __name__ == '__main__':
    app.run_server(debug=True)
