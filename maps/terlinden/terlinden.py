#!/usr/bin/env python
"""draws a 2D map of the dive site Terlinden

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
import numpy as np
import plotly.graph_objects as go
from pathlib import Path
import os, sys

current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(os.path.dirname(current))
sys.path.append(parent_directory)
from src.markers import Markers
from src.colorscale import Colorscale
from src.elevationData import ElevationData

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__email__ = "jo.gschwend@"
__status__ = "Production"


colorscale = Colorscale().maps
annotations = Markers().terlinden
annotations[0].update(dict(showarrow=True, arrowhead=2, arrowsize=2, ax=50, ay=-50))

fig = go.Figure(
    data=[
        go.Contour(
            colorscale=colorscale,
            z=ElevationData().terlinden,
            showscale=False,
            # contours_coloring="none",
            contours=dict(
                showlabels=True,
                start=-125,
                end=0,
                size=5,
                labelfont=dict(  # label font properties
                    size=8,
                    color="white",
                ),
            ),
        )
    ]
)

fig.update_yaxes(
    scaleanchor="x",
    scaleratio=1,
)

fig.update_layout(
    title="Tauchplatz Terlinden",
    font=dict(size=18),
    annotations=annotations,
)

# fig.show()
fig.write_image("{}/terlinden.pdf".format(current), scale=4, width=705, height=1000)
