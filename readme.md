# `game of life`
A computer science classic [Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## How
Game of life is really just counting neighbors. We can speed that up that by leverging the optimized `scipy.convolve` function. The kernel would be:
```
1 1 1
1 0 1
1 1 1
```
Convolution of state `I` (suppose living = 1, dead = 0) with kernel is the count of living neighbors:
```python
neighbors = convolve(self.I, self.kernel, mode='same')
```
We map living cells to `8` and dead cells to `-9`:
```python
I = 8 * I + (-9) * (1 - I)
```

Now `I + neighors` alone can represent the state of a cell and the number of its living neighbors. The range of cell states is from -17 to 16. For example, `-6` represents a dead cell with 3 living neighbors, which will live.

Combining the above logic, the state update is a two-liner:
```python
t = convolve(self.I, self.kernel, mode='same') + 17 * self.I - 9 # compute state variables
self.I = np.where((t == -6)|(t == 10)|(t == 11), 1, 0).reshape(self.I.shape)  # new state I
```