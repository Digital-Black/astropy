# Licensed under a 3-clause BSD style license - see LICENSE.rst

# The following few lines skip this module when running tests if matplotlib is
# not available (and will have no impact otherwise)
from ...tests.helper import pytest
pytest.importorskip("matplotlib.pyplot")
del pytest

from .core import *
from .coordinate_helpers import CoordinateHelper
from .coordinates_map import CoordinatesMap
from .patches import *

from ... import config as _config


class Conf(_config.ConfigNamespace):
    """
    Configuration parameters for `astropy.table`.
    """

    coordinate_range_samples = _config.ConfigItem(50,
        'The number of samples along each image axis when determining '
        'the range of coordinates in a plot.')

    frame_boundary_samples = _config.ConfigItem(1000,
        'How many points to sample along the axes when determining '
        'tick locations.')

    grid_samples = _config.ConfigItem(1000,
        'How many points to sample along grid lines.')

conf = Conf()
