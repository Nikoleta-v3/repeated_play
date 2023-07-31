# repeated play

In the study of repeated games, we often assume that players use strategies from
the family of memory-$n$ strategies. These strategies consider only the outcomes
in the previous $n$ outcomes to make a decision in the next round.

The advantage of constraining to these strategies is that it enables analytical
studies and allows us to model the repeated game between two such strategies
using a Markov process, avoiding the need for direct simulation of the
interactions.

For simulating the play in repeated games, consider using the Python package
[Axelrod](https://axelrod.readthedocs.io/en/stable/).

`repeated-play` is an open-source Python package that calculates the long-term
payoff when players use either memory-one, memory-two, or memory-three
strategies.

### Quick Usage

Assume a repeated game of the Prisoner's Dilemma where players can choose to
cooperate (C) or defect (D) in each round. A memory-one strategy is a strategy
that use the outcomes of the previous turn to decide on an action. Such a
strategy can be written as $p = (p_{CC}, p_{CD}, p_{DC}, p_{DD})$. Each entry
$p_h$ corresponds to the player's cooperation probability in the next round,
depending on the outcome of the previous round.

Tit For Tat, a strategy that copies the previous action of the co-player,
is a memory-one strategy and can be written as such $\text{TFT} = (1, 0, 1, 0)$.
AllD is another memory-one strategy which always defects, $\text{AllD} = (0, 0, 0, 0)$.

The play between the two strategies can be modelled a Markov process with
the transition matrix $M(\text{TFT}, \text{AllD})$. To retrieve the transition
matrix for this game in `repeated-play` we use the following lines of code:

```python
>>> import nympy as np
>>> import repeated_play

>>> TFT = np.array([1, 0, 1, 0])
>>> AllD = np.array([0, 0, 0, 0])

>>> M =  repeated_play.retr_transition_matrix_repeated_game(TFT, AllD, memory="one")
>>> M
array([[0, 1, 0, 0],
       [0, 0, 0, 1],
       [0, 1, 0, 0],
       [0, 0, 0, 1]])
```

In the `retr_transition_matrix_repeated_game` function we need to specify
the memory that our players are using. In the above example `memory="one"`.
Memory can take two more values in the current version of the package,
name `memory="two"` and `memory="three"`.


A Markov process is characterized by a transition matrix $M$, and the stationary
distribution. The stationary distribution is a probability distribution that
remains unchanged in the Markov chain as time progresses. The stationary
distribution can be expressed as $v = M \times v$.

```python
>>> ss = repeated_play.calc_stationary_distribution(M)
>>> ss
[array([0., 0., 0., 1.])]
```

We can see from the stationary distribution that a match between TFT and AllD
results to a long term outcome of both strategies defecting.

Notice that the function returns a `list`. That is because Markov processes can
have more then a single absorbing state.

## Memory Two

## Memory Three

## Long Term Payoffs

## Discounted Game

## Tests

The package has an automated tests suite. To run the test suit locally
you need `pytests` and then you can run the command:

```shell
$ pytest tests
```