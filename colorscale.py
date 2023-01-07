#!/usr/bin/env python
"""defines the different colorscales for the divesites

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


class Colorscale:
    def __init__(self) -> None:
        self.betlis = [
            [0, "black"],
            [0.125, "MidnightBlue"],
            [0.25, "Blue"],
            [0.375, "DodgerBlue"],
            [0.5, "Turquoise"],
            [0.5, "Green"],
            [1, "Green"],
        ]

        self.au = [
            [0, "black"],
            [0.1875, "MidnightBlue"],
            [0.375, "Blue"],
            [0.5625, "DodgerBlue"],
            [0.75, "Turquoise"],
            [0.75, "Green"],
            [1, "Green"],
        ]

        self.zollerbucht = [
            [0, "black"],
            [0.1875, "MidnightBlue"],
            [0.375, "Blue"],
            [0.5625, "DodgerBlue"],
            [0.75, "Turquoise"],
            [0.75, "Green"],
            [1, "Green"],
        ]