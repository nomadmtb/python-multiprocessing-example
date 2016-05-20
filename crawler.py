import multiprocessing as mp
import time
import random
from loader import Loader

# This function will be the worker that will participate the in the Pool. A
# random amount of time will get calculated to make the simulation a little more
# accurate.
def do_work( data ):
    print("Do workie work")
    data_bus = data[1]
    target = data[0]

    # If the posion pill has been submited just pass it to the Queue.
    # No need to wait for that to process. :)
    if target is None:
        data_bus.put(target)
    else:
        time.sleep(random.uniform(0.1, 5.0))
        data_bus.put("DATA-{0}".format(target))

    return

# Crawler: This class will orchestrate the whole process. It has several
# components that are required to manage the process pool, the loader process
# and the main thread.
class Crawler(object):

    def __init__(self):
        print("Initing")
        manager = mp.Manager()
        self.data_bus = manager.Queue()
        self.loader = Loader(self.data_bus)
        self.generators = mp.Pool(processes=(mp.cpu_count()*2))
        self.targets = []

    def load_targets(self):
        print("Loading targets")
        self.targets = list(range(25))

    def start(self):
        print("Starting")
        self.loader.start() # Start the loading process first
        packaged_data = [ (x, self.data_bus) for x in self.targets ]
        print(packaged_data) # Packing data with Queue embeded in the object
        outputs = self.generators.map(do_work, packaged_data)
        self.generators.close() # Close pool
        self.generators.join() # Wait for the worker process to finish
        print("Pool all done")
        self.data_bus.put(None) # Add poison so the loader will eventually die
        print("All done")

# Main: This function will create our Crawler instance and start it.
if __name__ == '__main__':

    my_crawler = Crawler()
    my_crawler.load_targets()
    my_crawler.start()
