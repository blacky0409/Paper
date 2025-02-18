.PHONY: all
all: sample-lines.pdf sample-boxes.pdf

.PHONY: clean
clean:
	@rm *.pdf

%.pdf: %.py %
	./$<
