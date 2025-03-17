.PHONY: all
all: dynamic.pdf latency.pdf dynamic-f2fs.pdf latency-f2fs.pdf aging-duration.pdf

.PHONY: clean
clean:
	@rm *.pdf

%.pdf: %.py %
	./$<
