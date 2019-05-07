.PHONY: all bib

rmds = sections/methods.tex sections/analyses-main.tex

all: bib main.pdf

bib: reference.bib
	sed -Ee '/month ?=/d' reference.bib > tmp
	mv tmp reference.bib

$(rmds): ../analyses/stats/methods.tex ../analyses/stats/analyses-main.tex
	make -C ../analyses/stats/

main.pdf: reference.bib $(rmds) sections/intro.tex sections/discussion.tex
	pdflatex main.tex
	bibtex main.aux
	pdflatex main.tex
	pdflatex main.tex
