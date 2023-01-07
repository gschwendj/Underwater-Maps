#!/usr/bin/env python
"""Process and save the z data for dive site Au Betlis

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
import process_data.process_data as process

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__email__ = "jo.gschwend@"
__status__ = "Production"


bathy3d_chlv95_ln02_2729_1221 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/swissBATHY3D_CHLV95_LN02_2729_1221.xyz"
)
bathy3d_chlv95_ln02_2729_1222 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/swissBATHY3D_CHLV95_LN02_2729_1222.xyz"
)
swissalti3d_chlv95_ln02_2729_1221 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/SWISSALTI3D_0.5_XYZ_CHLV95_LN02_2729_1221.xyz"
)
swissalti3d_chlv95_ln02_2729_1222 = process.loadXyz(
    "/home/gscd/Documents/swisstopo_geodata/walensee/SWISSALTI3D_0.5_XYZ_CHLV95_LN02_2729_1222.xyz"
)

altitude = 419.75  # waterlevel of lake

bathy3d_chlv95_ln02_2729_1221 -= altitude  # subtract the water level
bathy3d_chlv95_ln02_2729_1222 -= altitude
swissalti3d_chlv95_ln02_2729_1221 -= altitude
swissalti3d_chlv95_ln02_2729_1222 -= altitude

swissalti3d_chlv95_ln02_2729_1221 = process.edgeDetection(
    swissalti3d_chlv95_ln02_2729_1221, 0
)
swissalti3d_chlv95_ln02_2729_1222 = process.edgeDetection(
    swissalti3d_chlv95_ln02_2729_1222, 0
)

elevation_2729_1221 = process.combineLandWater(
    swissalti3d_chlv95_ln02_2729_1221, bathy3d_chlv95_ln02_2729_1221
)
elevation_2729_1222 = process.combineLandWater(
    swissalti3d_chlv95_ln02_2729_1222, bathy3d_chlv95_ln02_2729_1222
)

elevation_data = np.append(elevation_2729_1221, elevation_2729_1222, 0)
elevation_data = elevation_data[600:1200, :]
elevation_data[elevation_data > 125] = 125
elevation_data[elevation_data < -125] = -125
elevation_data = process.interpolateNan(elevation_data, "cubic")

np.save("/home/gscd/Documents/Underwater-Maps/npy_data/betlis", elevation_data)
