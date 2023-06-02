#!/usr/bin/env python
"""Process and save the z data for dive site Zick-Zack

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
__version__ = "v1.0"
__maintainer__ = "Jonas Gschwend"
__status__ = "Production"


bathy3d_chlv95_ln02_2730_1220 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/swissBATHY3D_CHLV95_LN02_2730_1220.xyz"
)
bathy3d_chlv95_ln02_2731_1220 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/swissBATHY3D_CHLV95_LN02_2731_1220.xyz"
)
swissalti3d_chlv95_ln02_2730_1220 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/SWISSALTI3D_0.5_XYZ_CHLV95_LN02_2730_1220.xyz"
)
swissalti3d_chlv95_ln02_2731_1220 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/SWISSALTI3D_0.5_XYZ_CHLV95_LN02_2731_1220.xyz"
)


altitude = 419.75  # waterlevel of lake

bathy3d_chlv95_ln02_2730_1220 -= altitude  # subtract the water level
bathy3d_chlv95_ln02_2731_1220 -= altitude
swissalti3d_chlv95_ln02_2730_1220 -= altitude
swissalti3d_chlv95_ln02_2731_1220 -= altitude

swissalti3d_chlv95_ln02_2730_1220 = process.edgeDetection(
    swissalti3d_chlv95_ln02_2730_1220, 0
)
swissalti3d_chlv95_ln02_2740_1219 = process.edgeDetection(
    swissalti3d_chlv95_ln02_2731_1220, 0
)

elevation_2730_1220 = process.combineLandWater(
    swissalti3d_chlv95_ln02_2730_1220, bathy3d_chlv95_ln02_2730_1220
)
elevation_2731_1220 = process.combineLandWater(
    swissalti3d_chlv95_ln02_2740_1219, bathy3d_chlv95_ln02_2731_1220
)

elevation_data = np.append(elevation_2730_1220, elevation_2731_1220, 1)
elevation_data = elevation_data[95:495, 720:1200]
elevation_data[elevation_data > 125] = 125
elevation_data[elevation_data < -125] = -125
elevation_data = process.interpolateNan(elevation_data, "linear")

np.save(
    "{}/npy_data/zick_zack".format(Path(__file__).parent.parent),
    elevation_data,
)
