import numpy as np

import sympy as sym


def transition_matrix_memory_one_strategies(
    player, co_player, analytical=False
):
    if analytical == False:
        func = np.array
    elif analytical == True:
        func = sym.Matrix
    M = func(
        [
            [
                player[0] * co_player[0],
                player[0] * (1 - co_player[0]),
                (1 - player[0]) * co_player[0],
                (1 - player[0]) * (1 - co_player[0]),
            ],
            [
                player[1] * co_player[2],
                player[1] * (1 - co_player[2]),
                (1 - player[1]) * co_player[2],
                (1 - player[1]) * (1 - co_player[2]),
            ],
            [
                player[2] * co_player[1],
                player[2] * (1 - co_player[1]),
                (1 - player[2]) * co_player[1],
                (1 - player[2]) * (1 - co_player[1]),
            ],
            [
                player[3] * co_player[3],
                player[3] * (1 - co_player[3]),
                (1 - player[3]) * co_player[3],
                (1 - player[3]) * (1 - co_player[3]),
            ],
        ]
    )

    return M


def transition_matrix_memory_one_two(player, co_player, analytical=False):
    (
        p1,
        p2,
        p3,
        p4,
        p5,
        p6,
        p7,
        p8,
        p9,
        p10,
        p11,
        p12,
        p13,
        p14,
        p15,
        p16,
    ) = player
    (
        q1,
        q2,
        q3,
        q4,
        q5,
        q6,
        q7,
        q8,
        q9,
        q10,
        q11,
        q12,
        q13,
        q14,
        q15,
        q16,
    ) = co_player

    if analytical == True:
        M = sym.zeros(16, 16)
    else:
        M = np.zeros((16, 16))

    col, row = 0, 0

    for p, q in [[p1, q1], [p2, q3], [p3, q2], [p4, q4]]:
        for i, combo in enumerate(
            [(p * q), ((1 - q) * p), ((1 - p) * q), ((1 - p) * (1 - q))]
        ):

            M[row, col + i] = combo

        col += 4
        row += 1

    col = 0
    for p, q in [[p5, q9], [p6, q11], [p7, q10], [p8, q12]]:
        for i, combo in enumerate(
            [(p * q), ((1 - q) * p), ((1 - p) * q), ((1 - p) * (1 - q))]
        ):

            M[row, col + i] = combo

        col += 4
        row += 1

    col = 0
    for p, q in [[p9, q5], [p10, q7], [p11, q6], [p12, q8]]:
        for i, combo in enumerate(
            [(p * q), ((1 - q) * p), ((1 - p) * q), ((1 - p) * (1 - q))]
        ):

            M[row, col + i] = combo

        col += 4
        row += 1

    col = 0
    for p, q in [[p13, q13], [p14, q15], [p15, q14], [p16, q16]]:
        for i, combo in enumerate(
            [(p * q), ((1 - q) * p), ((1 - p) * q), ((1 - p) * (1 - q))]
        ):

            M[row, col + i] = combo

        col += 4
        row += 1

    return M


def transition_matrix_memory_one_strategies(
    player, co_player, analytical=False
):
    row_iterations = [range(16), range(16, 32), range(32, 48), range(48, 64)]

    column_iterations = np.linspace(0, 63, 64).reshape(16, 4)

    if analytical == False:
        M = np.zeros((64, 64))

    elif analytical == True:
        M = sym.zeros(64, 64)

    player_probabilities = np.linspace(0, 63, 64).reshape(16, 4)
    co_player_probabilities = np.linspace(0, 63, 64).reshape(16, 4)

    # adjusting co-player
    co_player_probabilities[[1, 2]] = co_player_probabilities[[2, 1]]
    co_player_probabilities[[4, 8]] = co_player_probabilities[[8, 4]]
    co_player_probabilities[[5, 10]] = co_player_probabilities[[10, 5]]
    co_player_probabilities[[6, 9]] = co_player_probabilities[[9, 6]]
    co_player_probabilities[[7, 11]] = co_player_probabilities[[11, 7]]
    co_player_probabilities[[13, 14]] = co_player_probabilities[[14, 13]]
    co_player_probabilities[:, [1, 2]] = co_player_probabilities[:, [2, 1]]

    for row in row_iterations:
        for i, irow in enumerate(row):
            pi = int(player_probabilities.flatten()[irow])
            qi = int(co_player_probabilities.flatten()[irow])

            p = player[pi]
            q = co_player[qi]

            combos = [p * q, p * (1 - q), (1 - p) * q, (1 - p) * (1 - q)]

            for j, column in enumerate(column_iterations[i, :]):
                M[irow, int(column)] = combos[j]
    return M
