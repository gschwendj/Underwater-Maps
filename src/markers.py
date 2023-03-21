#!/usr/bin/env python
"""defines the different markers for the divesites

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

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__email__ = "jo.gschwend@"
__status__ = "Production"

import plotly.graph_objects as go


class Markers:
    def __init__(self) -> None:
        self.betlis = go.Scatter3d(
            x=[274],
            y=[124],
            z=[1],
            mode="markers+text",
            text=["Einstieg"],
        )
        self.au = go.Scatter3d()
        self.zollerbucht = go.Scatter3d()
        self.murg_west = go.Scatter3d()
        self.mols = go.Scatter3d()
        self.terlinden = go.Scatter3d()
        self.tiefenwinkel = go.Scatter3d()
        self.broder = go.Scatter3d()
        self.zick_zack = go.Scatter3d()
