.PHONY: all
all:

.PHONY: clean
clean:
	@rm -f pg*.pdf \~* doc_data.txt

%.pdf: %.odg
	$(SOFFICE) --convert-to-pdf $< -- outdir $(@D)
	pdfcrop $@ $@

figures.pdf: figures.pptx

pg%.pdf: figures.pdf
	@echo "Working on page $*"
	@pdftk $< cat $* output - | pdfcrop - $@ > /dev/null

.INTERMEDIATE: pg1.pdf pg2.pdf

arch.pdf: pg1.pdf
	@mv $< $@
