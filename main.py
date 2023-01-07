#!/usr/bin/env python
"""main file that host the dash app

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

from colorscale import Colorscale

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__email__ = "jo.gschwend@"
__status__ = "Production"

app = Dash(__name__)
colorscale = Colorscale()

elevation_data_betlis = np.load(
    "/home/gscd/Documents/Underwater-Maps/npy_data/betlis.npy"
)
elevation_data_au = np.load("/home/gscd/Documents/Underwater-Maps/npy_data/au.npy")

d = {
    "Tauchplatz": ["Betlis", "Au"],
    "z_data": [elevation_data_betlis, elevation_data_au],
    "colorscale": [colorscale.betlis, colorscale.au],
}

df = pd.DataFrame(data=d)

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    df["Tauchplatz"].unique(),
                    "Betlis",
                    id="tauchplatz",
                ),
            ],
            style={"width": "48%", "height": "5vh", "display": "inline-block"},
        ),
        html.Div(
            [
                dcc.Checklist(["show contours"], ["show contours"], id="show_contours"),
                "contours width: ",
                dcc.Input(id="contours_width", value=20, type="number"),
            ],
            style={
                "width": "48%",
                "height": "5vh",
                "float": "right",
                "display": "inline-block",
            },
        ),
        dcc.Graph(id="indicator-graphic", style={"width": "99vw", "height": "92vh"}),
        # dcc.Graph(id="indicator-graphic", style={"width": "99vw", "height": "92vh"}),
    ]
)


@app.callback(
    Output("indicator-graphic", "figure"),
    Input("tauchplatz", "value"),
    Input("show_contours", "value"),
    Input("contours_width", "value"),
)
def update_graph(tauchplatz, contours, contours_width):

    fig = go.Figure(
        data=[
            go.Surface(
                z=df.set_index("Tauchplatz").at[tauchplatz, "z_data"],
                colorscale=df.set_index("Tauchplatz").at[tauchplatz, "colorscale"],
                showscale=False,
            )
        ]
    )

    if contours and contours_width > 0:
        contours_start = 0
        while contours_start < 120:
            contours_start += contours_width
        fig.update_traces(
            contours_z=dict(
                show=True,
                start=-contours_start,
                end=contours_width,
                size=contours_width,
            )
        )

    fig.update_layout(
        scene_aspectmode="data",
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            zaxis=dict(showgrid=False, zeroline=False, visible=False),
        ),
    )
    fig.update_coloraxes(showscale=False)

    fig.update_layout(
        title="Tauchplatz {}".format(tauchplatz),
        font=dict(size=18),
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
