# repeated play

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
>>> import nympy as np
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
>>> M = repeated_play.retr_transition_matrix_repeated_game(Stick,
...                                                        Alternator,
...                                                        memory="one")

>>> ss = repeated_play.calc_stationary_distribution(M)
>>> ss
[array([0.5, 0.5, 0. , 0. ]), array([0. , 0. , 0.5, 0.5])]
```

## Memory Two

**Note**. In the case of memory-two strategies we assume that a strategy is
written as 

$$p = (p_{CC|CC}, p_{CC|CD}, p_{CC|DC}, p_{CC|DD}, p_{CD|CC},
p_{CD|CD},p_{CD|DC},p_{CD|DD}, p_{DC|CC}, p_{DC|CD}, p_{DC|DC}, p_{DC|DD},
p_{DD|CC}, p_{DD|CD}, p_{DD|DC}, p_{DD|DD})$$

where $CC|DC$ denotes that in the
second to last round both players cooperated and in the last round player one
defected. Thus $F_1 F_2 | E_1 E_2$ where $F_i$ is the action of player $i$ in
the second to last round and $E_{i}$ is the action of player $i$ in the last
round.

One you have defined the strategies in the memory-two space then you can use the
`transition_matrix_repeated_game` to retrieve the transition matrix as before,
but now `memory="two"`, and the `stationary_distribution` function to get the
long-term outcome.

```python
>>> DelayedAlternator = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
>>> AllD = np.array([0 for _ in range(16)])

>>> M = repeated_play.retr_transition_matrix_repeated_game(DelayedAlternator,
...                                                        AllD,
...                                                        memory="two")

>>> ss = repeated_play.calc_stationary_distribution(M)
>>> ss
```

## Memory Three

```python
>>> Random = np.random.random(64)
>>> AllD = np.array([0 for _ in range(64)])

>>> M = repeated_play.retr_transition_matrix_repeated_game(Random,
...                                                        AllD,
...                                                        memory='three')

>>> M.shape
(64, 64)
```

## Long Term Payoffs

## Discounted Game

_coming soon_

## Tests

The package has an automated tests suite. To run the test suit locally
you need `pytests` and then you can run the command:

```shell
$ pytest tests
```