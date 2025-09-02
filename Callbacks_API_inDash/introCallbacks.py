# a callback is a Python function automatically triggered when an Input property changes, updating one or more Output properties
# can have multiple inputs in a single callback -- the function will run whenever any of these inputs changes
# multiple outputs returns a tuple/list with one value for each output() in the order declared

# callback_example.py
# from dash import x, xx, x, etc. <-- means we don't have to call dash.x everytime
from dash import Dash, html, dcc, Input, Output, callback

app = Dash(__name__)
app.title = "Callback Example"

app.layout = html.Div(
    style={"maxWidth": 900, "margin": "40px auto", "fontFamily": "Georgia, serif"},
    # "children" here is a property name
    children=[
        html.H1("Callback Example"),
        html.Ul([
            html.Li(["Input box’s ", html.Code("value"), " property updates output text"])
        ]),
        # dcc = dash.dcc = Dash Core Components <-- necessary!
        dcc.Input(
            id="text-in",
            type="text",
            placeholder="type here…",
            style={"width": "100%", "fontSize": "48px", "padding": "8px"},
        ),
        html.Div(id="text-out", style={"fontSize": "64px", "marginTop": "20px"}),
    ],
)

# @app.callback decorate links inputs to outputs
@callback(Output(component_id="text-out", component_property="children"), 
          # decorator output -- where the result will be sent
          Input(component_id="text-in", component_property="value"))
          # decorator input -- which component's property will trigger the function when it changes
def show_text(value):
    return f"Text: {value or ''}"

if __name__ == "__main__":
    app.run(debug=True)
