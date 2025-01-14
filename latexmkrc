@default_files = ('p.tex');

$pdf_mode = 1;		# pdf using pdflatex
$bibtex = 'bibtex -min-crossref=99 %O %S'; 
$pdflatex = "pdflatex --shell-escape -interaction=nonstopmode -file-line-error %O %S";
