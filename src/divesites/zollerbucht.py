#!/usr/bin/env python
"""stores the elevation data, color scale and markers for the divesite Zollerbucht

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
__version__ = "v1.0"
__maintainer__ = "Jonas Gschwend"
__status__ = "Production"


class Zollerbucht:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Zollerbucht, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.name = "Zollerbucht"
        path = Path(__file__).parent.parent.parent
        self.elevationData = np.load("{}/npy_data/zollerbucht.npy".format(path))
        self.markers = [
            dict(
                x=180,
                y=573,
                text="Einstieg",
                bgcolor="white",
                bordercolor="black",
            )
        ]
        self.colorscale = [
            [0, "black"],
            [0.1875, "MidnightBlue"],
            [0.375, "Blue"],
            [0.5625, "DodgerBlue"],
            [0.75, "Turquoise"],
            [0.75, "Green"],
            [1, "Green"],
        ]
