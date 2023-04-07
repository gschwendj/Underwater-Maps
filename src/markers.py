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
                z=0,
                text="Einstieg Schiffstation",
                ax=0,
                ay=-50,
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=427,
                y=325,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg Bucht",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=243,
                y=499,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg Strassenlaterne",
                bgcolor="white",
                bordercolor="black",
            ),
        ]
        self.au = [
            dict(
                x=324,
                y=177,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.zollerbucht = [
            dict(
                x=180,
                y=573,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.murg_west = [
            dict(
                x=120,
                y=120,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.mols = [
            dict(
                x=369,
                y=425,
                z=0,
                text="Einstieg Hafen Mols Untiefe",
                ax=0,
                ay=-50,
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=566,
                y=438,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg Hafen Mols West",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=633,
                y=488,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg Hafen Mols Ost",
                bgcolor="white",
                bordercolor="black",
            ),
            dict(
                x=994,
                y=646,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg Känzeli",
                bgcolor="white",
                bordercolor="black",
            ),
        ]
        self.terlinden = [
            dict(
                x=127,
                y=174,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.tiefenwinkel = [
            dict(
                x=573,
                y=86,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.broder = [
            dict(
                x=450,
                y=67,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.zick_zack = [
            dict(
                x=245,
                y=110,
                z=0,
                ax=0,
                ay=-50,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
