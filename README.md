# repeated play

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![ci](https://github.com/Nikoleta-v3/repeated-play/actions/workflows/ci.yml/badge.svg)](https://github.com/Nikoleta-v3/repeated-play/actions/workflows/ci.yml)

In the study of repeated games, we often assume that players use strategies from
the family of memory-$n$ strategies. These strategies consider only the
$n$ previous outcomes to make a decision in the next round.

The advantage of constraining to these strategies is that it enables analytical
studies and allows us to model the repeated game between two such strategies
using a Markov process, avoiding the need for direct simulation of the
interactions.

For simulating the play in repeated games, consider using the Python package
[Axelrod](https://axelrod.readthedocs.io/en/stable/).

`repeated-play` is an open-source Python package that estimates the long-term
outcome and payoffs between a pair of players using either memory-one,
memory-two, or memory-three strategies.

## Install

For installation notes see: [installation.md](installation.md).

## Quick Usage

Assume a repeated game of the Prisoner's Dilemma where players can choose to
cooperate (C) or defect (D) in each round. A memory-one strategy is a strategy
that uses the outcome of the previous turn to decide on an action. Such a
strategy can be written as $p = (p_{CC}, p_{CD}, p_{DC}, p_{DD})$. Each entry
$p_h$ corresponds to the player's cooperation probability in the next round,
depending on the outcome of the previous round.

Tit For Tat, a strategy that copies the previous action of the co-player,
is a memory-one strategy and can be written as such $\text{TFT} = (1, 0, 1, 0)$.
AllD is another memory-one strategy which always defects, $\text{AllD} = (0, 0, 0, 0)$.

The play between the two strategies can be modelled a Markov process with the
transition matrix $M(\text{TFT}, \text{AllD})$. To retrieve the transition
matrix for this pair using `repeated-play` run the following lines of code:

```python
>>> import numpy as np
>>> import repeated_play

>>> TFT = np.array([1, 0, 1, 0])
>>> AllD = np.array([0, 0, 0, 0])

>>> M =  repeated_play.transition_matrix_repeated_game(TFT, AllD, memory="one")
>>> M
array([[0, 1, 0, 0],
       [0, 0, 0, 1],
       [0, 1, 0, 0],
       [0, 0, 0, 1]])
```

In the `transition_matrix_repeated_game` function we need to specify the memory
that our players are using. In the above example `memory="one"`. Memory can take
two more values in the current version of the package, namely `memory="two"` and
`memory="three"`.

A Markov process is characterized by the transition matrix $M$, and the
stationary distribution. The stationary distribution is a probability
distribution that remains unchanged in the Markov chain as time progresses ($v =
M \times v$). The stationary distribution represents the long-term outcome of
the match.

In the case of memory-one strategies $v = (v_{CC}, v_{CD}, v_{DC}, v_{DD})$
where the entry $v_{h}$ is the probability that the long term outcome is $h$.

```python
>>> ss = repeated_play.calc_stationary_distribution(M)
>>> ss
[array([0., 0., 0., 1.])]
```

A match between TFT and AllD results to both strategies defecting. results to a
long term outcome of both strategies defecting.

Notice that the function returns a `list`. That is because Markov processes can
have more then a single absorbing state.

## Multiple Absorbing States

It can happen that a match between two strategies can have more than one
possible solutions. Consider the case of $\text{Alternator} = (0, 0, 1, 1)$, a strategy that alternates
between it's actions and a strategy that
always cooperates if it did in the previous turn and always defects if it
defected, $\text{Stick} = (1, 1, 0, 0)$. A match
between these two strategies results in two solutions:

```python
>>> Alternator = np.array([0, 0, 1, 1])
>>> Stick = np.array([1, 1, 0, 0])
>>> M = repeated_play.transition_matrix_repeated_game(Stick,
...                                                   Alternator,
...                                                   memory="one")

>>> ss = repeated_play.stationary_distribution(M)
>>> ss
[array([0.5, 0.5, 0. , 0. ]), array([0. , 0. , 0.5, 0.5])]
```

## Memory Two

Memory-two strategies have 16 entries. We assume that a memory-two strategy is
written as,

$$\begin{aligned}p = (& p_{CC|CC}, p_{CC|CD}, p_{CC|DC}, p_{CC|DD}, \\
                      & p_{CD|CC}, p_{CD|CD}, p_{CD|DC},p_{CD|DD}, \\
                      & p_{DC|CC}, p_{DC|CD}, p_{DC|DC}, p_{DC|DD}, \\
                      & p_{DD|CC}, p_{DD|CD}, p_{DD|DC}, p_{DD|DD}) \end{aligned}$$

where $CC|DC$ denotes that in the second-to-last round, both players cooperated,
and in the last round player one, defected. More generally,
$p_{F_1 F_2 | E_1 E_2}, F_{i}, E_{i} \in \{C, D\}$ if the probability after
$F_1 F_2 | E_1 E_2$
where $F_i$ is the action of player $i$ in the second-to-last round and $E_{i}$
is the action of player $i$ in the last round.

One you have defined your memory-two strategies, you can use the
`transition_matrix_repeated_game` function to retrieve the transition matrix as
before, but now by setting `memory="two"`, and the `stationary_distribution`
function to obtain the long-term outcome.

```python
>>> import numpy as np
>>> import repeated_play

>>> DelayedAlternator = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
>>> AllD = np.array([0 for _ in range(16)])

>>> M = repeated_play.transition_matrix_repeated_game(DelayedAlternator,
...                                                   AllD,
...                                                   memory="two")

>>> ss = repeated_play.stationary_distribution(M)
>>> ss
[array([0.  , 0.  , 0.  , 0.  , 0.  , 0.25, 0.  , 0.25, 0.  , 0.  , 0.  ,
        0.  , 0.  , 0.25, 0.  , 0.25])]
```

## Memory Three

Memory-three strategies have 64 entries. We assume that a memory-three
strategy is written as,

$$\begin{aligned}p = (& p_{CC|CC|CC}, p_{CC|CC|CD}, p_{CC|CC|DC}, p_{CC|CC|DD}, \\
                      & p_{CC|CD|CC}, p_{CC|CD|CD}, p_{CC|CD|DC}, p_{CC|CD|DD}, \\
                      & p_{CC|DC|CC}, p_{CC|DC|CD}, p_{CC|DC|DC}, p_{CC|DC|DD}, \\
                      & p_{CC|DD|CC}, p_{CC|DD|CD}, p_{CC|DD|DC}, p_{CC|DD|DD}, \\
                      & p_{CD|CC|CC}, p_{CD|CC|CD}, p_{CD|CC|DC}, p_{CD|CC|DD}, \\
                      & p_{CD|CD|CC}, p_{CD|CD|CD}, p_{CD|CD|DC}, p_{CD|CD|DD}, \\
                      & p_{CD|DC|CC}, p_{CD|DC|CD}, p_{CD|DC|DC}, p_{CD|DC|DD}, \\
                      & p_{CD|DD|CC}, p_{CD|DD|CD}, p_{CD|DD|DC}, p_{CD|DD|DD}, \\
                      & p_{DC|CC|CC}, p_{DC|CC|CD}, p_{DC|CC|DC}, p_{DC|CC|DD}, \\
                      & p_{DC|CD|CC}, p_{DC|CD|CD}, p_{DC|CD|DC}, p_{DC|CD|DD}, \\
                      & p_{DC|DC|CC}, p_{DC|DC|CD}, p_{DC|DC|DC}, p_{DC|DC|DD}, \\
                      & p_{DC|DD|CC}, p_{DC|DD|CD}, p_{DC|DD|DC}, p_{DC|DD|DD}, \\
                      & p_{DD|CC|CC}, p_{DD|CC|CD}, p_{DD|CC|DC}, p_{DD|CC|DD}, \\
                      & p_{DD|CD|CC}, p_{DD|CD|CD}, p_{DD|CD|DC}, p_{DD|CD|DD}, \\
                      & p_{DD|DC|CC}, p_{DD|DC|CD}, p_{DD|DC|DC}, p_{DD|DC|DD}, \\
                      & p_{DD|DD|CC}, p_{DD|DD|CD}, p_{DD|DD|DC}, p_{DD|DD|DD}) \end{aligned}$$

where $p_{G_1 G_2 | F_1 F_2 | E_1 E_2}, G_{i}, F_{i}, E_{i} \in \{C, D\}$ is the
probability of cooperating following the outcome $G_1 G_2| F_1 F_2 | E_1 E_2$.
$G_i$ is the action of player $i$ in the third-to-last round, $F_i$ is the
action of player $i$ in the second-to-last round and $E_{i}$ is the action of
player $i$ in the last round.

```python
>>> import numpy as np
>>> import repeated_play

>>> Random = np.random.random(64)
>>> AllD = np.array([0 for _ in range(64)])

>>> M = repeated_play.transition_matrix_repeated_game(Random,
...                                                   AllD,
...                                                   memory='three')

>>> M.shape
(64, 64)
```

## Long Term Payoffs

For a given pair we want to know the long-term payoff each player achieved. The
long-term payoff is estimated using the stationary distribution of the match and
the payoff matrix of each player. The payoff matrices depend on the repeated
game.

For example consider our running example of the Prisoner's Dilemma. The payoff
$S_{i}$ for players 1 and 2 are the following:

$$ S_{1} = (R, S, T, P) \quad \text{ and } \quad S_{2} = (R, T, S, P).$$

Assume that $R=3, S=0, T=5 and P=1$, the following code calculates the
long-term payoff of Tit For Tat against Alternator.

```python
>>> import numpy as np
>>> import repeated_play

>>> TFT = np.array([1, 0, 1, 0])
>>> Alternator = np.array([0, 0, 1, 1])

>>> M = repeated_play.transition_matrix_repeated_game(TFT, Alternator, memory='one')
>>> ss = repeated_play.stationary_distribution(M)
>>> ss @ np.array([3, 0, 5, 1])
array([2.5])
```

## Other repeated games

The examples we have discussed here have been tailored to the Prisoner's Dilemma
but `repeated-play` can be used for any two players repeated game.

## Analytical

### Defining Strategies

Sometimes we want the analytical expressions of the invariant distribution or
the payoffs. This is possible using `repeated-play` with
[SymPy](https://www.sympy.org/en/index.html), the Python library for symbolic
mathematics.

So far, we have defined strategies as `np.array`. Here we will use
`sympy.symbols` and the `sym.Matrix` to define strategies instead. In the case
of a memory-one strategies,

```python
>>> import sympy as sym
>>> p1, p2, p3, p4 = sym.symbols("p1:5")
>>> player_one = sym.Matrix([p1, p2, p3, p4])
>> player_one
Matrix([
[p1],
[p2],
[p3],
[p4]])

>>> q1, q2, q3, q4 = sym.symbols("q1:5")
>>> player_two = sym.Matrix([q1, q2, q3, q4])
```

### Long-term outcome and long-term payoff

Let's consider a special case of memory-one strategies called reactive strategies
for which $p_1 = p_3, p_2 = p_4, q_1 = q_3$ and $q_2 = q_4$:

```python
>>> player_one = sym.Matrix([p1, p2, p1, p2])
>>> player_two = sym.Matrix([q1, q2, q1, q2])

>>> M = repeated_play.transition_matrix_repeated_game(player_one,
...                                                   player_two,
...                                                   memory="one",
...                                                   analytical=True)
>>> M
Matrix([
[p1*q1, p1*(1 - q1), q1*(1 - p1), (1 - p1)*(1 - q1)],
[p2*q1, p2*(1 - q1), q1*(1 - p2), (1 - p2)*(1 - q1)],
[p1*q2, p1*(1 - q2), q2*(1 - p1), (1 - p1)*(1 - q2)],
[p2*q2, p2*(1 - q2), q2*(1 - p2), (1 - p2)*(1 - q2)]])

>>> ss = repeated_play.stationary_distribution(M, analytical=True)

>>> R, S, T, P = sym.symbols("R, S, T, P")
>>> payoff_player_one = ss.dot(sym.Matrix([R, S, T, P]))
```

To learn more about `SymPy` check the [online
documentation](https://docs.sympy.org/latest/index.html).

The analytical code, in theory, can work for higher memory values, but some
stationary distributions are not computed in a realistic amount of time.
Specifically, for the cases of memory-two and memory-three, calculating the
invariant distributions for a generic player-one against another generic player
are not calculable.

However, if you want transition matrices for you paper you can use the
`repeated-game` to obtain the matrices and then exported to LaTex:

```python
>>> pis, qis = sym.symbols("p1:17"), sym.symbols("q1:17")
>>> memory_two_player_one = sym.Matrix(pis)
>>> memory_two_player_two = sym.Matrix(qis)

>>> M =  repeated_play.transition_matrix_repeated_game(memory_two_player_one, 
...                                                    memory_two_player_two,
...                                                    memory="two",
...                                                    analytical=True)

>>> latex_code = sym.latex(M)
```


## Discounted Game

_coming soon_

## Tests

The package has an automated tests suite. To run the test suit locally
you need `pytests` and then you can run the command:

```shell
$ pytest tests
```

### Requirements

The requirements for `repeated-play` can be found in `requirements.txt`. All the
requirements are standard Python packages, `sympy`, `numpy`, and for testing we
use `pytest`.

### Contributions

All contributions are welcome! This may include communicating ideas for new
sections, letting us know about bugs, and code contributions.
