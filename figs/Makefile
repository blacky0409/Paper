.PHONY: all
all: ssd.pdf nvmev-making.pdf free-fragmentation.pdf data-fragmentation.pdf mapping-table.pdf ftl-role.pdf

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

ssd.pdf: pg1.pdf
	@mv $< $@

nvmev-making.pdf: pg2.pdf
	@mv $< $@

free-fragmentation.pdf: pg3.pdf
	@mv $< $@

data-fragmentation.pdf: pg4.pdf
	@mv $< $@

mapping-table.pdf: pg5.pdf
	@mv $< $@

ftl-role.pdf: pg6.pdf
	@mv $< $@

