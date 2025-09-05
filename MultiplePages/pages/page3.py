from dash import html, register_page, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from pathlib import Path

register_page(__name__, path="/page3", name="Page 3")

DataPath = Path(__file__).resolve().parent.parent / "data" / "electricity_prices.csv"
df = pd.read_csv(DataPath)
df["year"] = pd.to_numeric(df["year"]).astype(int)

layout = html.Div(
    style = {"backgroundColor":"#293831", "padding":"20px"},
    children = [
    html.H1("Electricty Prices by US State", style = {"color":"#CDD6D3", "textAlign":"center"}),
    dcc.Slider(
        id = "year-slider",
        min = int(df["year"].min()),
        max = int(df["year"].max()),
        value = int(df["year"].min()),
        marks = {str(y): str(y) for y in sorted(df["year"].unique())},
        step = None,
        tooltip = {"placement":"bottom", "always_visible":True}
    ),
    html.Br(),
    dcc.Graph(id="choropleth-map")
    ]
)

@callback(
    Output("choropleth-map", "figure"),
    Input("year-slider", "value")
)

def update_map(selected_year):
    d = df[df["year"]==selected_year]
    fig = px.choropleth(
        d,
        locations = "state",
        locationmode = "USA-states",
        color = "price",
        scope = "usa",
        color_continuous_scale = "Reds",
        labels = {"price": "Price (cents/kWh)"},
        title = f"Residential Electricity Prices - {selected_year}"
    )
    fig.update_layout(
        geo = dict(bgcolor = "#B9975B"), # background color around map
        paper_bgcolor = "#32453C", # background color on everything else
        font_color = "white",
        margin = dict(l = 10, r = 10, t = 50, b = 10)
    )
    return fig