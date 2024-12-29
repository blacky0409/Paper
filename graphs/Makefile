.PHONY: all
all: sample.pdf

.PHONY: clean
clean:
	@rm *.pdf

%.pdf: %.plot %
	./$<
