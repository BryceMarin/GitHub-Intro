import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div([
    html.H2("Welcome to my Home Page"),
    html.P("This is a simple multipage Dash project")
])