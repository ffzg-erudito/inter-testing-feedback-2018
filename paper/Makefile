.PHONY: all

all: main.pdf

rmds = sections/methods.tex sections/analyses-main.tex

main.pdf: reference.bib $(rmds) sections/intro.tex
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex
	pdflatex main.tex

$(rmds): ../analyses/stats/methods.tex ../analyses/stats/analyses-main.tex
	make -C ../analyses/stats/
