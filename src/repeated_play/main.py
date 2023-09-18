import numpy as np
import sympy as sym

from .stationary import (
    stationary_distribution_algebraic_system,
    stationary_distribution_eigenvalues,
)
from .transition_matrices import (
    transition_matrix_memory_one_strategies,
    transition_matrix_memory_three_strategies,
    transition_matrix_memory_two_strategies,
)


def stationary_distribution(M, analytical=False):
    if analytical == False:
        assert isinstance(M, np.ndarray), "M needs to be an numpy array."
        return stationary_distribution_eigenvalues(M)

    if analytical == True:
        assert isinstance(M, sym.Matrix), "M needs to be an numpy array."
        return stationary_distribution_algebraic_system(M)


def transition_matrix_repeated_game(
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
