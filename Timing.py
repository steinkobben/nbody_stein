# Program to get and plot the runtime of nbody.cpp in debug and in release mode, and the runtime of nbody.py
# Authors: Stein Köbben, ...
# Student numbers: 4886488, ...
import os
import time
import matplotlib.pyplot as plt
import numpy as np


def time_programs():
    """
    when timing the programs comment out the writing of the csv files.
    """
    for n in [5000, 500000, 5000000, 50000000]:
        t_py_start = time.perf_counter()
        os.system(f"nbody.py {n}")
        t_py_end = time.perf_counter()
        print(t_py_end - t_py_start)


# Python:
# time for 5000 iterations: 0.27627690000000005
# time for 500000 iterations: 4.020867
# time for 5000000 iterations: 45.668577299999995
# time for 50000000 iterations: 596.3705481

# C++ debug
# time for 5000 iterations: 0.015
# time for 500000 iterations: 0.851
# time for 5000000 iterations: 4.836
# time for 50000000 iterations: 46.258

# C++ release
# time for 5000 iterations: 0.004
# time for 500000 iterations: 0.13
# time for 5000000 iterations: 0.515
# time for 50000000 iterations: 4.469

def plot_timings():
    runtimes = [[0.27627690000000005, 0.015, 0.004], [4.020867, 0.851, 0.13], [45.668577299999995, 4.836, 0.515], [596.3705481, 46.258, 4.469]]
    x = np.arange(len(runtimes[0])) + 0.3

    for i in range(4):
        plt.bar(x, runtimes[i])
        plt.ylabel("runtime [s]")
        plt.show()


plot_timings()
# time_programs()
