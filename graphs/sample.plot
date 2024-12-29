#!/usr/bin/env gnuplot
# vim: nowrap
set grid
set grid noxtics linetype 0 # linecolor rgb "gray"

set bmargin 3.5

set xrange [-0.5:3.5]
set yrange [0:*]

set xtics out nomirror scale 0.5 1 1
set ytics

set xlabel "# of nodes"
set ylabel "Normalized throughputs"

set key inside top center horizontal width +2

set style data histogram
set style histogram cluster gap 2.0
set style fill pattern border -1;
#set boxwidth 0.4
set style line 1 lt 1
set style line 2 lt 1
set style line 3 lt 1
set style line 4 lt 1

#set terminal postscript eps color enhanced clip size 8,4 font "Times-Roman" 28 solid
set terminal pdfcairo enhanced mono font "Times,24" size 5,3.1 solid

set output "sample.pdf"
plot "sample" \
	   using 1 lt 1 fs solid 0.2 t "Ethernet", \
	"" using 2 lt 1 fs solid 0.8 t "InfiniBand"
