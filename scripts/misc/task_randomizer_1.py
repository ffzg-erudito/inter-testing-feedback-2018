from random import shuffle
import pandas as pd

tasks = ['SART', 'anti-saccade', 'reading span']

taskOrder = {'task1': [], 'task2': [], 'task3': []}

for i in range(0, 300):
    tasksTmp = tasks[:]
    shuffle(tasksTmp)

    for j, key in enumerate(list(taskOrder.keys())):
        taskOrder[key].append(tasksTmp[j])

df = pd.DataFrame(taskOrder)

box = list(range(1, 7)) * 50

box = pd.Series(box)
box.name = 'box'

df = pd.concat([df, pd.Series(box)], axis=1)

df.to_csv('~/Downloads/tasks-rand.csv', index=False)
