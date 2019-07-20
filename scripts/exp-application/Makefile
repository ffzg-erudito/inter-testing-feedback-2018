# this Makefile builds the model.py file, which contains the text-related
# questsions

targetDir = fwt_oTree/fwt/

$(targetDir)models.py: questions/pitanja-korovi-nepovezani-intruzori-py.txt\
    models_template.py
	python question-import.py
	mv $(targetDir)out.py $(targetDir)models.py
