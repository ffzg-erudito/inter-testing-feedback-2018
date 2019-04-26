.PHONY: all

all: main.pdf

main.pdf: reference.bib sections/methods.tex sections/analyses-main.tex\
	sections/intro.tex
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex
	pdflatex main.tex

sections/methods.tex: ../analyses/stats/methods.tex
	make -C ../analyses/stats/

sections/analyses-main.tex: ../analyses/stats/analyses-main.tex
	make -C ../analyses/stats/
