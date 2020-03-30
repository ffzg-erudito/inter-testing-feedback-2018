.PHONY: all ../images/flowchart/flowchart.pdf

sections=../../paper/sections/

all: $(sections)methods.tex $(sections)analyses-main.tex

methods.Rmd: ../images/flowchart/flowchart.pdf

%.tex: %.Rmd
	Rscript -e 'rmarkdown::render("$<")'

$(sections)methods.tex: methods.tex
	python tex-strip.py $<
	mv tmp-$< $@

$(sections)analyses-main.tex: analyses-main.tex
	python tex-strip.py $<
	sed -i -Ee\
	    's@analyses-main_files/figure-latex/descFig-1.pdf@../analyses/images/descFig-1.pdf@'\
	    tmp-$<
	mv tmp-$< $@

../../paper/images/flowchart.pdf: ../images/flowchart/flowchart.pdf
	cp $< $@
