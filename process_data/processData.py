#!/usr/bin/env python
"""helper functions to run the code

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
from scipy import interpolate

__author__ = "Jonas Gschwend"
__copyright__ = "Copyright 2021, Jonas Gschwend"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonas Gschwend"
__status__ = "Production"


def loadXyz(file_name: str) -> np.ndarray | None:
    """Loads the xyz text data in an ndarray

    Parameters
    ----------
    file_name : str
        The name of the file to load in an array
    Returns
    -------
    elevation: np.ndarray
        array of the elevation data
        None for failure
    """
    try:
        data = np.loadtxt(file_name, skiprows=1)
    except:
        print("file not found")
        return None

    origin_long = int(data[0, 0] // 1000) * 1000
    origin_lat = int(data[0, 1] // 1000) * 1000

    elevation = np.full((1000, 1000), np.nan, dtype=float)

    # the land and underwaterdata have different sample sizes. hence the different shapes
    if np.shape(data)[0] == 4000000:
        # only store and order the z data in the surface matrix
        surface2000 = np.full((2000, 2000), np.nan, dtype=float)
        for elem in data:
            surface2000[
                int(2 * (elem[0] - origin_long - 0.25)),
                int(2 * (elem[1] - origin_lat - 0.25)),
            ] = elem[2]

        for i in range(1000):
            # combine 4 data points of the surface data to one and save them to the elevation data
            for j in range(1000):
                elevation[i, j] = (
                    surface2000[2 * i, 2 * j]
                    + surface2000[2 * i + 1, 2 * j]
                    + surface2000[2 * i, 2 * j + 1]
                    + surface2000[2 * i + 1, 2 * j + 1]
                ) / 4
    else:
        # only store and order the z data in the elevation matrix
        for elem in data:
            elevation[
                int(elem[0] - origin_long - 0.5), int(elem[1] - origin_lat - 0.5)
            ] = elem[2]

    return elevation.transpose()


def edgeDetection(input: np.ndarray, filter_size: int = 1) -> np.ndarray:
    """simple edge dedecton. Dedects the coastline and sets all other values to nan

    Parameters
    ----------
    input : np.ndarray
        The input array. The higt must be adjust, so that the water level is 0.
    filter size : size of the cubic filter mask.
    Returns
    -------
    output : np.ndarray
        filterd array
    """
    tmp = np.copy(input)
    shape = np.shape(input)
    if filter_size == 0:
        tmp[tmp <= 0] = np.nan
        return tmp
    for i in range(shape[0]):
        for j in range(shape[1]):
            if input[i, j] <= 0:
                xmi = i - filter_size
                xma = i + filter_size
                ymi = j - filter_size
                yma = j + filter_size
                if i == 0:
                    xmi = i
                if i == shape[1] - 1:
                    xma = i
                if j == 0:
                    ymi = j
                if j == shape[1] - 1:
                    yma = j
                if not (np.sum(input[xmi:xma, ymi:yma]) > 0):
                    tmp[i, j] = np.nan
    return tmp


def interpolateNan(input: np.ndarray, method: str = "linear"):
    """interpolate all nan values in an Array

    Parameters
    ----------
    input : np.ndarray
        The input array
    method : interpolation method. cubic or linear
    Returns
    -------
    output : np.ndarray
        filterd array
    """
    tmp = np.copy(input)
    x = np.arange(0, tmp.shape[1])
    y = np.arange(0, tmp.shape[0])
    tmp = np.ma.masked_invalid(tmp)
    xx, yy = np.meshgrid(x, y)
    x1 = xx[~tmp.mask]
    y1 = yy[~tmp.mask]
    newarr = tmp[~tmp.mask]

    return interpolate.griddata((x1, y1), newarr.ravel(), (xx, yy), method=method)


def combineLandWater(land: np.ndarray, water: np.ndarray) -> np.ndarray:
    """combines the an array with the underwater data with an array of the land data.

    Parameters
    ----------
    land : np.ndarray
        The array with the elevation data of the land
    water : np.ndarray
        The array with the elevation data of the under water surface
    Returns
    -------
    output : np.ndarray
        combined array with the water and land data
    """
    out = np.full((1000, 1000), np.nan, dtype=float)

    for i in range(1000):
        for j in range(1000):
            if not np.isnan(water[i, j]):
                out[i, j] = water[i, j]
    for i in range(1000):
        for j in range(1000):
            if not np.isnan(land[i, j]):
                out[i, j] = land[i, j]

    return out
