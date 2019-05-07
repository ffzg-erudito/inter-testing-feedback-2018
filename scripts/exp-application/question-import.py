import re
import os

# set paths
modelsPath = 'models_template.py'

questionsPath = os.path.join('questions',
                             'pitanja-korovi-nepovezani-intruzori-py.txt')

# read files
with open(modelsPath, 'r') as infile:
    modelScript = infile.readlines()

with open(questionsPath, 'r') as infile:
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

outFile = open(os.path.join('fwt_oTree', 'fwt', 'out.py'), 'w')

iModelScript = iter(modelScript)
for line in iModelScript:
    if re.search('\s+test\d_q\d{1,2}', line):
        qKey = re.findall('test(\d)_q(\d{1,2})', line)
        qKey = qKey[0][0] + '.' + qKey[0][1] + '.'

        newLine = line +\
        f"label = '{questionImport.get(qKey).get('question')}'," + '\n'
        newLine = re.sub('\n', '', newLine, 1)
        line = newLine

        outFile.write(line)

        # skip `choices= [` line
        outFile.write(next(iModelScript))

        # modify choice lines
        for qNr in range(0,4):
            line = next(iModelScript)

            optNr = re.search('\d{1}', line).group(0)

            line = re.sub("(?<=')(?=')",
                        questionImport.get(qKey).get('options').get(str(optNr)),
                        line)

            outFile.write(line)

    else:
        outFile.write(line)

outFile.close()
