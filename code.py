import plotly.express as px 
import plotly.graph_objects as go
from palmerpenguins import load_penguins

dat = load_penguins().dropna()

selected_species = "Chinstrap"

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


fig
