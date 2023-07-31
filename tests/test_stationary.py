from repeated_play.stationary import stationary_distribution_eigenvalues

import numpy as np


def test_stationary_distribution_eigenvalues():
    M = np.array([[0.9, 0.1], [0.5, 0.5]])

    stationary_dists = stationary_distribution_eigenvalues(M)

    expected = [0.83333333, 0.1666667]
    assert np.allclose(stationary_dists[0], expected)


def test_stationary_distribution_eigenvalues_two():
    M = np.array([[0.9, 0.075, 0.025], [0.15, 0.8, 0.05], [0.25, 0.25, 0.5]])

    stationary_dists = stationary_distribution_eigenvalues(M)

    expected = [0.625, 0.3125, 0.0625]
    assert np.allclose(stationary_dists[0], expected)


def test_stationary_distribution_eigenvalues_multiple_absorbing_states():
    M = np.array(
        [
            [0, 1 / 2, 0, 1 / 2, 0],
            [1 / 2, 0, 1 / 2, 0, 0],
            [0, 1 / 2, 0, 0, 1 / 2],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
        ]
    )

    stationary_dists = stationary_distribution_eigenvalues(M)
    expected = [[0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    for ss, exp in zip(stationary_dists, expected):
        assert np.allclose(ss, exp)
