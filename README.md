# python-multiprocessing-example
================================

Just a simple example of some multiprocessing stuff.

This example utilizes a processing pool that will simulate a set of work that
needs to be done. There is also a Queue that is used to send data from the
processes generating the data to the process that is in-charge of loading the
data (planning to make this insert into a database for work).

The Loader class is a multiprocessing.Process object that is extended to include
the Queue that is created in the Crawler class.

A single process is used for loading the generated data so once the processing
pool is completed and joined back into the main process, we can submit a posion
pill (aka None) that will break the Loader out of the run() method. This will
let us exit the Loader process gracefully.

[HERE](https://docs.python.org/3.5/library/multiprocessing.html) is the link to
the docs for the multiprocessing modules.  Please note this is written w/ python
3.5 .
