import sympy as sym

import numpy as np

from numpy.linalg import inv


def stationary_distribution_eigenvalues(M):
    """A function that takes a numerical transition matrix as input and
    returns the stationary state.

    This function uses the eigenvalues of the transition matrix method.

    Parameters
    ----------
    M : np.array
        The transition matrix

    Returns
    -------
    list
        A list of stationary distributions
    """
    vectors = []

    eigenvalues, eigenvectors = np.linalg.eig(M.T)

    for index in np.where(np.isclose(eigenvalues, 1))[0]:
        eigenvectors_one = eigenvectors[:, index]
        stationary = eigenvectors_one / eigenvectors_one.sum()
        vectors.append(stationary.real)

    return vectors


def stationary_distribution_algebraic_system(M):
    """A function that takes a transition matrix with symbols as input and
    returns the stationary state analytically.

    Parameters
    ----------
    M : sym.Matrix
        The transition matrix

    Returns
    -------
    sym.Matrix
        The stationary vector
    """
    size = M.shape[1]
    pi = sym.symbols(f"p_1:{size + 1}")
    ss = sym.solve(
        [sum(pi) - 1]
        + [a - b for a, b in zip(M.transpose() * sym.Matrix(pi), pi)],
        pi,
    )

    v_vector = sym.Matrix(
        [
            [ss[p] for p in pi],
        ]
    )

    return v_vector


def stationary_distribution_discount_factor_numerical(M, opening_state, delta):
    """Stationary distribution of a finite repeated game with discount factor.

    Parameters
    ----------
    M : np.array
        The transition matrix
    opening_state : np.array
        The opening state vector
    delta : float
        Discount factor

    Returns
    -------
    np.array
        Stationary vector
    """
    eye_matrix = np.eye(4)
    inverse_matrix = inv(eye_matrix - delta * M)

    return ((1 - delta) * opening_state.T) @ inverse_matrix


def stationary_distribution_discount_factor_analytical(M, opening_state, delta):
    """Stationary distribution of a finite repeated game with discount factor.

    Parameters
    ----------
    M : sym.Matrix
        The transition matrix
    opening_state : sym.Matrix
        The opening state vector
    delta : float
        Discount factor

    Returns
    -------
    sym.Matrix
        Stationary vector
    """
    eye_matrix = sym.eye(4)
    inverse_matrix = (eye_matrix - delta * M).inv()

    return ((1 - delta) * opening_state.T) @ inverse_matrix
