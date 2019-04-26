.PHONY: all

sections=../../paper/sections/

all: $(sections)methods.tex $(sections)analyses-main.tex

$(sections)methods.tex: methods.tex
	python tex-strip.py $<
	mv tmp-$< $@

$(sections)analyses-main.tex: analyses-main.tex
	python tex-strip.py $<
	mv tmp-$< $@

../../paper/images/flowchart.pdf: ../images/flowchart/flowchart.pdf
	cp $< $@
