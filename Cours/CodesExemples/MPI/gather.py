from mpi4py import MPI
import numpy as np
rank=MPI.COMM_WORLD.rank
nbproc=MPI.COMM_WORLD.size
a=rank*10
b=0
print("rank ",rank,": before gather:",a)
b=MPI.COMM_WORLD.gather(a,0)
b=MPI.COMM_WORLD.gather(a,0)
print("rank ",rank,": after gather:",b)
