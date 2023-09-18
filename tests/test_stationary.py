import numpy as np
import sympy as sym

from repeated_play.stationary import (
    stationary_distribution_algebraic_system,
    stationary_distribution_discount_factor_numerical,
    stationary_distribution_eigenvalues,
    stationary_distribution_discount_factor_analytical,
)
from repeated_play.transition_matrices import (
    transition_matrix_memory_one_strategies,
)


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


def test_stationary_distribution_with_algebraic_system():
    p1, p2 = sym.symbols("p_1, p_2")
    b, c = sym.symbols("c, b")

    M = transition_matrix_memory_one_strategies(
        [p1, p2, p1, p2], [0, 0, 0, 0], analytical=True
    )
    payoff_expected_1 = -c * p2
    payoff_expected_2 = b * p2

    ss = stationary_distribution_algebraic_system(M)

    assert sum(ss @ sym.Matrix([b - c, -c, b, 0])) - payoff_expected_1 == 0
    assert sum(ss @ sym.Matrix([b - c, b, -c, 0])) - payoff_expected_2 == 0


def test_stationary_with_discount_numerical():
    M = np.array([[0.9, 0.1], [0.5, 0.5]])

    # without discount
    stationary_dists = stationary_distribution_eigenvalues(M)

    opening_state = np.array([0.5, 0.5])
    stationary_dists_discount = (
        stationary_distribution_discount_factor_numerical(
            M, opening_state, delta=0.9999999
        )
    )
    assert np.allclose(stationary_dists[0], stationary_dists_discount)

    stationary_dists_discount = (
        stationary_distribution_discount_factor_numerical(
            M, opening_state, delta=0.99
        )
    )
    assert np.allclose(stationary_dists[0], stationary_dists_discount) == False


def test_stationary_distribution_discount_factor_analytical():
    p1, p2 = sym.symbols("p_1, p_2")
    b, c, delta = sym.symbols("b, c, delta")

    M = transition_matrix_memory_one_strategies(
        [p1, p2, p1, p2], [0, 0, 0, 0], analytical=True
    )

    opening_state = sym.Matrix([0, 0, 0, 1])

    ss = stationary_distribution_discount_factor_analytical(
        M, opening_state, delta
    )

    expected_payoff = -c * delta * p2

    assert sum(ss @ sym.Matrix([b - c, -c, b, 0])) - expected_payoff == 0
