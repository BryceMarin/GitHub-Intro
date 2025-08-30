from dash import Dash, html
# initalizing app
app = Dash(__name__)
app.title = "My First Dash App"
# define layout
# everything within layout are html elements
# look on ppt for dash equivalents to html
app.layout = html.Div([
    html.H1("My Dashboard", style = {
        "color":"#281D5C",
        "fontSize":"20px",
        "backgroundColor":"#E898AA"
    }),
    html.P("This is a simple dashboard", style = {
        "border":"1px solid black",
        "padding":"20px",
        "margin":"50px"
    }),
    html.Br(), html.A("Click here", href="https://example.com")
])
# running the app
if __name__ == '__main__':
    app.run(debug = True, use_reloader = False)