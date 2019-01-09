# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 15:01:21 2018

@authors: matpa, vdeni
"""
import os
import re
import csv
import random

# set paths
os.chdir('C:\\Users\matpa\inter-testing-feedback-2018\scripts\exp-application\questions')

questionsPath = 'pitanja-opca-kultura.txt'


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

    
# correct answers    
solution = [3, 5, 2, 2, 4, 2, 3, 5, 2, 4, 3, 5, 4, 3, 2, 3, 4, 2, 5, 4, 3, 5, 4, 3, 4, 2, 3, 4, 5, 2, 2, 4, 2, 5, 3, 2, 4, 2, 5, 3, 4]

# for quiz1, create list of indices into items
indices_quiz1 = random.sample(range(0,len(items)), 10)

# create element writer
with open('gk_quiz1.csv', 'w', newline = '', encoding='utf-8') as questions_file:
    questions_writer = csv.writer(questions_file, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
    
    # create and write header
    header = ['id', 'question', 'choice1', 'choice2', 'choice3', 'choice4', 'solution']
    questions_writer.writerow(header)
    
    # create empty list 'data' which will contain as elements rows to be written into file
    data = []
    q_num = 0
    
    # each row is a ...
    for index in indices_quiz1:
        
        # list 'row', containing the question, answers, and the solution at the end
        row = re.split('\n', items[index])
        
        # at this moment, the first element, i.e. the question, contains both 
        # its number and the question itself, so let's split this element
        row[0] = row[0].split(' ', 1)   
        
        # at index number 1 in 'row' place the question itself
        row.insert(1, row[0][1])
        
        # at index number 0 in 'row' place question number
        row[0] = q_num + 1
        
        # delete whitespaces before the possible answers
        index_to_answers = 2
        for element in row[2:]:
            row[index_to_answers] = element[11:]
            index_to_answers += 1
        
        # append as last element in row the solution to the question
        row.append(row[solution[index]])
        
        # append the created row to the list of questions
        data.append(row)
        
        # increment question number
        q_num += 1
    
    # write the generated list of questions 'data' into the .csv file
    questions_writer.writerows(data)

# delete the questions selected for quiz1 from the item list, as well as their solutions
for index in sorted(indices_quiz1, reverse = True):
    del solution[index]
    del items[index]



indices_quiz2 = random.sample(range(0,len(items)), 10)
print(indices_quiz2)


# create element writer
with open('gk_quiz2.csv', 'w', newline = '', encoding='utf-8') as questions_file:
    questions_writer = csv.writer(questions_file, delimiter = ',', quoting=csv.QUOTE_MINIMAL)
    
    # create and write header
    header = ['id', 'question', 'choice1', 'choice2', 'choice3', 'choice4', 'solution']
    questions_writer.writerow(header)
    
    # create empty list 'data' which will contain as elements rows to be written into file
    data = []
    q_num = 0
    
    # each row is a ...
    for index in indices_quiz2:
        
        # list 'row', containing the question, answers, and the solution at the end
        row = re.split('\n', items[index])
        
        # at this moment, the first element, i.e. the question, contains both 
        # its number and the question itself, so let's split this element
        row[0] = row[0].split(' ', 1)   
        
        # at index number 1 in 'row' place the question itself
        row.insert(1, row[0][1])
        
        # at index number 0 in 'row' place question number
        row[0] = q_num + 1
        
        # delete whitespaces before the possible answers
        index_to_answers = 2
        for element in row[2:]:
            row[index_to_answers] = element[11:]
            index_to_answers += 1
        
        # append as last element in row the solution to the question
        row.append(row[solution[index]])
        
        # append the created row to the list of questions
        data.append(row)
        
        # increment question number
        q_num += 1
    
    # write the generated list of questions 'data' into the .csv file
    questions_writer.writerows(data)