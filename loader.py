import multiprocessing

# Loader: Is a process object that will be doing the work in terms of loading
# the data submitted into the data_stream. This process will only be pulling
# data out of the shared Queue.
class Loader(multiprocessing.Process):

    # Init our object with the extra Queue object.
    def __init__(self, data_stream):
        multiprocessing.Process.__init__(self)
        self.data_stream = data_stream

    # Run baby, run.
    def run(self):

        # Keep going until the posion pill is detected.
        while True:
            print("hi")
            data = self.data_stream.get()

            if data is None:
                print("Exiting. Posion Pill.")
                break
            else:
                print("Loading... {0}".format(data))

        return
