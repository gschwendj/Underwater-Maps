#!/usr/bin/env python
"""stores the elevation data, color scale and markers for the divesite Mols

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

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__email__ = "jo.gschwend@"
__status__ = "Production"


class Mols:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Mols, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.name = "Känzeli und Hafen Mols"
        path = Path(__file__).parent.parent.parent
        self.elevationData = np.load("{}/npy_data/hafen_mols_kaenzeli.npy".format(path))
        self.markers = [
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
        border = 120 / (120 + 90)
        self.colorscale = [
            [0, "black"],
            [border / 4 * 1, "MidnightBlue"],
            [border / 4 * 2, "Blue"],
            [border / 4 * 3, "DodgerBlue"],
            [border, "Turquoise"],
            [border, "Green"],
            [1, "Green"],
        ]
