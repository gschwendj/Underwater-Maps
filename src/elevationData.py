#!/usr/bin/env python
"""loads all elevation data of the dive sites

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

path = Path(__file__).parent.parent


class ElevationData:
    def __init__(self) -> None:
        self.betlis = np.load("{}/npy_data/betlis.npy".format(path))
        self.au = np.load("{}/npy_data/au.npy".format(path))
        self.zollerbucht = np.load("{}/npy_data/zollerbucht.npy".format(path))
        self.murg_west = np.load("{}/npy_data/murg_west.npy".format(path))
        self.mols = np.load("{}/npy_data/hafen_mols_kaenzeli.npy".format(path))
