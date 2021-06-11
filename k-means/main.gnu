#!/usr/bin/gnuplot

set term png
set output "output.png"
set style fill solid border
plot 'data.csv' using 1:2 title "points"

