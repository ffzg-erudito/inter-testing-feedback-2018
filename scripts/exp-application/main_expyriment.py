# -*- coding: utf-8 -*-

# This script contains the main body of code for an experiment that investigates the forward testing effect

# A rough outline of the presentation flow is as follows: 
# 1. Setup (choosing an experimental condition)
# 2. Instructions (vary depending on chosen experimental condition)
# 3. Looping through 3 phases of learning and a secondary activity (varies depending on chosen experimental condition)
# 4. "Thank you" message
#

import expyriment

n_blocks = 3


# define target text path and load text
with open('text.txt', 'r') as myfile:
    text = myfile.read().replace('\n', '')
    
    
    
# define instructions path and load instructions
with open('instructions.txt', 'r') as myfile:
    instructions = myfile.read().replace('\n', '')


# create experiment
experiment = expyriment.design.Experiment(name='Forward testing effect')
expyriment.control.initialize(experiment)



# create blocks, i.e. 3 sections containing both a text presentation part, and a secondary activity part
for block in range(n_blocks):
    this_block = expyriment.design.Block(name = str(block + 1))
    
    
    # Select a part of the target text
    this_stim = text
    temp_stim = expyriment.stimuli.TextScreen(text)
    
    
    
    #
    
    experiment.add_block(this_block)
