from mpi4py import MPI
import numpy as np
rank=MPI.COMM_WORLD.rank
nbproc=MPI.COMM_WORLD.size
if rank==0:
   a=np.random.rand(nbproc)
   print("before bcast:",a)
   b=MPI.COMM_WORLD.bcast(a,0)
else:
   b=MPI.COMM_WORLD.bcast(None,0)
print("after bcast:",b)
