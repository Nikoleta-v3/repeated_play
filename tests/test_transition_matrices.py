import numpy as np

from repeated_play.transition_matrices import (
    transition_matrix_memory_one_strategies,
    transition_matrix_memory_two_strategies,
    transition_matrix_memory_three_strategies,
)


def test_memory_one_example_one():
    TFT = np.array([1, 0, 1, 0])
    AllD = np.array([0, 0, 0, 0])

    M = transition_matrix_memory_one_strategies(TFT, AllD)
    expected = np.array(
        [[0, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 0, 1]]
    )

    assert isinstance(M, np.ndarray)
    assert M.shape == (4, 4)
    assert np.allclose(M, expected)


def test_memory_two():
    "Here we will test properties"
    pass
