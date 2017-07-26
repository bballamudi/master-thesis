all: thesis

thesis:
	pdflatex -synctex=1 thesis.tex
	bibtex thesis.aux
	pdflatex -synctex=1 thesis.tex
	pdflatex -synctex=1 thesis.tex
	evince thesis.pdf &
clean:
	rm -rf *.log *.aux *synctex.gz *.bbl *.blg *.backup *.out *.aux *.bit *.blg *.bbl *.lof *.log *.lot *.glo *.glx *.gxg *.gxs *.idx *.ilg *.ind *.out *.url *.svn *.toc *.out
