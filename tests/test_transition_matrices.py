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
    DelayedAlternator = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
    AllC = np.array([1 for _ in range(16)])

    M = transition_matrix_memory_two_strategies(DelayedAlternator, AllC)
    
    assert isinstance(M, np.ndarray)
    assert M.shape == (16, 16)

    # assert that each row sums to 1
    assert np.allclose(M.sum(axis = 1), np.array([1 for _ in range(16)]))

    expected = np.array([
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
       [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.]])

    assert np.allclose(M, expected)


def test_memory_three():
    player_one = np.random.random(64)
    player_two = np.random.random(64)

    M = transition_matrix_memory_three_strategies(player_one, player_two)
    
    assert isinstance(M, np.ndarray)
    assert M.shape == (64, 64)

    # assert that each row sums to 1
    assert np.allclose(M.sum(axis = 1), np.array([1 for _ in range(64)]))