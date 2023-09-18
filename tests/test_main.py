import numpy as np
import sympy as sym

import repeated_play


def test_stationary_distribution_numerical():
    M = np.array([[0.9, 0.1], [0.5, 0.5]])
    stationary_dists = repeated_play.stationary_distribution(
        M, analytical=False
    )

    expected = [0.83333333, 0.1666667]
    assert np.allclose(stationary_dists[0], expected)


def test_transition_matrix_memory_one():
    memory = "one"
    TFT = np.array([1, 0, 1, 0])
    AllC = np.array([1, 1, 1, 1])

    M = repeated_play.transition_matrix_repeated_game(TFT, AllC, memory)

    assert isinstance(M, np.ndarray)
    assert M.shape == (4, 4)


def test_transition_matrix_memory_two():
    memory = "two"
    DelayedAlternator = np.array(
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    )
    AllD = np.array([0 for _ in range(16)])

    M = repeated_play.transition_matrix_repeated_game(
        DelayedAlternator, AllD, memory
    )

    assert isinstance(M, np.ndarray)
    assert M.shape == (16, 16)


def test_transition_matrix_memory_three():
    memory = "three"
    Random = np.random.random(64)
    AllD = np.array([0 for _ in range(64)])

    M = repeated_play.transition_matrix_repeated_game(Random, AllD, memory)

    assert isinstance(M, np.ndarray)
    assert M.shape == (64, 64)


def test_stationary_distribution_analytical():
    p1, p2 = sym.symbols("p_1, p_2")

    b, c = sym.symbols("b, c")

    M = repeated_play.transition_matrices.transition_matrix_memory_one_strategies(
        [p1, p2, p1, p2], [0, 0, 0, 0], analytical=True
    )

    ss = repeated_play.stationary_distribution(M, analytical=True)
    expected_payoff = -c * p2

    assert expected_payoff - sum(ss @ sym.Matrix([b - c, -c, b, 0])) == 0
