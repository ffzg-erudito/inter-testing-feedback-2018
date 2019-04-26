import re
from sys import argv

target = argv[1]

with open(target, 'r') as infile:
    content = infile.readlines()

content[0] = re.sub('\[.*\]', '[../main.tex]', content[0])
content[0] = re.sub('article', 'subfiles', content[0])

delTargets = []

for i, line in enumerate(content):
    if i == 0:
        continue
    if not re.search('\\\\begin\{document\}', line):
        delTargets.append(i)
    else:
        break

content = [content[i] for i in range(0, len(content))
           if i not in delTargets]

if target == 'methods.tex':
    for i, line in enumerate(content):
        content[i] = re.sub('(\.\./)(images/)(flowchart/)(procedure.pdf)',
                            '\\2\\4', line)

with open('tmp-' + target, 'w') as outfile:
    outfile.writelines(content)
