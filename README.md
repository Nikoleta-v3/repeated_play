# stationary

A Markov chain or Markov process is a probabilistic model that describes a
sequence of potential events, where the probability of each event occurring
depends solely on the state reached in the preceding event.

A Markov process is characterized by a transition matrix $M$, describing the
probabilities of particular transitions (changes of state of the system), and
the stationary distribution. The stationary distribution is a probability
distribution that remains unchanged in the Markov chain as time progresses. The
stationary distribution can be expressed as $v = M \times v$.

`stationary` is an open source Python package for calculating the stationary
distribution(s) of a Markov process.

## Quick Usage

To calculate the stationary distribution of a process, you first need to define
the transition matrix of the process as an `np.array`. Following this,
you can use the function `calculate_stationary_distribution`.

```python
>>> import numpy as np
>>> import stationary as stpy
>>> M = np.array([[0.9, 0.1], [0.5, 0.5]])

>>> stationary_dists = stpy.cal_stationary_distribution(M)
>>> stationary_dists
[array([0.83333333, 0.16666667])]
```

Notice that the function returns a `list`. That is because Markov processes can have
more then a single absorbing state. Take for example the following transition
matrix:

```python
>>> M = np.array(
...    [
...        [0, 1 / 2, 0, 1 / 2, 0],
...        [1 / 2, 0, 1 / 2, 0, 0],
...        [0, 1 / 2, 0, 0, 1 / 2],
...        [0, 0, 0, 1, 0],
...        [0, 0, 0, 0, 1],
...    ]
... )
```

Here the first three states are the transient ones and the last two ones are the
absorbing states. Using the `calculate_stationary_distribution` function now
returns two distributions:

```python
>>> stationary_dists = stpy.cal_stationary_distribution(M)
>>> stationary_dists
[array([0., 0., 0., 1., 0.]), array([0., 0., 0., 0., 1.])]
```

## Repeated Games

Markov process are vastly used in studying repeated games. In repeated games we
can assume that players use specific memory-$n$ strategies (strategies that
only consider the last $n$ outcomes). A repeated game between two such
strategies can be described as a Markov process.

`stationary` allows you to define the transitions matrices when players
use memory-1, 2 and 3 strategies.


## Tests

The package has an automated tests suite. To run the test suit locally
you need `pytests` and then you can run the command:

```shell
$ pytest tests
```