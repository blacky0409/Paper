SOFFICE := /usr/bin/soffice 

.PHONY: all
all: file_extents_git.pdf free_block_git.pdf continuous_free_segment_fsfs.pdf free_segment_f2fs.pdf file_extents_f2fs.pdf file_block_f2fs.pdf file_extents_ext4.pdf file_block_ext4.pdf free_extents_ext4.pdf free_block_ext4.pdf file_extents_rocksdb.pdf file_block_rocksdb.pdf free_extents_rocksdb.pdf free_block_rocksdb.pdf save_latency.pdf load_latency.pdf aging_duration.pdf ext_latency.pdf f2fs_vs_ext4_latency.pdf ext4_dynamic.pdf f2fs_vs_ext4_dynamic.pdf
	
.PHONY: clean
clean:
	@rm -f pg*.pdf \~* doc_data.txt

graphs.pdf: graphs.pptx

%.pdf: %.pptx
	touch figures.pptx
	$(SOFFICE) --convert-to pdf $< --outdir $(@D)
	pdfcrop $@ $@

pg%.pdf: graphs.pdf
	@echo "Working on page $*"
	@pdftk $< cat $* output - | pdfcrop - $@ > /dev/null

.INTERMEDIATE: pg1.pdf pg2.pdf

file_extents_git.pdf: pg1.pdf
	@mv $< $@

free_block_git.pdf: pg2.pdf
	@mv $< $@

continuous_free_segment_fsfs.pdf: pg3.pdf
	@mv $< $@

free_segment_f2fs.pdf: pg4.pdf
	@mv $< $@

file_extents_f2fs.pdf: pg5.pdf
	@mv $< $@

file_block_f2fs.pdf: pg6.pdf
	@mv $< $@

file_extents_ext4.pdf: pg7.pdf
	@mv $< $@

file_block_ext4.pdf: pg8.pdf
	@mv $< $@

free_extents_ext4.pdf: pg9.pdf
	@mv $< $@

free_block_ext4.pdf: pg10.pdf
	@mv $< $@

file_extents_rocksdb.pdf: pg11.pdf
	@mv $< $@

file_block_rocksdb.pdf: pg12.pdf
	@mv $< $@

free_extents_rocksdb.pdf: pg13.pdf
	@mv $< $@

free_block_rocksdb.pdf: pg14.pdf
	@mv $< $@

save_latency.pdf: pg15.pdf
	@mv $< $@

load_latency.pdf: pg16.pdf
	@mv $< $@

aging_duration.pdf: pg17.pdf
	@mv $< $@

ext_latency.pdf: pg18.pdf
	@mv $< $@

f2fs_vs_ext4_latency.pdf: pg19.pdf
	@mv $< $@

ext4_dynamic.pdf: pg20.pdf
	@mv $< $@

f2fs_vs_ext4_dynamic.pdf: pg21.pdf
	@mv $< $@