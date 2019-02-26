from darkbox import energy

import numpy as np
from numpy.testing import assert_equal


def test_abs_area():
    x = -3
    assert_equal(energy.abs_area(x), 3)
