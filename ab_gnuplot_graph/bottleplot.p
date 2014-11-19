# gnuplot script to plot the output of apache benchmark(ab) data for bottle application
# Author Sachin Deep
# Copyright (c) 2014-2015, RackSpace
# All rights reserved.

# To output a jpeg file
set terminal jpeg size 500,500
# This sets the aspect ratio of the graph
set size 1, 1
# The file to write output
set output "Bottle_performance.jpg"
# The graph title
set title "Bottle Request Plot"
# Where to place the legend/key
set key left top
# Draw gridlines oriented on the y axis
set grid y
# Label the x-axis
set xlabel 'Requests'
# Label the y-axis
set ylabel "Response time (ms)"
# Tell gnuplot to use tabs as the delimiter instead of spaces (default)
set datafile separator '\t'
# Plot from output of apache benchmark data 
plot "bottle.tsv" every ::2 using 5 title 'response time' with lines
exit
