import numpy as np

import sympy as sym

from .methods import (
    stationary_distribution_eigenvalues,
    stationary_distribution_algebraic_system,
)


def cal_stationary_distribution(M, analytical=False):
    if analytical == False:
        assert isinstance(M, np.ndarray), "M needs to be an numpy array."
        return stationary_distribution_eigenvalues(M)

    if analytical == True:
        assert isinstance(M, sym.Matrix), "M needs to be an numpy array."
        return stationary_distribution_algebraic_system(M)
    return
