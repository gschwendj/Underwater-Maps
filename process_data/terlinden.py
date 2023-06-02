#!/usr/bin/env python
"""Process and save the z data for dive site Terlinden

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


bathy3d_chlv95_ln02_2691_1233 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/zuerichsee/swissBATHY3D_CHLV95_LN02_2685_1242.xyz"
)
swissalti3d_chlv95_ln02_2691_1233 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/zuerichsee/SWISSALTI3D_0.5_XYZ_CHLV95_LN02_2685_1242.xyz"
)

altitude = 405.95  # waterlevel of lake

bathy3d_chlv95_ln02_2691_1233 -= altitude  # subtract the water level
swissalti3d_chlv95_ln02_2691_1233 -= altitude

swissalti3d_chlv95_ln02_2691_1233 = process.edgeDetection(
    swissalti3d_chlv95_ln02_2691_1233, 0
)

elevation_data = process.combineLandWater(
    swissalti3d_chlv95_ln02_2691_1233, bathy3d_chlv95_ln02_2691_1233
)

z_max = 10
z_min = -70
elevation_data = elevation_data[450:750, 600:800]
elevation_data[elevation_data > z_max] = z_max
elevation_data[elevation_data < z_min] = z_min
elevation_data = process.interpolateNan(elevation_data, "linear")


np.save("{}/npy_data/terlinden".format(Path(__file__).parent.parent), elevation_data)
