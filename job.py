from mpi4py import MPI

from functools import wraps

# def parallel_debug(func):
#     """
#     Defines a decorator that wraps a method with all MPI ranks reporting entry
#     And only rank==0 reporting exit.
#     """
#     count = 0 # used to generate a unique id for debuging
# 
#     @wraps(func)
#     def wrapper(self, verbose=1):
# 
#         nonlocal count # only works for nested function !!!
#         count += 1
#         cid = count
# 
#         funcname = f"{func.__name__}_{cid}"
# 
#         try:
#             if verbose: 
#                 funcname = f"{func.__name__}_{cid}"
#                 print(f"[Rank {self.rank}] Start collective func {funcname}", flush=True)
# 
#             result = func(self)
# 
#             if verbose and self.rank == 0:
#                 print(f"End collective func {funcname}", flush=True)
# 
#             return result
# 
#         except Exception as e:
#             print(f"[Rank {self.rank}] Exception in collective method {funcname}: {e}")
#             exit(1)
# 
#     return wrapper

import numpy as np
class Worker:
    def __init__(self, comm=MPI.COMM_WORLD):
        self.comm = comm
        self.rank = comm.Get_rank()
        self.size = comm.Get_size()

        np.random.seed()
        self.ldata = np.random.randint(low=1, high=(self.size+1))

    def lView(self):
        print(f"[Rank {self.rank}] ldata is {self.ldata}.", flush=True)

    def lAdd(self, add_i):
        self.ldata = self.ldata + add_i

    #@parallel_debug
    def gSum(self):
        max = self.comm.allreduce(self.ldata, op=MPI.SUM)
        return max

    #@parallel_debug
    def gGather(self):
        self.gdata = self.comm.allgather(self.ldata)
        if self.rank == 0:
            print(f"The allgather result: {self.gdata}", flush=True)
        
import ipdb; ipdb.set_trace()
comm = MPI.COMM_WORLD
op = Worker()
op.lView()      # view
comm.barrier()

add = op.gSum() # find the sum - collective operation
op.lAdd(add)    # add the sum
if comm.rank == 0:
    print(f"Addition is {add}", flush=True)
op.lView()
comm.barrier()

add = op.gSum()
op.lAdd(add)
if comm.rank == 0:
    print(f"Addition is {add}", flush=True)

comm.barrier()
op.gGather()
