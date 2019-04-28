.PHONY: all

all: main.pdf

rmds = sections/methods.tex sections/analyses-main.tex

$(rmds): ../analyses/stats/methods.tex ../analyses/stats/analyses-main.tex
	make -C ../analyses/stats/

main.pdf: reference.bib $(rmds) sections/intro.tex sections/discussion.tex
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex
	pdflatex main.tex
