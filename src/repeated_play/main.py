import numpy as np

import sympy as sym

from .stationary import (
    stationary_distribution_eigenvalues,
    stationary_distribution_algebraic_system,
)

from .transition_matrices import (
    transition_matrix_memory_one_strategies,
    transition_matrix_memory_two_strategies,
    transition_matrix_memory_three_strategies,
)


def calc_stationary_distribution(M, analytical=False):
    if analytical == False:
        assert isinstance(M, np.ndarray), "M needs to be an numpy array."
        return stationary_distribution_eigenvalues(M)

    if analytical == True:
        assert isinstance(M, sym.Matrix), "M needs to be an numpy array."
        return stationary_distribution_algebraic_system(M)


def retr_transition_matrix_repeated_game(
    player, co_player, memory, analytical=False
):
    if memory == "one":
        return transition_matrix_memory_one_strategies(
            player, co_player, analytical
        )
    if memory == "two":
        return transition_matrix_memory_two_strategies(
            player, co_player, analytical
        )
    if memory == "three":
        return transition_matrix_memory_three_strategies(
            player, co_player, analytical
        )
