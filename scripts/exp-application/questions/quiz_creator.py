# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:01:21 2018

@authors: matpa, vdeni
"""
import os
import re
import csv

# set paths
questionsPath = "C:\\Users\\matpa\\inter-testing-feedback-2018\\scripts\\exp-application\\questions\\pitanja-korovi-nepovezani-intruzori-py.txt"

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


    
with open('quiz.csv', 'w') as questions_file:
    questions_writer = csv.writer(questions_file, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    
    for item in items:
        row = re.split('\n', item)
        row_0 = row[0].split('. ')
        row[0] = row_0[0]
        row.insert(1, row_0[1])
        for element in row:
            element = element.split('. ').Last()


outFile.close()
