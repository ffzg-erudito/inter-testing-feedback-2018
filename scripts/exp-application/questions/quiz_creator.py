# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:01:21 2018

@authors: matpa, vdeni
"""
import os
import re
import csv

# set paths
os.chdir('C:\\Users\Matej\inter-testing-feedback-2018\scripts\exp-application\questions')

questionsPath = 'pitanja-korovi-nepovezani-intruzori-test2.txt'


# read files
with open(questionsPath, 'r', encoding='utf8') as infile:
    items = infile.read()

# clean questions and put them in a dict
items = re.split('(?=\d\.\d{1,2}\.)', items)

items = [item.strip() for item in items][1:]

optSubtitution = {'a.': 1, 'b.': 2,  'c.': 3, 'd.': 4}
questionImport = {}
for item in items:
    elements = re.split('\n +', item)
    elements = [element.strip() for element in elements]

    qnr, question = tuple(elements[0].split(' ', 1))

    options = elements[1:]
    options = [option.split(' ', 1) for option in options]
    options = dict([[str(optSubtitution.get(option[0])), option[1]]
                    for option in options])

    questionImport.update({qnr: {'question': question,
                                 'options': options}})

    
    
# solution = [3, 5, 4, 4, 2, 4, 4, 5, 2, 4, 3, 5, 4, 2, 5, 2, 3, 4, 2, 4, 5, 5, 2, 5, 2, 2, 4, 2, 5, 2] - za prvi, drugi i treći dio s po 10 pitanja
# intrusor = []
    
# za test2:
solution = [3, 5, 4, 2, 5, 2, 3, 4, 2, 4]
intrusor = [4, 2, 5, 3, 2, 3, 5, 2, 4, 3]

# za 3. dio s 20 pitanja ('pitanja-korovi-nepovezani-intruzori-3.0.txt'):
# solution = [5, 5, 2, 5, 2, 2, 4, 2, 5, 2, 5, 2, 3, 4, 3, 5, 5, 2, 4, 5]
# intrusor = [2, 3, 3, 2, 5, 4, 5, 4, 2, 3, 3, 3, 2, 3, 4, 4, 2, 3, 2 ,4]

with open('quiz.csv', 'w', newline = '', encoding='utf-8') as questions_file:
    questions_writer = csv.writer(questions_file, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
    header = ['id', 'question', 'choice1', 'choice2', 'choice3', 'choice4', 'solution', 'intrusor']
    questions_writer.writerow(header)
    
    data = []
    q_num = 0
    for item in items:
        row = re.split('\n', item)
        row[0] = row[0].split(' ', 1)       
        row.insert(1, row[0][1])
        row[0] = q_num + 1
        index = 2
        for element in row[2:]:
            row[index] = element[11:]
            index += 1
        row.append(row[solution[q_num]])
        row.append(row[intrusor[q_num]])
        data.append(row)
        q_num += 1
    questions_writer.writerows(data)