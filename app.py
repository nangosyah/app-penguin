import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
from palmerpenguins import load_penguins

# initialize the dashboard 
app = dash.Dash(__name__)


# load data
dat = load_penguins().dropna()

# define the layout
app.layout = html.Div(
    [
        # radio buttons for species selection
        html.Div(
            [
                html.Label('Species:'),
                dcc.RadioItems(
                    id="species-radio",
                    options=["Adelie", "Gentoo", "Chinstrap"],
                    value="Adelie",
                    inline=True,
                ),
            ]
        ),
        # graph container
        dcc.Graph(id="histogram-plot"),
    ]
)

@app.callback(
    Output("histogram-plot", "figure"),
    Input("species-radio", "value")
)
def update_plot(selected_species):
    # create two histograms

    # 1. All penguins (lightgray)
    all_penguins = go.Histogram(
    x=dat["bill_length_mm"].dropna(),
    xbins=dict(size=1),
    marker_color="#C2C2C4",
    name="All Penguins"
    )

    # 2. Selected species
    sel = dat[dat["species"] == selected_species]
    selected_penguins = go.Histogram(
        x=sel["bill_length_mm"].dropna(),
        xbins=dict(size=1),
        marker_color="#447099",
        name=f"{selected_species}",
    )

    # create the figure
    fig = go.Figure(data=[all_penguins, selected_penguins])

    # update layout
    fig.update_layout(
        barmode="overlay",
        template="plotly_white",
        showlegend=False,
    )

    return fig


# run the app
if __name__ == "__main__":
    app.run()