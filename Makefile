all: thesis

thesis:
	pdflatex -synctex=1 2017_10_Grattarola.tex
	bibtex 2017_10_Grattarola.aux
	pdflatex -synctex=1 2017_10_Grattarola.tex
	pdflatex -synctex=1 2017_10_Grattarola.tex
	evince 2017_10_Grattarola.pdf &
clean:
	rm -rf *.log *.aux *synctex.gz *.bbl *.blg *.backup *.out *.aux *.bit *.blg *.bbl *.lof *.log *.lot *.glo *.glx *.gxg *.gxs *.idx *.ilg *.ind *.out *.url *.svn *.toc *.out
