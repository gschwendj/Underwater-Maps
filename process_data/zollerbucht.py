#!/usr/bin/env python
"""Process and save the z data for dive site Zollerbucht

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
from pathlib import Path
import processData as process

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__status__ = "Production"

bathy3d_chlv95_ln02_2687_1239 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/zuerichsee/swissBATHY3D_CHLV95_LN02_2687_1239.xyz"
)
swissalti3d_chlv95_ln02_2687_1239 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/zuerichsee/SWISSALTI3D_0.5_XYZ_CHLV95_LN02_2687_1239.xyz"
)

altitude = 405.94  # waterlevel of lake

bathy3d_chlv95_ln02_2687_1239 -= altitude  # subtract the water level
swissalti3d_chlv95_ln02_2687_1239 -= altitude

swissalti3d_chlv95_ln02_2687_1239 = process.edgeDetection(
    swissalti3d_chlv95_ln02_2687_1239, 3
)

elevation_data = process.combineLandWater(
    swissalti3d_chlv95_ln02_2687_1239, bathy3d_chlv95_ln02_2687_1239
)

elevation_data = elevation_data[:700, :550]
elevation_data[elevation_data > 42.8] = 42.8
elevation_data[elevation_data < -125] = -125
elevation_data = process.interpolateNan(elevation_data)

np.save("{}/npy_data/zollerbucht".format(Path(__file__).parent.parent), elevation_data)


colorscale = [
    [0, "black"],
    [0.1875, "MidnightBlue"],
    [0.375, "Blue"],
    [0.5625, "DodgerBlue"],
    [0.75, "Turquoise"],
    [0.75, "Green"],
    [1, "Green"],
]

import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Surface(z=elevation_data, colorscale=colorscale, showscale=False)]
)

fig.update_traces(
    contours_z=dict(
        show=True,
        start=-100,
        end=20,
        size=20,
    )
)

fig.update_layout(
    scene_aspectmode="data",
    scene=dict(
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        zaxis=dict(showgrid=False, zeroline=False),
    ),
)

fig.update_layout(
    title="Tauchplatz Zollerbucht",
    font=dict(size=18),
)
fig.show()
