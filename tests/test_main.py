import repeated_play

import numpy as np

import sympy as sym


def test_calc_stationary_distribution_numerical():
    M = np.array([[0.9, 0.1], [0.5, 0.5]])
    stationary_dists = repeated_play.calc_stationary_distribution(
        M, analytical=False
    )

    expected = [0.83333333, 0.1666667]
    assert np.allclose(stationary_dists[0], expected)


def test_retr_transition_matrix_memory_one():
    memory = "one"
    TFT = np.array([1, 0, 1, 0])
    AllC = np.array([1, 1, 1, 1])

    M = repeated_play.retr_transition_matrix_repeated_game(TFT, AllC, memory)

    assert isinstance(M, np.ndarray)
    assert M.shape == (4, 4)


def test_retr_transition_matrix_memory_two():
    memory = "two"
    DelayedAlternator = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
    AllD = np.array([0 for _ in range(16)])

    M = repeated_play.retr_transition_matrix_repeated_game(DelayedAlternator, AllD, memory)

    assert isinstance(M, np.ndarray)
    assert M.shape == (16, 16)


def test_retr_transition_matrix_memory_three():
    memory = "three"
    Random = np.random.random(64)
    AllD = np.array([0 for _ in range(64)])

    M = repeated_play.retr_transition_matrix_repeated_game(Random, AllD, memory)

    assert isinstance(M, np.ndarray)
    assert M.shape == (64, 64)
