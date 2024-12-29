LATEXMK	= latexmk

SRC_TEX	= $(wildcard *.tex)
SRC_TBL = $(wildcard tbl/*.tex)
SRC_CODE= $(wildcard code/*.tex)
SRC_GRHS= $(wildcard graphs/*.plot) $(wildcard graphs/*)
SRC_FIGS= figs/figures.pdf

TITLE	= p
BIB		= $(wildcard *.bib)
SRC		= $(SRC_TEX) $(SRC_TBL) $(SRC_CODE) $(SRC_GRHS) $(BIB)

PDF		= $(TITLE).pdf

.PHONY: all
all: $(PDF)

.PHONY: open
open:
	@$(LATEXMK) -pv

.PHONY: build
build:
	@$(LATEXMK) -pvc

.PHONY: graphs figs
graphs: $(SRC_GRPHS)
	@echo "[GRAPHS]"
	@make -C graphs

figs: $(SRC_FIGS)
	@echo "[FIGS]"
	@make -C figs

.PHONY: clean
clean:
	@echo "[RM]"
	@$(LATEXMK) -c

.PHONY: distclean
distclean:
	@echo "[DISTCLEAN]"
	@$(LATEXMK) -C
	@find . -iname "*-eps-converted-to.pdf"
	@$(RM) figs/*.eps

.PHONY: spell
spell:	$(SRC_TEX)
	@for f in $(SRC_TEX); do bin/aspell.sh tex $$f; done
	@for f in $(SRC_TEX); do bin/double.pl $$f; done

.PHONY: pdf
pdf: $(PDF)
$(PDF): $(SRC)
	@$(LATEXMK) -quiet
