from numpy.random import choice
from pandas import Series

expSituations = list(range(1, 4))

order = choice(expSituations, size=400, p=(.4, .4, .2))

sequence = Series(order, index=range(1, 401))

sequence.to_csv(path='/home/denis/Downloads/exp.csv')
