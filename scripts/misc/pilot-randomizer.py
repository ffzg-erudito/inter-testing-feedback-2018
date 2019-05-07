from random import choice
from collections import Counter
from pandas import Series

expSituations = list(range(1, 6))

order = list()
for i in range(0, 15):
    order.append(choice(expSituations))

cnt = Counter()

for situation in order:
    cnt[situation] += 1

while not (all(x == list(cnt.values())[0] for x in list(cnt.values())) and
           len(cnt) == 5):
    order = list()
    for i in range(0, 15):
        order.append(choice(expSituations))

    cnt = Counter()
    for situation in order:
        cnt[situation] += 1

sequence = Series(order, index=range(1, 16))

sequence.to_csv(path='/home/denis/Downloads/exp.csv')
