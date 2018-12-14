# this Makefile builds the model.py file, which contains the text-related
# questsions

targetDir = /home/denis/Documents/Poso/faks/istraživanja/inter-testing-feedback-2018/scripts/exp-application/fwt_oTree/fwt/

$(targetDir)models.py: questions/pitanja-korovi-nepovezani-intruzori-py.txt models_template.py models_template.py
	python question-import.py
	mv $(targetDir)out.py $(targetDir)models.py
