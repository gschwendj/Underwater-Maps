#!/usr/bin/env python
"""stores the elevation data, color scale and markers for the divesite Au

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
__status__ = "Production"

from .au import Au
from .betlis import Betlis
from .broder import Broder
from .mols import Mols
from .murg_west import Murg_west
from .terlinden import Terlinden
from .tiefenwinkel import Tiefenwinkel
from .zick_zack import Zick_zack
from .zollerbucht import Zollerbucht

__all__ = [
    "Au",
    "Betlis",
    "Broder",
    "Mols",
    "Murg_west",
    "Terlinden",
    "Tiefenwinkel",
    "Zick_zack",
    "Zollerbucht",
]
