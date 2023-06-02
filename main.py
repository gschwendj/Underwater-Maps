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

import src.divesites as ds

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__status__ = "Production"

app = Dash(__name__)

divesites = [
    ds.Au(),
    ds.Betlis(),
    ds.Broder(),
    ds.Mols(),
    ds.Murg_west(),
    ds.Terlinden(),
    ds.Tiefenwinkel(),
    ds.Zick_zack(),
    ds.Zollerbucht(),
]

d = {
    "Tauchplatz": [site.name for site in divesites],
    "z_data": [site.elevationData for site in divesites],
    "colorscale": [site.colorscale for site in divesites],
    "markers": [site.markers for site in divesites],
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
        html.Div(children="Source: Federal Office of Topography swisstopo"),
    ]
)


@app.callback(
    Output("indicator-graphic", "figure"),
    Input("tauchplatz", "value"),
    Input("show_contours", "value"),
    Input("contours_width", "value"),
)
def update_graph(tauchplatz, show_contours, contours_width):
    fig = go.Figure(
        data=[
            go.Surface(
                z=df.set_index("Tauchplatz").at[tauchplatz, "z_data"],
                colorscale=df.set_index("Tauchplatz").at[tauchplatz, "colorscale"],
                showscale=False,
                hoverinfo="x+y+z",
            )
        ]
    )

    if show_contours and contours_width > 0:
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

    fig.update_coloraxes(showscale=False)

    annotations = df.set_index("Tauchplatz").at[tauchplatz, "markers"]
    for annotation in annotations:
        annotation.update(dict(z=0, ax=0, ay=-50))

    fig.update_layout(
        title="Tauchplatz {}".format(tauchplatz),
        font=dict(size=18),
        scene_aspectmode="data",
        scene=dict(
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
            zaxis=dict(showgrid=False, zeroline=False, visible=False),
            annotations=annotations,
        ),
    )

    return fig


if __name__ == "__main__":
    app.run_server(host="0.0.0.0")
