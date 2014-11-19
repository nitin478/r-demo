Help for Gnuplot and apache benchmark execution

### Description ###
Gnuplot is a command-driven interactive function plotting program.

The ApacheBench tool (ab) can load test servers by sending an arbitrary number of concurrent requests. ab can be used to benchmark any HTTP server.

Apache Bench -g switch gives the file can easily be imported into packages like Gnuplot
The file output by the -g switch of Apache Bench is NOT in time sequence order. It is sorted by ttime (total time).

### Installation on Ubuntu ###
sudo apt-get install apache2-utils

sudo apt-get intall gnuplot

sudo apt-get install gnuplot-x11

### Working with gnuplot Scripts ### 
1. Create .p file 
   touch foo.p   

2. write script data into file and save it.
   gedit foo.p  

3. Generate the plot file of the foo.p by ::
    gnuplot foo.p

### Command to GET Http/Https request ###

Usage: ab [options] [http[s]://]hostname[:port]/path
Options are:
    -n requests     Number of requests to perform
    -c concurrency  Number of multiple requests to make at a time
    -g filename     Output collected data to gnuplot format file.
  
### Examples ### 

Flask Application:
ab -n 1000 -c 100 -g flask.tsv http://172.16.15.26:5000/Rackspace/api/v1.0/product/test-product

Bottle Application:
ab -n 1000 -c 100 -g bottle.tsv http://172.16.15.26:8080/Rackspace/api/v1.0/product/test-product


