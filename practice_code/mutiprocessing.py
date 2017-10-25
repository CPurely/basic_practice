import multiprocessing
import os
import time
import numpy


def task(args):
    print("PID =", os.getpid(), ", args =", args)
    return os.getpid(), args


task('test')
pool = multiprocessing.Pool(processes=2)
result = pool.map(task, [1, 2, 3, 4, 5, 6, 7, 8])
