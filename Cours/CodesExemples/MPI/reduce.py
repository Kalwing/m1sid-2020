from mpi4py import MPI
import numpy as np
rank=MPI.COMM_WORLD.rank
nbproc=MPI.COMM_WORLD.size
a=rank
print("rank ",rank,": before gather:",a)
b=MPI.COMM_WORLD.reduce(a,op=MPI.SUM,root=0)
print("rank ",rank,": after gather:",b)
