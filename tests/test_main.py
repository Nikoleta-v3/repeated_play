import repeated_play

import numpy as np

import sympy as sym


def test_calc_stationary_distribution_numerical():
    M = np.array([[0.9, 0.1], [0.5, 0.5]])
    stationary_dists = repeated_play.cal_stationary_distribution(M, analytical=False)

    expected = [0.83333333, 0.1666667]
    assert np.allclose(stationary_dists[0], expected)
