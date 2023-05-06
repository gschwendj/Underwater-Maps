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

textsize = 30


class Markers:
    def __init__(self) -> None:
        self.betlis = [
            dict(
                x=540,
                y=196,
                text="Einstieg Schiffstation",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=427,
                y=325,
                text="Einstieg Bucht",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=243,
                y=499,
                text="Einstieg Strassenlaterne",
                bgcolor="white",
                bordercolor="black",
            ),
        ]
        self.au = [
            dict(
                x=324,
                y=177,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.zollerbucht = [
            dict(
                x=180,
                y=573,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.murg_west = [
            dict(
                x=120,
                y=120,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.mols = [
            dict(
                x=369,
                y=425,
                text="Einstieg Hafen Mols Untiefe",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=566,
                y=438,
                text="Einstieg Hafen Mols West",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=633,
                y=488,
                text="Einstieg Hafen Mols Ost",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=994,
                y=646,
                text="Einstieg Känzeli",
                bgcolor="white",
                bordercolor="black",
            ),
        ]
        self.terlinden = [
            dict(
                x=127,
                y=174,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.tiefenwinkel = [
            dict(
                x=573,
                y=86,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.broder = [
            dict(
                x=450,
                y=67,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.zick_zack = [
            dict(
                x=245,
                y=110,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
