.PHONY: all ../images/flowchart/flowchart.pdf

sections=../../paper/sections/

all: $(sections)methods.tex $(sections)analyses-main.tex

methods.Rmd: ../images/flowchart/flowchart.pdf

methods.tex: methods.Rmd
	Rscript -e 'rmarkdown::render("$<")'

$(sections)methods.tex: methods.tex
	python tex-strip.py $<
	mv tmp-$< $@

$(sections)analyses-main.tex: analyses-main.tex
	python tex-strip.py $<
	mv tmp-$< $@

../../paper/images/flowchart.pdf: ../images/flowchart/flowchart.pdf
	cp $< $@
